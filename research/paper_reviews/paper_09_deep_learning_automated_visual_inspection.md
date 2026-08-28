# Deep Learning for Automated Visual Inspection in Manufacturing and Maintenance: A Survey of Open-Access Papers

## Basic Information

- **Year:** 2024
- **Journal:** Applied System Innovation
- **Type:** Survey / Review Paper
- **Topic:** Deep Learning-Based Automated Visual Inspection
- **DOI:** 10.3390/asi7010011

## Problem Statement

Manual visual inspection in manufacturing and maintenance is often:

- Time-consuming
- Expensive
- Error-prone
- Dependent on human expertise

Although deep learning has shown strong potential for automating visual inspection, there is a wide range of models, datasets, inspection tasks, and industrial applications.

This makes it difficult to determine:

- Which deep learning models are commonly used
- Which methods perform well for different inspection tasks
- Which datasets are available
- What challenges still exist in automated visual inspection

## Objective

The objective of this paper is to provide a comprehensive review of deep learning-based automated visual inspection in manufacturing and maintenance.

The study analyzes:

- Deep learning models used in industrial visual inspection
- Different inspection tasks
- Manufacturing and maintenance applications
- Available datasets
- Model performance
- Current research gaps
- Future research opportunities

## Methodology

The authors conducted a systematic literature review of open-access research papers.

The review process involved:

1. Searching for publications related to deep learning and automated visual inspection.
2. Applying filters to focus on industrial applications.
3. Considering publications using 2D image data.
4. Selecting papers that clearly described the task, method, dataset, and performance.

The initial search identified **6,583 publications**.

After filtering and reviewing the papers, the final study analyzed **196 open-access publications** related to deep learning-based automated visual inspection. :contentReference[oaicite:0]{index=0}

## Areas Covered

The reviewed papers were divided into two major application areas:

- **Manufacturing**
- **Maintenance**

The survey found that:

- **31.7%** of the reviewed publications focused on manufacturing.
- **68.3%** focused on maintenance. :contentReference[oaicite:1]{index=1}

## Inspection Tasks

The paper identifies four major automated visual inspection tasks:

- Binary Classification
- Multi-Class Classification
- Binary Localization
- Multi-Class Localization

These tasks are related to common computer vision approaches:

- Image Classification
- Object Detection
- Image Segmentation :contentReference[oaicite:2]{index=2}

## Deep Learning Models

The survey found that Convolutional Neural Networks (CNNs) are the most commonly used models in industrial automated visual inspection.

The reviewed approaches include:

- CNN
- ResNet
- EfficientNet
- YOLO
- Mask R-CNN
- Faster R-CNN
- U-Net
- DeepLab
- Vision Transformers
- Swin Transformer
- DETR

The paper also highlights the growing use of **Vision Transformers**, which show strong potential but generally require more computational resources. :contentReference[oaicite:3]{index=3}

## Datasets

The paper analyzes datasets used for industrial visual inspection.

Some commonly used datasets include:

- NEU Surface Defect Database
- SDNET 2018
- Crack Forest Dataset
- Road Damage Dataset
- Severstal Dataset
- Magnetic Tile Surface Dataset

The study found **77 open datasets** in the reviewed publications, but only **14 datasets** were reused more than once for benchmarking. :contentReference[oaicite:4]{index=4} :contentReference[oaicite:5]{index=5}

## Key Findings

The study found that:

- CNN-based models are currently the most widely used.
- Most industrial inspection systems use supervised learning.
- Approximately **97%** of the reviewed publications used supervised learning.
- The median dataset size was around **2,500 samples**.
- Small datasets can make training deep learning models from scratch difficult.
- Self-supervised learning could help reduce the requirement for large amounts of labeled data.
- There is approximately a **2–3 year gap** between new computer vision research and its adoption in industrial visual inspection. :contentReference[oaicite:6]{index=6} :contentReference[oaicite:7]{index=7}

## Results and Recommendations

The survey suggests that different models are suitable for different inspection tasks.

For localization-based applications, methods such as:

- YOLO
- Mask R-CNN
- U-Net
- DeepLab

are commonly used.

For classification tasks, the paper recommends considering:

- ResNet
- EfficientNet

The choice of model should depend on factors such as:

- Accuracy
- Real-time performance
- Hardware limitations
- Dataset size
- Need for defect localization

## Limitations / Challenges

The paper identifies several challenges:

- Small and imbalanced datasets
- Limited availability of labeled defect samples
- Poor dataset documentation
- Difficulty in comparing results between different studies
- Generalization to new environments
- Real-time processing requirements
- Hardware constraints
- Limited explainability of deep learning models

The survey itself is limited to **2D image data** and provides only a concise treatment of individual models and training methods. :contentReference[oaicite:8]{index=8}

## Research Gap

The paper highlights several important research gaps:

- Greater use of self-supervised learning for industrial inspection.
- Better generalization across different industrial environments.
- More detailed and standardized dataset descriptions.
- Increased use of public benchmark datasets.
- Improved explainability of AI models.
- More research on Vision Transformers for industrial inspection.
- Development of lightweight models suitable for edge devices.

## Relevance to Inspectra

This paper is highly relevant to Inspectra because it provides a broad overview of the main technologies used for AI-based industrial quality inspection.

The paper supports the use of computer vision techniques for tasks such as:

Image / Video Input  
→ Classification / Object Detection / Segmentation  
→ Defect Identification  
→ Quality Decision  

For Inspectra, the main takeaway is that the model should be selected based on the specific inspection task:

- **Classification** → Determine whether a product is defective.
- **Object Detection** → Locate defects using bounding boxes.
- **Segmentation** → Identify the exact defective area.

The paper also highlights important factors for our project, including **limited training data, generalization, real-time performance, and hardware constraints**.
