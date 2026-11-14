import os
import time
import pickle

import cv2
import joblib
import numpy as np
import torch
import torch.nn.functional as F
from PIL import Image

from torchvision.models import wide_resnet50_2


# Device


if torch.backends.mps.is_available():
    DEVICE = torch.device("mps")
elif torch.cuda.is_available():
    DEVICE = torch.device("cuda")
else:
    DEVICE = torch.device("cpu")



# Paths


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "models")


# Inspectra configuration

CATEGORIES = [
    "bottle",
    "cable",
    "capsule",
    "carpet",
    "grid",
    "hazelnut",
    "leather",
    "metal_nut",
    "pill",
    "screw",
    "tile",
    "toothbrush",
    "transistor",
    "wood",
    "zipper",
]

IMAGE_SIZE = 224
PATCH_GRID_SIZE = 28
FEATURE_DIMENSION = 1536
PCA_DIMENSION = 128
MEMORY_BANK_SIZE = 2048

 
# WideResNet50-2 Backbone
 

MODEL_PATH = os.path.join(MODEL_DIR, "wide_resnet50_2.pth")

backbone = wide_resnet50_2(weights=None)

# Load the trained ImageNet weights saved from Colab
state_dict = torch.load(
    MODEL_PATH,
    map_location="cpu",
    weights_only=True
)

backbone.load_state_dict(state_dict)
backbone = backbone.to(DEVICE)
backbone.eval()

 
# Feature Extraction Hooks
 

features = {}


def hook_layer2(module, inputs, output):
    features["layer2"] = output


def hook_layer3(module, inputs, output):
    features["layer3"] = output


handle2 = backbone.layer2.register_forward_hook(hook_layer2)
handle3 = backbone.layer3.register_forward_hook(hook_layer3)


 
# Image Preprocessing
 

IMAGENET_MEAN = [0.485, 0.456, 0.406]
IMAGENET_STD = [0.229, 0.224, 0.225]


def preprocess_image(image_path):
    image = Image.open(image_path).convert("RGB")

    image = image.resize((256, 256))

    left = (256 - IMAGE_SIZE) // 2
    top = (256 - IMAGE_SIZE) // 2

    image = image.crop(
        (left, top, left + IMAGE_SIZE, top + IMAGE_SIZE)
    )

    image = np.array(image).astype(np.float32) / 255.0

    mean = np.array(IMAGENET_MEAN, dtype=np.float32)
    std = np.array(IMAGENET_STD, dtype=np.float32)

    image = (image - mean) / std

    image = torch.from_numpy(image).permute(2, 0, 1).float()

    image = image.unsqueeze(0)

    return image.to(DEVICE)

 
# Patch Feature Extraction
 

def extract_patch_features(image_tensor):
    """
    Extract and combine Layer 2 and Layer 3 features,
    then convert them into normalized patch embeddings.
    """

    features.clear()

    with torch.no_grad():
        _ = backbone(image_tensor)

    layer2 = features["layer2"]
    layer3 = features["layer3"]

    # Layer 3: 14x14 → 28x28
    layer3 = F.interpolate(
        layer3,
        size=layer2.shape[-2:],
        mode="bilinear",
        align_corners=False
    )

    # Combine Layer 2 (512) + Layer 3 (1024)
    combined = torch.cat([layer2, layer3], dim=1)

    # Convert:
    # [B, C, H, W] → [B, H, W, C]
    combined = combined.permute(0, 2, 3, 1)

    B, H, W, C = combined.shape

    # Convert spatial locations into patches
    patches = combined.reshape(B, H * W, C)

    # L2 normalize each patch
    patches = F.normalize(patches, p=2, dim=2)

    return patches


 
# Model Artifacts
 

from sklearn.neighbors import NearestNeighbors


# Load category-specific thresholds
thresholds_path = os.path.join(MODEL_DIR, "thresholds.csv")
thresholds_data = {}

