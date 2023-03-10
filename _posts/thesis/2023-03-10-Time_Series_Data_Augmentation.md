---
layout: single
title:  'Time Series Data Augmentation for Neural Networks by Time Warping with a Discriminative Teacher'
toc: true
categories: [Thesis]
tags: [Data Augmentation, Timeseires]

---

본 게시물은 시계열 데이터의 증강법에 대해 [해당 논문](https://paperswithcode.com/paper/time-series-data-augmentation-for-neural)을 읽고 정리하는 글이다.
{: .notice}

## 0. Abstract

Neural networks는 패턴 인식에서 강력한 도구가 되었으며 이는 large dataset의 일반화 덕분이다. 하지만 다른 도메인들과 달리 시계열 분류 데이터 세트는 대부분 스케일이 작다. 이 문제를 해결하기 위해, 해당 논문은 guided warping이라고 불리는 데이터 증강법을 제안한다. 많은 데이터 증강 방법이 random한 변환에 기초를 두고 있는 반면, guided warping은 Dynamic Time Warping의 요소의 정렬 특성과 그 모양을 활용하여 결정적인 샘플의 패턴을 warping 한다.

### 📌 Warping?

> warping의 사전적 의미는 휘어지게 하다, 왜곡하다라는 뜻을 가지고 있다. 이미지, 영상에서의 warping은 x축, y축, 회전 scale 등을 이용하여, 보정이나 찌그러진 이미지를 정규화 하기 위한 처리 기법을 의미한다.

이러한 방식으로, time series는 기준이 되는 패턴의 시간 단계와 일치하도록 샘플 패턴을 warping하여 혼합되어 구성된다. 더하여, 본 논문은 guided warping에 대한 직접적인 참조자 역할을 제공하기 위해 discriminative teacher를 소개한다. 마지막으로 CNN과 RNN을 사용하여 2015년 UCR UCR 시계열 아카이브의 85개 데이터 세트 모두에 대한 방법을 평가한다. 구현된 코드는 [여기]( https://github.com/uchidalab/time )에서 찾을 수 있다.

### 📌 discriminative teacher?

> Data에 대한 Label을 통해 학습시킨다는 의미로, [해당 포스트](https://sigirace.github.io/knowledge/discriminative_generative/)를 통해 discriminative의 의미를 확인 할 수 있다.



## 1. Introduction

데이터의 양을 늘리면 일반화에 도움이 되고, 결과적으로 많은 기계 학습 모델의 정확성에 도움이 된다는 것은 잘 알려져 있다. 그러나 이미지 도메인과 달리 시계열 데이터 세트는 비교적 작은 데이터셋을 구성하는 경향이 있다. 예를 들어, 가장 많이



In fact, it is well-known that increasing the amount ofdata helps with generalization and, in turn, the accuracy ofmany machine learning models [5]–[7].However, unlike the image domain, time series datasets tendto be tiny in comparison.

For example, one of the most usedsources of time series classification datasets, the University ofCalifornia Riverside (UCR) Time Series Archive [8], contains85 time series datasets but only 10 have more than 1,000training samples and the largest, ElectricDevices, only has8,926.

By comparison, the popular image datasets, ImageNetLarge Scale Visual Recognition Challenge (ILSVRC) [9],MNIST [10], and CIFAR [11], have 1.2 million, 60,000, and50,000 training patterns respectively.

Thus, in order to use thefull potential of modern machine learning methods, there is aneed for time series classification data.



실제로, 데이터의 양을 늘리면 일반화에 도움이 되고, 결과적으로 많은 기계 학습 모델[5]–[7]의 정확성에 도움이 된다는 것은 잘 알려져 있다.그러나 이미지 도메인과 달리 시계열 데이터 세트는 비교적 작은 경향이 있다.

예를 들어, 가장 많이 사용되는 시계열 분류 데이터 세트의 소스 중 하나인 캘리포니아 대학교 리버사이드(UCR) 시계열 아카이브[8]는 85개의 시계열 데이터 세트를 포함하고 있지만 1,000개 이상의 교육 샘플을 보유한 것은 10개뿐이고 가장 큰 Electric Devices는 8,926개만 있다.

이에 비해 인기 있는 이미지 데이터 세트인 ImageNet Large Scale Visual Recognition Challenge(ILSVRC)[9], MNIST[10] 및 CIFAR[11]는 각각 120만, 60,000, 50,000개의 훈련 패턴을 가지고 있다.

따라서 현대 기계 학습 방법의 잠재력을 최대한 활용하기 위해서는 시계열 분류 데이터가 필요하다.
