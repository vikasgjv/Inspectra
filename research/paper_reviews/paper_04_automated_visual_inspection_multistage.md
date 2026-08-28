# Improving Automated Visual Fault Inspection for Semiconductor Manufacturing Using a Hybrid Multistage System of Deep Neural Networks

## Basic Information

- **Authors:** Tobias Schlosser, Michael Friedrich, Frederik Beuth, Danny Kowerko
- **Year:** 2022
- **Journal:** Journal of Intelligent Manufacturing
- **Type:** Research Paper
- **DOI:** 10.1007/s10845-021-01906-9

## Problem Statement

In semiconductor manufacturing, very small defects can occur on large, high-resolution wafer images.

These defects may be only a few micrometers or pixels in size, making them difficult to detect using traditional computer vision or a single deep learning model.

The challenge is to achieve accurate defect detection while also satisfying real-time processing requirements.

## Objective

The objective of this paper is to develop an automated visual fault inspection system that can accurately detect and classify very small semiconductor manufacturing defects.

The proposed system aims to improve both:

- Defect detection accuracy
- Real-time processing performance

## Methodology

The authors propose a **Hybrid Multistage System of Stacked Deep Neural Networks (SH-DNN)**.

The system combines classical computer vision with deep learning.

### Main stages:

1. **Image Preprocessing and Localization**
   - Histogram equalization
   - Binary thresholding
   - Contour detection
   - Erosion
   - Bounding rectangle generation

2. **Region of Interest Extraction**
   - Relevant wafer and street regions are identified.

3. **Classification**
   - Deep neural networks classify the extracted regions as flawless or faulty.
   - Different models are evaluated, including:
     - Custom CNN
     - MobileNetV2
     - DenseNet
     - ResNet

4. **Multistage Inspection**
   - The inspection process focuses progressively on more detailed regions.
   - This reduces the complexity of detecting very small defects in large images.

## Dataset

The paper uses semiconductor wafer imagery in a created test environment.

The images are processed to identify:

- Chips
- Streets
- Street segments
- Flawless regions
- Faulty regions

The input images used in the classification process have a resolution of **192 × 192 pixels**.

## Results

The proposed SH-DNN system achieved:

- **F1-score: up to 99.5%**
- Improved fault detection compared with conventional approaches.
- Improved fault detection by up to **8.6 times** compared with single DNN-based approaches.
- Processing time of approximately **5.2 ms per chip image sample** using MobileNetV2.

The results show that combining localization with task-specific classification can improve both accuracy and processing speed.

## Limitations / Challenges

Some challenges include:

- The system is evaluated specifically for semiconductor wafer inspection.
- The approach depends on a multistage pipeline designed for the specific manufacturing process.
- Performance comparisons between models can vary depending on:
  - Hardware
  - Image resolution
  - Inspection requirements

Further improvements could include the use of additional sensor information such as:

- Audio
- Heat signatures

## Research Gap

Existing systems often struggle to balance:

- High accuracy
- Real-time performance
- Detection of very small defects
- Processing of high-resolution images

There is a need for flexible inspection systems that can efficiently focus on important regions instead of processing the entire image with one complex model.

## Relevance to Inspectra

This paper is highly relevant to Inspectra because it demonstrates a complete inspection pipeline:

Image Input
→ Preprocessing
→ Defect Region Localization
→ AI Classification
→ Quality Decision

The multistage approach can be useful for Inspectra, especially if our project needs to detect small defects while maintaining fast processing.

A key insight for our project is that combining traditional image processing with AI can sometimes be more efficient than relying on a single deep learning model.