with open(thresholds_path, "r") as f:
    next(f)  # Skip header

    for line in f:
        parts = line.strip().split(",")

        if len(parts) >= 2:
            category = parts[0]
            threshold = float(parts[1])
            thresholds_data[category] = threshold


# Cache loaded PCA, memory banks and NN models
category_models = {}


def load_category_model(category):
    """
    Load the PCA model, memory bank and nearest-neighbor
    model for a specific product category.
    """

    if category not in CATEGORIES:
        raise ValueError(
            f"Unsupported category: {category}"
        )

    # Return cached model if already loaded
    if category in category_models:
        return category_models[category]

    category_dir = os.path.join(
        MODEL_DIR,
        category
    )

    memory_bank_path = os.path.join(
        category_dir,
        "memory_bank.npy"
    )

    pca_path = os.path.join(
        category_dir,
        "pca.pkl"
    )

    # Load memory bank
    memory_bank = np.load(memory_bank_path)

    # Load PCA
    pca_model = joblib.load(pca_path)

    # Create nearest-neighbor search
    nn_search = NearestNeighbors(
        n_neighbors=1,
        metric="euclidean",
        n_jobs=-1
    )

    nn_search.fit(memory_bank)

    threshold = thresholds_data.get(category)

    if threshold is None:
        raise ValueError(
            f"No threshold found for category: {category}"
        )

    category_models[category] = {
        "memory_bank": memory_bank,
        "pca": pca_model,
        "nn_search": nn_search,
        "threshold": threshold
    }

    return category_models[category]

 
# Anomaly Map
 

def create_anomaly_map(patch_distances):
    """
    Convert 784 patch distances into a 28x28 anomaly map.
    """

    anomaly_map = patch_distances.reshape(
        PATCH_GRID_SIZE,
        PATCH_GRID_SIZE
    )

    # Normalize for visualization
    anomaly_map = anomaly_map.astype(np.float32)

    min_value = anomaly_map.min()
    max_value = anomaly_map.max()

    if max_value > min_value:
        anomaly_map = (
            anomaly_map - min_value
        ) / (
            max_value - min_value
        )

    # Resize to input image resolution
    anomaly_map = cv2.resize(
        anomaly_map,
        (IMAGE_SIZE, IMAGE_SIZE),
        interpolation=cv2.INTER_LINEAR
    )

    return anomaly_map


 
# Main Prediction Function
 

def predict(image_path, category):
    """
    Run Inspectra anomaly detection on one image.

    Returns:
        prediction
        anomaly_score
        threshold
        anomaly_map
        processing_time
    """

    start_time = time.time()

    # Load category-specific model
    model = load_category_model(category)

    pca_model = model["pca"]
    nn_search = model["nn_search"]
    threshold = model["threshold"]

    # Preprocess image
    image_tensor = preprocess_image(image_path)

    # Extract patch embeddings
    patches = extract_patch_features(image_tensor)

    # Move features to CPU / NumPy
    patches_np = patches.detach().cpu().numpy()

    batch_size, num_patches, feature_dim = patches_np.shape

    # Flatten patches
    patches_flat = patches_np.reshape(
        -1,
        feature_dim
    )

    # PCA: 1536 → 128
    reduced_features = pca_model.transform(
        patches_flat
    )

    # Nearest-neighbor distance
    distances, _ = nn_search.kneighbors(
        reduced_features
    )

    distances = distances.reshape(
        batch_size,
        num_patches
    )

    # Image-level anomaly score
    anomaly_score = float(
        distances.max()
    )

    # Generate anomaly map
    patch_distances = distances[0]

    anomaly_map = create_anomaly_map(
        patch_distances
    )

    # Classification
    if anomaly_score > threshold:
        prediction = "Defective"
    else:
        prediction = "Normal"

    processing_time = time.time() - start_time

    return {
        "prediction": prediction,
        "anomaly_score": anomaly_score,
        "threshold": float(threshold),
        "anomaly_map": anomaly_map,
        "processing_time": processing_time
    }
