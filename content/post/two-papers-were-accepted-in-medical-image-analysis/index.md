---
title: Two papers were accepted in Medical Image Analysis
subtitle: ""
date: 2022-11-11T03:34:19.810Z
lastmod: 2022-11-11T03:34:19.810Z
summary: |-
  <!--StartFragment-->

  Good News! We have two papers accepted in Medical Image Analysis.

  <!--EndFragment-->
draft: false
featured: false
image:
  filename: 1-s2.0-s1361841522003012-main.png
  focal_point: Smart
  preview_only: false
---
## [Deep semi-supervised multiple instance learning with self-correction for DME classification from OCT images](https://www.sciencedirect.com/science/article/pii/S1361841522003012)

Supervised deep learning has achieved prominent success in various diabetic macular edema (DME) recognition tasks from optical coherence tomography (OCT) volumetric images. A common problematic issue that frequently occurs in this field is the shortage of labeled data due to the expensive fine-grained annotations, which increases substantial difficulty in accurate analysis by supervised learning. The morphological changes in the retina caused by DME might be distributed sparsely in B-scan images of the OCT volume, and OCT data is often coarsely labeled at the volume level. Hence, the DME identification task can be formulated as a multiple instance classification problem that could be addressed by multiple instance learning (MIL) techniques. Nevertheless, none of previous studies utilize unlabeled data simultaneously to promote the classification accuracy, which is particularly significant for a high quality of analysis at the minimum annotation cost. To this end, we present a novel deep semi-supervised multiple instance learning framework to explore the feasibility of leveraging a small amount of coarsely labeled data and a large amount of unlabeled data to tackle this problem. Specifically, we come up with several modules to further improve the performance according to the availability and granularity of their labels. To warm up the training, we propagate the bag labels to the corresponding instances as the supervision of training, and propose a self-correction strategy to handle the label noise in the positive bags. This strategy is based on confidence-based pseudo-labeling with consistency regularization. The model uses its prediction to generate the pseudo-label for each weakly augmented input only if it is highly confident about the prediction, which is subsequently used to supervise the same input in a strongly augmented version. This learning scheme is also applicable to unlabeled data. To enhance the discrimination capability of the model, we introduce the Student-Teacher architecture and impose consistency constraints between two models. For demonstration, the proposed approach was evaluated on two large-scale DME OCT image datasets. Extensive results indicate that the proposed method improves DME classification with the incorporation of unlabeled data and outperforms competing MIL methods significantly, which confirm the feasibility of deep semi-supervised multiple instance learning at a low annotation cost.

![](2202.05126.png)

## [Deep Learning for Computational Cytology: A Survey](https://arxiv.org/pdf/2202.05126.pdf)

Computational cytology is a critical, rapid-developing, yet challenging topic in the field of medical image computing which analyzes the digitized cytology image by computeraided technologies for cancer screening. Recently, an increasing number of deep learning (DL) algorithms have made significant progress in medical image analysis, leading to the boosting publications of cytological studies. To investigate the advanced methods and comprehensive applications, we survey more than 120 publications of DL-based cytology image analysis in this article. We first introduce various deep learning methods, including fully supervised, weakly supervised, unsupervised, and transfer learning. Then, we systematically summarize the public datasets, evaluation metrics, versatile cytology image analysis applications including classification, detection, segmentation, and other related tasks. Finally, we discuss current challenges and potential research directions of computational cytology.