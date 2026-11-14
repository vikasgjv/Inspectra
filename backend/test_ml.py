import os
import cv2
import numpy as np

from app.ml_engine import predict


# --------------------------------------------------
# Input
# --------------------------------------------------

IMAGE_PATH = "/Applications/7CAI/mvtec_anomaly_detection/bottle/test/contamination/007.png"
CATEGORY = "bottle"


# --------------------------------------------------
# Run Inspectra
# --------------------------------------------------

result = predict(IMAGE_PATH, CATEGORY)


print("\n--- Inspectra Prediction ---")
print("Category:", CATEGORY)
print("Prediction:", result["prediction"])
print("Anomaly Score:", result["anomaly_score"])
print("Threshold:", result["threshold"])
print("Processing Time:", result["processing_time"], "seconds")
print("Anomaly Map Shape:", result["anomaly_map"].shape)


# --------------------------------------------------
# Create visualization
# --------------------------------------------------

# Read original image
original = cv2.imread(IMAGE_PATH)

# Resize and center crop to match ML input (224x224)
original = cv2.resize(original, (256, 256))

left = (256 - 224) // 2
top = (256 - 224) // 2

original = original[
    top:top + 224,
    left:left + 224
]


# Get anomaly map
anomaly_map = result["anomaly_map"]


# Convert anomaly map to 0-255
heatmap = (anomaly_map * 255).astype(np.uint8)


# Apply OpenCV heatmap
heatmap = cv2.applyColorMap(
    heatmap,
    cv2.COLORMAP_JET
)


# Overlay heatmap on original image
overlay = cv2.addWeighted(
    original,
    0.6,
    heatmap,
    0.4,
    0
)


# --------------------------------------------------
# Save result
# --------------------------------------------------

output_dir = "backend/results"
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(
    output_dir,
    "bottle_contamination_result.jpg"
)

cv2.imwrite(output_path, overlay)


print("\n--- Visualization ---")
print("Saved result to:")
print(output_path)