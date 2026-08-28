# A Dataset and Baseline for Deep Learning-Based Visual Quality Inspection in Remanufacturing

## Basic Information

- **Authors:** Johannes C. Bauer, Paul Geng, Stephan Trattnig, Petr Dokládal, Rüdiger Daub
- **Year:** 2025
- **Conference:** 2025 IEEE 30th International Conference on Emerging Technologies and Factory Automation (ETFA)
- **Publisher:** IEEE
- **Type:** Conference Paper
- **Conference Date:** 09–12 September 2025
- **Conference Location:** Porto, Portugal
- **DOI:** 10.1109/ETFA65518.2025.11205777
- **Paper Link:** https://ieeexplore.ieee.org/document/11205777

## Problem Statement

Remanufacturing involves restoring worn products to a like-new condition. A key step in this process is the quality inspection of disassembled components.

Currently, many inspection tasks are performed manually because of:

- High variety of components
- Different product variants
- Different defect patterns
- Dependence on expert knowledge

Deep learning can help automate visual inspection, but existing models often struggle to generalize to:

- New product variants
- Unseen components
- Different defect patterns

## Objective

The objective of this paper is to develop a dataset and baseline evaluation framework for deep learning-based visual quality inspection in remanufacturing.

The authors also aim to improve the generalization ability of classification models when they encounter previously unseen types of components.

## Methodology

The paper proposes a new image dataset containing typical gearbox components from two automotive transmissions.

The components are captured in:

- Good condition
- Defective condition

The authors create different train-test splits to generate distribution shifts.

This allows them to evaluate how well deep learning models generalize when the test data contains different types of components from the training data.

The paper also proposes a:

**Contrastive Regularization Loss**

This additional loss function is designed to improve the robustness and generalization ability of the classification model.

## Dataset

The proposed dataset contains images of:

- Typical gearbox components
- Components from two automotive transmissions
- Good-condition components
- Defective-condition components

The dataset is specifically designed to evaluate the generalization ability of visual quality inspection models under different distribution shifts.

The provided information does not specify the exact number of images or defect categories.

## Results

The authors evaluated different deep learning models using the proposed dataset.

The results demonstrate that the proposed **contrastive regularization loss** improves the model's ability to generalize to unseen types of components.

This is important because industrial inspection systems often need to work with product variants or components that were not fully represented during training.

The provided abstract does not include exact numerical performance values.

## Key Advantages

- Introduces a dataset specifically designed for remanufacturing quality inspection.
- Includes both good and defective components.
- Evaluates generalization under different distribution shifts.
- Addresses the challenge of unseen component types.
- Proposes contrastive regularization to improve model robustness.
- Focuses on a practical industrial inspection problem.

## Limitations / Challenges

Based on the available paper information, some challenges include:

- The dataset focuses on gearbox components from two automotive transmissions.
- Generalization to completely different industries or product categories is not established.
- Exact dataset size and detailed performance metrics are not available in the provided information.
- Real-world remanufacturing environments may contain a wider variety of components and defect types.

## Research Gap

Many deep learning-based inspection systems perform well when training and testing data come from similar distributions.

However, in real manufacturing and remanufacturing environments, systems may encounter:

- New product variants
- Unseen components
- Different defect patterns
- Distribution shifts

There is a need for visual inspection systems that can maintain good performance even when the test data differs from the training data.

## Relevance to Inspectra

This paper is highly relevant to Inspectra because one of the major challenges for our project is ensuring that an AI inspection system can generalize beyond the exact products and defect examples used during training.

The key idea from this paper can be represented as:

Product Image
→ Deep Learning Model
→ Robust Feature Learning
→ Generalization to New Components
→ Defect / Quality Classification

The concept of **contrastive learning and robustness to unseen components** could be useful for Inspectra when designing a system that can work with different product types instead of being limited to one specific product.
