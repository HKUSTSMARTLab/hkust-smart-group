---
title: One paper was accepted in Medical Image Analysis
date: 2023-05-09T09:39:10.598Z
summary: |-
  <!--StartFragment-->

  Good News! We have one paper accepted in Medical Image Analysis.

  <!--EndFragment-->
draft: false
featured: false
image:
  filename: 8.png
  focal_point: Smart
  preview_only: false
---
## [Dual-distribution discrepancy with self-supervised refinement for anomaly detection in medical images](https://www.sciencedirect.com/science/article/pii/S1361841523000555)

Medical anomaly detection is a crucial yet challenging task aimed at recognizing abnormal images to assist in diagnosis. Due to the high-cost annotations of abnormal images, most methods utilize only known normal images during training and identify samples deviating from the normal profile as anomalies in the testing phase. Many readily available unlabeled images containing anomalies are thus ignored in the training phase, restricting the performance. To solve this problem, we introduce one-class semi-supervised learning (OC-SSL) to utilize known normal and unlabeled images for training, and propose Dual-distribution Discrepancy for Anomaly Detection (DDAD) based on this setting. Ensembles of reconstruction networks are designed to model the distribution of normal images and the distribution of both normal and unlabeled images, deriving the normative distribution module (NDM) and unknown distribution module (UDM). Subsequently, the intra-discrepancy of NDM and inter-discrepancy between the two modules are designed as anomaly scores. Furthermore, we propose a new perspective on self-supervised learning, which is designed to refine the anomaly scores rather than directly detect anomalies. Five medical datasets, including chest X-rays, brain MRIs and retinal fundus images, are organized as benchmarks for evaluation. Experiments on these benchmarks comprehensively compare a wide range of anomaly detection methods and demonstrate that our method achieves significant gains and outperforms the state-of-the-art.