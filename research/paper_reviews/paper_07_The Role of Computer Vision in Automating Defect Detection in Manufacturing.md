# The Role of Computer Vision in Automating Defect Detection in Manufacturing

## Basic Information

- **Authors:** Vijayalakshmi G, Jagmeet Sohal, Shankar Prasd S, Santosh Kumar, S. Arul Antran Vijay, Prateek Garg
- **Year:** 2024
- **Conference:** 2024 IEEE 4th International Conference on ICT in Business, Industry & Government (ICTBIG)
- **Publisher:** IEEE
- **Type:** Conference Paper
- **Date of Conference:** 13–14 December 2024
- **Date Added to IEEE Xplore:** 13 March 2025
- **DOI:** 10.1109/ICTBIG64922.2024.10911417
- **Paper Link:** https://ieeexplore.ieee.org/document/10911417

## Problem Statement

Traditional defect detection methods in manufacturing may struggle to detect complex and changing defects efficiently.

Many approaches focus mainly on static image analysis and may not effectively handle defects that evolve over time. Delayed defect detection can also lead to the production of more defective products.

## Objective

The objective of this paper is to develop a computer vision-based approach for automated defect detection in manufacturing.

The proposed approach aims to improve:

- Feature extraction
- Detection of dynamically changing defects
- Object detection
- Real-time monitoring
- Manufacturing quality control

## Methodology

The proposed approach combines three main components:

### 1. CNN-Based Feature Extraction

Convolutional Neural Networks (CNNs) are used to extract important and detailed features from images of manufacturing objects.

This helps the system identify small or subtle defect-related features.

### 2. RNN-Based Temporal Analysis

Recurrent Neural Networks (RNNs) are used to analyze defects that change or develop over time.

This component addresses situations where static image-based analysis may not be sufficient.

### 3. Object Detection and Real-Time Monitoring

Object detection is used to identify defects, while real-time monitoring enables faster responses when faults are detected.

This can help reduce the number of defective products produced.

## Dataset

The proposed approach was tested using a **well-annotated dataset**.

However, the provided abstract does not specify:

- Dataset name
- Number of images or samples
- Number of defect classes
- Dataset source

## Results

According to the abstract, the proposed approach achieved better:

- Precision
- Accuracy
- F1-score

when compared with more conventional defect detection methods.

The CNN-based feature extraction approach showed competitive performance, particularly in terms of accuracy.

The RNN-based temporal analysis performed well in situations where defects changed dynamically over time.

The abstract does not provide exact numerical values for the performance metrics.

## Key Advantages

- Combines spatial and temporal analysis.
- Uses CNNs to extract detailed visual features.
- Uses RNNs to analyze defects that change over time.
- Supports object detection.
- Enables real-time monitoring.
- Aims to reduce the production of defective goods.
- Designed to handle dynamic and complex manufacturing defects.

## Limitations / Challenges

Based on the information available in the abstract, some limitations include:

- The dataset details are not specified.
- Exact performance values are not provided.
- The abstract does not provide detailed information about computational requirements.
- Real-world deployment performance across different manufacturing environments is not described.

## Research Gap

Traditional defect detection systems may focus mainly on static image analysis and may not effectively handle defects that evolve over time.

There is a need for automated inspection systems that can combine:

- Detailed visual feature extraction
- Temporal analysis
- Object detection
- Real-time monitoring

Such systems can potentially provide faster and more adaptive quality control in manufacturing environments.

## Relevance to Inspectra

This paper is relevant to Inspectra because it demonstrates how multiple AI techniques can be combined for automated manufacturing inspection.

The proposed concept can be represented as:

Image / Video Input
→ CNN-Based Feature Extraction
→ RNN-Based Temporal Analysis
→ Object Detection
→ Real-Time Monitoring
→ Quality Decision

A key insight for Inspectra is that defect detection does not necessarily need to rely only on a single image classification model.

For applications involving continuous monitoring or video data, analyzing how defects change over time could provide an additional approach for improving automated quality inspection.
