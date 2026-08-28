# A Survey on RGB, 3D, and Multimodal Approaches for Unsupervised Industrial Image Anomaly Detection

## Basic Information

- **Authors:** Yuxuan Lin, Yang Chang, Xuan Tong, Jiawen Yu, Antonio Liotta, Guofan Huang, Wei Song, Deyu Zeng, Zongze Wu, Yan Wang, Wenqiang Zhang
- **Year:** 2025
- **Type:** Survey Paper
- **Source:** arXiv / Preprint submitted to Elsevier
- **arXiv ID:** 2410.21982v2
- **Keywords:** Unsupervised Learning, Multimodal Fusion, Anomaly Detection, Industrial Scene

## Problem Statement

Industrial quality inspection often faces a major challenge: **defective samples are rare**, making it difficult to collect enough labelled anomaly data for supervised deep learning.

Traditional manual inspection is also:

- Time-consuming
- Dependent on human attention
- Difficult to scale
- Less effective in complex industrial environments

Many existing industrial anomaly detection approaches mainly focus on **RGB images**. However, RGB images alone may not capture all information required to detect complex defects.

For example:

- RGB images provide color and texture information.
- 3D data provides structural and spatial information.
- Combining multiple data types can provide more complete information about a product.

Therefore, there is a need for more comprehensive industrial anomaly detection approaches using **RGB, 3D, and multimodal data**. :contentReference[oaicite:0]{index=0}

## Objective

The objective of this paper is to provide a comprehensive survey of **Unsupervised Industrial Image Anomaly Detection (UIAD)** in three different settings:

1. **RGB-based anomaly detection**
2. **3D-based anomaly detection**
3. **Multimodal anomaly detection**

The paper reviews:

- Existing datasets
- Detection methods
- Model architectures
- Learning approaches
- Multimodal fusion strategies
- Challenges
- Future research directions

:contentReference[oaicite:1]{index=1}

## Core Concept: Unsupervised Anomaly Detection

Unlike supervised learning, unsupervised anomaly detection mainly uses **normal product samples for training**.

The general workflow is:

Normal Product Images  
→ Data Processing  
→ Learn Normal Patterns  
→ Train Model  

During testing:

New Product Image  
→ Data Processing  
→ Compare with Learned Normal Pattern  
→ Calculate Anomaly Score  
→ Detect Defect

A higher anomaly score indicates that the product is more likely to contain an abnormality or defect. :contentReference[oaicite:2]{index=2}

## Methodology

Since this is a **survey paper**, it does not propose one specific model.

Instead, it organizes existing UIAD research into three major categories.

### 1. RGB-Based Anomaly Detection

Uses normal RGB images to identify visual defects.

Common methods include:

- Reconstruction-based methods
- Feature embedding methods
- Memory bank methods
- Distribution map methods
- Teacher-student architectures
- One-class classification

RGB is useful for detecting:

- Surface defects
- Color abnormalities
- Texture changes
- Assembly errors

### 2. 3D-Based Anomaly Detection

Uses 3D information such as:

- Point clouds
- Depth maps
- Spatial information

3D data can help detect structural abnormalities that may not be clearly visible in RGB images.

### 3. Multimodal Anomaly Detection

Combines multiple types of information, such as:

- RGB + Point Cloud
- RGB + Depth

The paper discusses several multimodal fusion strategies:

- Early Fusion
- Middle Fusion
- Late Fusion
- Hybrid Fusion

The survey explains that different data modalities can compensate for the limitations of a single modality. :contentReference[oaicite:3]{index=3}

## Learning Approaches

The paper also reviews modern learning strategies, including:

- Few-shot learning
- Zero-shot learning
- Multi-class learning
- Continual learning
- Large model-based approaches
- Anomaly simulation learning

These approaches are useful when limited labelled industrial data is available.

## Important Datasets

The paper reviews several datasets for industrial anomaly detection.

### RGB Datasets

- MVTec AD
- BTAD
- MPDD
- MVTec LOCO-AD
- VisA
- GoodsAD
- Real-IAD
- RAD

### 3D Datasets

- Real3D-AD
- Anomaly-ShapeNet

### Multimodal Datasets

- MVTec 3D-AD
- PD-REAL
- Eyecandies

These datasets include RGB images, point clouds, depth information, and different types of industrial defects. :contentReference[oaicite:4]{index=4}

## Key Challenges

The paper identifies several challenges in real-world industrial anomaly detection.

### 1. Small-Scale Defects

Very small or subtle defects can be difficult to detect, especially in high-resolution industrial images.

### 2. Complex Industrial Environments

Lighting, noise, different product surfaces, and changing working conditions can affect detection accuracy.

### 3. Generalization

A model trained on one product or manufacturing environment may not perform well on another.

### 4. Large-Scale 3D Data

Processing large point clouds can require significant computational resources.

### 5. Multimodal Alignment

RGB and 3D data may not always be perfectly aligned because of differences in camera angles or data collection errors.

### 6. Real-World Deployment

Models need to be lightweight, fast, reliable, and suitable for real-time production environments. :contentReference[oaicite:5]{index=5}

## Future Directions

The paper suggests future research in:

- More transferable models
- Better generalization across industries
- Detection of tiny and subtle defects
- Efficient processing of high-resolution images
- Better multimodal fusion
- Noise-resistant models
- Few-shot and zero-shot anomaly detection
- Lightweight models for real-time deployment
- Multi-class anomaly detection

:contentReference[oaicite:6]{index=6}

## Key Advantages

- Provides a comprehensive overview of RGB, 3D, and multimodal anomaly detection.
- Covers multiple datasets and model architectures.
- Explains different learning approaches.
- Discusses multimodal fusion strategies.
- Identifies real-world challenges.
- Provides useful future research directions.

## Limitations

Since this is a **survey paper**, it does not provide a new model or direct experimental results.

Instead, its main contribution is the comparison and organization of existing research.

## Research Gap

The paper highlights that many existing industrial anomaly detection systems:

- Focus mainly on RGB images.
- Struggle to generalize across different products.
- Require large amounts of training data.
- Have difficulty detecting very small defects.
- Face challenges when deployed in real production environments.

Multimodal approaches can improve defect detection, but challenges remain in:

- Data collection
- Modal alignment
- Efficient fusion
- Real-time deployment

## Relevance to Inspectra

This paper is highly relevant to **Inspectra** because our project focuses on AI-based industrial quality inspection and defect detection.

The biggest takeaway is that Inspectra does not necessarily need to depend only on labelled defective samples.

An unsupervised approach could allow the system to:

Normal Product Images  
→ Learn Normal Appearance  
→ Capture New Product Image  
→ Calculate Anomaly Score  
→ Detect Possible Defect

For the initial version of Inspectra, we can start with:

**RGB Image-Based Inspection**

Later, the system can be extended to support:

**RGB + Depth / 3D Information**

The paper also highlights important areas for Inspectra:

- Detecting small defects
- Generalizing across different products
- Working with limited defect data
- Real-time processing
- Few-shot or zero-shot learning
- Future multimodal inspection

Overall, this paper provides a strong research foundation for deciding the future architecture and direction of the Inspectra project. :contentReference[oaicite:7]{index=7}
