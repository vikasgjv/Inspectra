# Inspectra

## AI-Powered Visual Quality Inspection System

Inspectra is an AI-based industrial visual inspection system designed to detect product anomalies and defects using computer vision and deep learning.

The system uses a PatchCore-style anomaly detection pipeline with a pretrained WideResNet50-2 backbone and the MVTec AD dataset.

## Project Overview

Traditional manual inspection can be slow, inconsistent, and difficult to scale.

Inspectra aims to provide automated visual inspection by analyzing product images and identifying regions that differ from normal product appearance.

## ML Pipeline

MVTec AD
↓
Image Preprocessing
↓
WideResNet50-2
↓
Layer 2 + Layer 3 Features
↓
Patch Feature Extraction
↓
PCA Dimensionality Reduction
↓
Memory Bank
↓
Nearest Neighbor Search
↓
Anomaly Score
↓
Normal / Defective
↓
Anomaly Localization

## Dataset

The project uses the MVTec Anomaly Detection (MVTec AD) dataset.

The current implementation covers 15 categories:

- Bottle
- Cable
- Capsule
- Carpet
- Grid
- Hazelnut
- Leather
- Metal Nut
- Pill
- Screw
- Tile
- Toothbrush
- Transistor
- Wood
- Zipper

The model is built using only normal (`good`) training samples and detects deviations during testing.

## Model

### Backbone

- WideResNet50-2
- ImageNet pretrained
- Layer 2 and Layer 3 feature extraction

### Anomaly Detection

- PatchCore-style pipeline
- Patch-level feature extraction
- PCA dimensionality reduction
- MiniBatchKMeans-based memory-bank reduction
- Nearest-neighbor anomaly scoring
- Category-specific thresholds
- Anomaly map generation

> The current implementation uses MiniBatchKMeans as a scalable approximation for memory-bank reduction rather than the original greedy coreset selection used in standard PatchCore.

## Evaluation

The system was evaluated across all 15 MVTec AD categories using:

- Image-level AUROC
- Pixel-level AUROC
- Precision
- Recall
- F1-score
- Anomaly localization

Results and evaluation files are available in the `results/` directory.

## Project Structure

```text
Inspectra/
├── research/
├── notebooks/
│   └── Inspectra_PatchCore.ipynb
├── results/
│   ├── metrics/
│   └── visualizations/
├── backend/
├── README.md
├── requirements.txt
└── .gitignore
