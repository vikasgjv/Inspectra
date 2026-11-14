import os
import shutil
import uuid
import cv2

from fastapi import FastAPI, UploadFile, File, Form
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from .ml_engine import predict


app = FastAPI(
    title="Inspectra API",
    description="AI-powered industrial visual inspection system",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount(
    "/uploads",
    StaticFiles(directory="backend/uploads"),
    name="uploads"
)

app.mount(
    "/frontend",
    StaticFiles(directory="frontend"),
    name="frontend"
)


@app.get("/")
def home():
    return FileResponse("frontend/index.html")


@app.post("/predict")
async def predict_image(
    image: UploadFile = File(...),
    category: str = Form(...)
):
    upload_dir = "backend/uploads"
    os.makedirs(upload_dir, exist_ok=True)

    filename = f"{uuid.uuid4()}_{image.filename}"
    image_path = os.path.join(upload_dir, filename)

    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    result = predict(image_path, category)

    # Save anomaly heatmap
    heatmap = result["anomaly_map"]

    heatmap_uint8 = (heatmap * 255).astype("uint8")

    colored_heatmap = cv2.applyColorMap(
        heatmap_uint8,
        cv2.COLORMAP_JET
    )

    heatmap_filename = f"{uuid.uuid4()}_heatmap.jpg"
    heatmap_path = os.path.join(upload_dir, heatmap_filename)

    cv2.imwrite(heatmap_path, colored_heatmap)

    # Create heatmap overlay
    original = cv2.imread(image_path)

    original = cv2.resize(original, (224, 224))
    overlay = cv2.addWeighted(
    original,
    0.6,
    colored_heatmap,
    0.4,
    0
    )

    overlay_filename = f"{uuid.uuid4()}_overlay.jpg"
    overlay_path = os.path.join(upload_dir, overlay_filename)

    cv2.imwrite(overlay_path, overlay)


    return {
        "category": category,
        "prediction": result["prediction"],
        "anomaly_score": result["anomaly_score"],
        "threshold": result["threshold"],
        "processing_time": result["processing_time"],
        "heatmap_url": f"/uploads/{heatmap_filename}",
        "overlay_url" : f"/uploads/{overlay_filename}"
    }