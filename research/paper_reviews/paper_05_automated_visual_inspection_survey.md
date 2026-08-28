# Deep Learning for Automated Visual Inspection in Manufacturing and Maintenance: A Survey of Open-Access Papers

## Basic Information

- **Authors:** Nils Hütten, Miguel Alves Gomes, Florian Hölken, Karlo Andricevic, Richard Meyes, Tobias Meisen
- **Year:** 2024
- **Journal:** Applied System Innovation
- **Type:** Survey / Review Paper
- **DOI:** 10.3390/asi7010011

## Problem Statement

Industrial quality assessment is often performed through manual visual inspection.

Manual inspection can be:

- Error-prone
- Expensive
- Time-consuming
- Difficult to scale

Deep learning provides an opportunity to automate visual inspection, even in complex industrial environments.

## Objective

The objective of this paper is to investigate how deep learning is currently being used for automated visual inspection in:

- Manufacturing
- Maintenance

The paper also examines which modern deep learning approaches could improve existing industrial inspection systems.

## Methodology

The authors conducted a large-scale literature review of open-access research papers.

### Paper Selection Process

- Initial publications found: **6,583**
- After filtering for industrial relevance: **808**
- Final publications reviewed: **196**

The review focuses on:

- Manufacturing applications
- Maintenance applications
- Classification
- Object detection
- Segmentation
- Deep learning architectures
- Training methods
- Datasets
- Model performance

The review found:

- **31.7%** of the papers focused on manufacturing.
- **68.3%** focused on maintenance.

## Key Technologies Reviewed

The paper analyzes several deep learning approaches, including:

- CNNs
- ResNet
- EfficientNet
- YOLO
- Mask R-CNN
- UNet
- DeepLab
- Vision Transformers

The authors found that CNN-based models are currently the most commonly used approach.

However, Vision Transformers are emerging as a promising alternative.

## Dataset

Since this is a survey paper, it does not use one single dataset.

The reviewed papers use multiple industrial datasets.

Examples include:

- NEU Surface Defect Database
- SDNET 2018
- Road Damage Dataset
- Severstal Dataset
- Rail Surface Defect Dataset
- Magnetic Tile Surface Dataset

The survey found that the median dataset size was approximately **2,500 samples**.

## Results / Key Findings

The survey found that:

- CNNs are the most widely used models for automated visual inspection.
- Vision Transformers show strong potential but generally require more computational resources.
- **97%** of the reviewed papers use supervised learning.
- Many industrial datasets are relatively small.
- Small datasets make training deep learning models from scratch difficult.
- Self-supervised learning could be a promising future direction.
- There is an approximately **three-year gap** between new deep learning approaches appearing in academic research and their adoption in industrial visual inspection.

## Limitations / Challenges

The paper identifies several challenges:

- Limited dataset sizes
- Expensive data collection and annotation
- Heavy dependence on supervised learning
- Difficulty in comparing results between papers
- Limited reproducibility due to incomplete dataset information
- Computational requirements of advanced models
- A gap between academic research and real industrial deployment

The review itself focuses mainly on **2D image data**, which limits the discussion of 3D and other sensor-based inspection approaches.

## Research Gap

Future research should focus on:

- Self-supervised learning for industrial inspection
- Vision Transformers for automated visual inspection
- Better use of small industrial datasets
- 3D and multi-sensor inspection
- Reducing the gap between academic research and industrial deployment
- More standardized and reproducible dataset reporting

## Relevance to Inspectra

This paper is very useful for defining the overall direction of Inspectra.

It shows that most current industrial inspection systems depend heavily on supervised learning and CNN-based models.

For Inspectra, we can explore a system that considers:

Product Image
→ AI-Based Visual Analysis
→ Defect Detection / Localization
→ Quality Decision

The paper also highlights important areas we should consider while designing Inspectra:

- Dataset availability
- Model generalization
- Real-time performance
- Computational requirements
- Practical industrial deployment

The paper suggests that future automated inspection systems should move toward more flexible and scalable approaches rather than depending only on large, fully labeled datasets.
