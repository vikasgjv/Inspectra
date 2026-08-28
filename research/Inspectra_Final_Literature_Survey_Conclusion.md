# Inspectra — Literature Survey, Comparison & Final Conclusion

---

## 1. Main Problem

Manual quality inspection in manufacturing is slow, inconsistent, and dependent on human expertise. Because of this, manufacturers reject **3–5% of products** due to defects that are only discovered late in the process — after time and resources have already been spent on them.

**Inspectra aims to solve this by using AI and computer vision to automatically detect surface defects, dimensional errors, and assembly faults in real time on the production line**, catching problems earlier instead of at final inspection.

---

## 2. What Existing Papers Have Done

Across the 10 reviewed papers, research clusters around eight common approaches:

| Approach | What it means | Papers |
|---|---|---|
| **CNN / Deep Learning** | CNNs (ResNet, EfficientNet, MobileNetV2, DenseNet) are the standard backbone for extracting visual defect features | 01, 02, 04, 05, 07, 09 |
| **Computer Vision Pipelines** | Multi-stage systems combining preprocessing, localization, and classification instead of one single model | 02, 04, 07 |
| **Anomaly Detection** | Detecting "abnormal" products by comparing them to learned normal patterns rather than classifying against fixed defect labels | 03, 06, 10 |
| **Supervised Learning** | Training on labeled defect/no-defect images — still the dominant method industry-wide (~97% of reviewed systems) | 01, 02, 04, 05, 07, 09 |
| **Unsupervised / Self-Supervised Learning** | Training mainly on normal samples, useful when defect examples are rare | 06, 10 |
| **RGB Image Inspection** | The default and most common input type across nearly all papers | 01–09 |
| **3D / Multimodal Inspection** | Combining RGB with depth or point-cloud data to capture structural/dimensional information RGB alone misses | 10 |
| **Real-Time Defect Detection** | Designing pipelines specifically to meet production-line speed requirements (e.g., 5.2 ms/image) | 04, 09 |

**Overall pattern:** most existing research uses CNN-based supervised learning on RGB images for classification, detection, or segmentation, with a smaller but growing body of work exploring anomaly detection, self-supervised learning, and multimodal (RGB+3D) inputs to address the shortage of labeled defect data.

---

## 3. Common Limitations

The following limitations appear repeatedly across the reviewed papers:

- **Need for many labeled defect images** — supervised methods dominate, but defective samples are naturally rare on a working production line (Papers 01, 05, 09)
- **Difficulty detecting small/subtle defects** — especially in high-resolution images where defects occupy only a few pixels (Papers 01, 04, 10)
- **Poor generalization to new products** — models trained on one product or dataset often fail to transfer to new variants, components, or environments (Papers 01, 02, 08, 10)
- **High computational requirements** — particularly for Vision Transformers and 3D/multimodal processing of large point clouds (Papers 05, 09, 10)
- **Difficulty with real-time deployment** — many proposed methods are not evaluated for production-line speed, or require multiple slow iterative training cycles (Papers 03, 06, 07, 08)
- **Sensitivity to lighting/image quality and environmental noise** — complex industrial environments (lighting changes, camera angle, surface variation) reduce detection accuracy (Papers 04, 10)
- **Research-to-industry gap** — a 2–3 year lag exists between new techniques appearing in research and being adopted in real inspection systems (Papers 05, 09)

---

## 4. Research Gap

**What problem is still not completely solved that Inspectra can address?**

Existing systems achieve high accuracy, but almost always within a narrow, controlled scope — a specific product, a specific dataset, or a specific defect type they were trained on (e.g., Paper 02's PCB system hit 100% accuracy but only on six boards of one design; Paper 04's semiconductor pipeline is built specifically around wafer geometry; Paper 08 explicitly studies this generalization failure with gearbox components).

At the same time, the most flexible techniques that don't depend on large labeled datasets — unsupervised/anomaly-based detection (Papers 06, 10) — are still maturing and haven't yet been combined with the real-time, multistage efficiency shown in the supervised pipelines (Papers 02, 04).

**The gap:** *A practical inspection system that can (a) work with limited/imperfect defect data, (b) generalize across different products and defect types rather than being locked to one, and (c) still run in real time on a production line* is not fully addressed by any single paper reviewed. Most papers solve one or two of these three requirements, not all three together.

This is exactly the space Inspectra can occupy.

---

## 5. What Inspectra Will Do

Inspectra's proposed pipeline:

```
Product Image
      ↓
Image Preprocessing
      ↓
AI / Computer Vision Analysis
      ↓
Defect or Anomaly Detection
      ↓
Defect Classification / Localization
      ↓
Inspection Result
```

