# Self-Supervised Iterative Refinement for Anomaly Detection in Industrial Quality Control

## Basic Information

- **Authors:** Muhammad Aqeel, Shakiba Sharifi, Marco Cristani, Francesco Setti
- **Year:** 2025
- **Type:** Research Paper
- **Source:** arXiv
- **Paper ID:** arXiv:2408.11561v2

## Problem Statement

Industrial anomaly detection is challenging because defects are often rare, subtle, and difficult to label accurately.

Self-supervised anomaly detection methods usually assume that the training data contains only normal samples. However, in real industrial environments, training data may contain noisy or anomalous samples.

These misleading samples can reduce model performance and increase false positives or false negatives.

## Objective

The objective of this paper is to develop a robust anomaly detection method that can improve detection performance even when the training data contains noisy or misleading samples.

## Methodology

The authors propose the:

**Self-Supervised Iterative Refinement Process (IRP)**

The method uses a cyclic data refinement strategy.

### Main Process

1. Train an anomaly detection model using the available data.
2. Calculate anomaly scores for the training samples.
3. Identify misleading or abnormal data points.
4. Dynamically adjust the exclusion threshold using robust statistical measures.
5. Remove the most misleading samples.
6. Retrain the model using the refined dataset.
7. Repeat the process iteratively to improve data quality and model performance.

The main idea is to reduce the influence of noisy and anomalous samples during training.

## Datasets

The proposed method was evaluated using two industrial anomaly detection datasets:

- **Kolektor Surface-Defect Dataset 2 (KSDD2)**
- **MVTec-AD**

The datasets include different industrial products and defect types.

## Evaluation Metric

The paper uses:

- **AUROC (Area Under the Receiver Operating Characteristic Curve)**

The experiments evaluate model performance under different levels of noise in the training data.

## Results

The proposed IRP method outperformed the compared traditional approaches, including:

- Vanilla model
- One Shot Removal (OSR) model

IRP showed better robustness as noise levels increased.

### Example Results

At different noise levels, the paper reports:

| Model | 0% Noise | 10% Noise | 20% Noise | 30% Noise | 40% Noise | 50% Noise |
|---|---:|---:|---:|---:|---:|---:|
| Vanilla | 0.8931 | 0.8455 | 0.8235 | 0.7797 | 0.7331 | 0.7171 |
| OSR | 0.8960 | 0.8674 | 0.8327 | 0.7916 | 0.7684 | 0.7338 |
| IRP on MVTec-AD | 0.9118 | 0.8797 | 0.8638 | 0.8228 | 0.7965 | 0.7708 |
| IRP on KSDD2 | 0.9403 | 0.9238 | 0.9024 | 0.9109 | 0.8923 | 0.8967 |

The results show that IRP maintains stronger anomaly detection performance, particularly when the training data contains noise.

## Key Advantages

- Does not require perfectly clean training data.
- Uses self-supervised learning.
- Iteratively improves the quality of training data.
- Adapts the exclusion threshold dynamically.
- Performs well under noisy conditions.
- Improves robustness for industrial anomaly detection.

## Limitations / Challenges

The paper identifies several areas for further improvement:

- Training may require multiple iterative refinement cycles.
- Processing capacity needs improvement for faster deployment.
- Long training epochs can affect real-time applicability.
- Detecting extremely subtle defects remains challenging.
- Further work is needed to adapt to newly emerging defect types in real time.

## Research Gap

Many anomaly detection systems assume that training data contains only normal samples.

However, real industrial datasets may contain:

- Noise
- Outliers
- Misleading samples
- Previously unnoticed defects

There is a need for anomaly detection systems that can learn robustly from imperfect training data and adapt to different industrial environments.

## Relevance to Inspectra

This paper is highly relevant to Inspectra because our system may also face limited or imperfect training data.

A useful idea from this paper is:

Image Data
→ Initial AI Model
→ Detect Suspicious / Misleading Samples
→ Refine Training Data
→ Retrain Model
→ Improved Defect Detection

The IRP approach shows that improving the quality of training data can be as important as improving the AI model itself.

For Inspectra, this could be useful if we want to build a system that remains reliable even when the available product images are noisy, limited, or not perfectly labeled.
