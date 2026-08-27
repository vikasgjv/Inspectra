# Deep Learning Model for Automated Visual Inspection of Electronic Boards

## Basic Information

- **Authors:** José Antonio Lara-Chávez, Carlos Avilés-Cruz, Miguel Magos-Rivera
- **Year:** 2025
- **Journal:** Journal of Intelligent Manufacturing
- **Type:** Research Paper
- **DOI:** 10.1007/s10845-025-02748-5

## Problem Statement

Manual inspection of printed circuit boards can be difficult, time-consuming, and uncertain because PCBs contain many small electronic components.

Errors in component assembly can affect product quality and increase production costs.

## Objective

The objective of this paper is to develop a deep learning-based system for automatically detecting assembly errors in printed circuit boards.

The system is designed to inspect a PCB image and determine whether it is correctly assembled or contains one of the predefined defects.

## Methodology

The proposed Convolutional Deep Learning Model consists of three main stages:

1. **Segmentation**
   - Mask R-CNN is used to segment the PCB.

2. **Feature Extraction**
   - CNN-based feature extraction is performed using a hierarchical approach:
     - Coarse features
     - Medium features
     - Fine features

3. **Classification**
   - Fully Connected Neural Networks are used to classify the board.

## Dataset

The authors created their own proprietary dataset.

- Total images: **2,376**
- Image type: RGB
- Board classes: **6**
- One class represents a correctly assembled board.
- Five classes represent assembly defects.

The defects include:

- Missing integrated circuit
- Integrated circuit mounted in the opposite direction
- Diode with reverse polarity
- Integrated circuit in the wrong position
- Resistor with the wrong value

The dataset was split using an **80:20 ratio** for training and evaluation.

## Results

The proposed model achieved:

- **Accuracy: 100%**
- **Zero classification error**

The trained model was implemented in a computer system for real-time PCB inspection.

## Key Advantages

- Combines segmentation, hierarchical feature extraction, and classification.
- Can identify multiple predefined PCB assembly defects.
- Designed for real-time inspection.
- Achieved very high classification performance on the created dataset.

## Limitations

The system was trained and evaluated on a proprietary dataset created from six boards based on a single PCB design.

Therefore, the reported performance may not directly demonstrate generalization to:

- Different PCB designs
- Different manufacturing environments
- Unseen defect types

## Research Gap

A key area for further investigation is the development of inspection systems that can generalize across different products, designs, environments, and unseen defects.

## Relevance to Inspectra

This paper demonstrates a complete automated visual inspection pipeline:

Image Input → Segmentation → Feature Extraction → Classification → Quality Decision

This pipeline is useful as a practical reference for Inspectra when designing an AI-based quality inspection system.