- **Image Preprocessing** — normalize/localize the region of interest before analysis, following the multistage localize-then-classify approach shown in Paper 04.
- **AI / Computer Vision Analysis** — a CNN-based backbone processes the image, informed by the consistent evidence across Papers 01, 02, 05, and 09.
- **Defect or Anomaly Detection** — combine supervised classification where labeled data exists with anomaly scoring (trained mainly on normal samples) for rare or unseen defect types, following Papers 06 and 10.
- **Classification / Localization** — output whether a product is defective, and where the defect is (bounding box or segmented region), reusing the classification/detection/segmentation taxonomy common to Papers 01, 05, and 09.
- **Inspection Result** — a final pass/reject/flag decision usable directly on the line.

---

## 6. Final Approach

- **Approach:** RGB image-based defect and anomaly detection using deep learning, structured as a staged pipeline (localize → analyze → decide) rather than one end-to-end model.
- **Starting model/technique:** A CNN backbone (e.g., MobileNetV2 or ResNet) for classification/detection, paired with an anomaly-scoring component for defects with little or no labeled data.
- **Why this choice:**
  - CNNs are the most consistently validated, production-proven approach across nearly every paper reviewed (01, 02, 04, 05, 07, 09) — Vision Transformers, while promising, aren't yet the safer choice for real-time, resource-constrained deployment (05, 09).
  - The staged/localize-first pipeline is the only approach in the review with hard real-time numbers behind it — Paper 04 achieved 99.5% F1 at ~5.2 ms/image, and Paper 02's staged segmentation → feature extraction → classification pipeline hit 100% accuracy.
  - Starting with **supervised learning where labeled data is available, backed by anomaly detection where it isn't**, directly targets the research gap identified above: it lets Inspectra work with limited defect samples (Paper 06's iterative refinement, Paper 10's normal-sample-only training) instead of being blocked on collecting thousands of labeled defect images.
- **Dataset:** Start with a proprietary RGB image dataset of the target product(s) in both good and defective condition (following the format used in Papers 02 and 08), split for training/testing, and where possible structured to include product/defect variants — deliberately testing generalization, since that's the specific weakness Papers 01, 02, 08, and 10 flag.
- **Learning type:** A hybrid: **supervised learning** for known, labeled defect categories, **unsupervised/anomaly-based learning** for detecting unknown or rare defects — rather than committing to one or the other exclusively.
- **Evaluation:** Standard industrial inspection metrics used across the reviewed papers — **accuracy, precision, recall, F1-score**, and **AUROC** for anomaly detection (as used in Paper 06) — plus real-time processing time per image (ms) to confirm the system meets production-line speed requirements, and separate generalization testing on held-out product variants to directly measure the gap Inspectra is meant to close.

---

## 7. Expected Outcome

Inspectra should deliver an automated industrial visual inspection system capable of analyzing product images and identifying possible surface defects, dimensional errors, and assembly faults in real time — reducing reliance on manual inspection, catching defects earlier in the production process, and improving overall quality control. Unlike many of the systems reviewed, Inspectra should also be designed with generalization and limited-data operation in mind from the start, rather than being tied to a single product or a large labeled dataset.

---

## Summary  

1. **What is the problem?** Manual inspection is slow, inconsistent, and catches defects too late — Inspectra automates this with computer vision.
2. **What have other researchers done?** Mostly CNN-based supervised classification/detection/segmentation on RGB images, with a growing shift toward anomaly detection, self-supervised learning, and multimodal (RGB+3D) inspection.
3. **What approaches work well?** Staged pipelines (localize → classify) achieve the best combination of accuracy and real-time speed (Papers 02, 04).
4. **What limitations exist?** Heavy reliance on labeled data, poor generalization across products, high compute needs, real-time deployment difficulty, and sensitivity to environmental conditions.
5. **What is the research gap?** No reviewed system combines real-time performance, limited-data operation, and cross-product generalization all at once.
6. **What will Inspectra do differently/practically?** Build a staged CNN pipeline that pairs supervised classification with anomaly detection, explicitly evaluated for generalization across products, not just accuracy on one dataset.
7. **Which approach/model will we choose and why?** CNN-based staged pipeline (starting with MobileNetV2/ResNet) with anomaly scoring — because it's the most production-proven, real-time-capable approach across the review, and it directly targets the identified data-scarcity and generalization gap.
8. **What result do we expect?** A working real-time visual inspection system that detects surface, dimensional, and assembly defects, reduces manual inspection effort, and generalizes better than existing narrowly-scoped systems.
