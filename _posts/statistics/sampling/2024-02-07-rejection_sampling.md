---
layout: single
title:  'Sampling (3) Rejection Sampling이 뭐야?'
toc: true
categories: [Statistics]
tags: [Rejection Sampling, PDF, CDF, Uniform Distribution]

---



## 1. Rejection Sampling

### 1.1 Definition

> Rejection Sampling은 target 분포의 PDF는 알고 있으나, 이를 수학적으로 계산하여 직접 샘플링 하는 것이 매우 어렵거나 불가능할 때 효율적으로 샘플링하기 위해 사용되는 방법이다.

- target 확률 분포 f(x)의 확률 밀도 함수를 알고 있어야 함

### 1.2 Method

Rejection Sampling을 수행하기 위한 준비물은 아래 3가지이다.

- Target density f(x): 목표 확률 분포
- Proposal density g(x): 제안 분포
- Envelope function e(x): 덮개 함수





$$
f(x) = 0.3 \cdot e^{-0.2 x^2} + 0.7 \cdot e^{-0.2(x - 10)^2}
$$
