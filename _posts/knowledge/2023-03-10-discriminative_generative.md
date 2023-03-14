---
layout: single
title:  'Discriminative vs Generative'
toc: true
categories: [Knowledge]
tags: [Discriminative, Generative]

---

본 게시물은 discriminative model과 generative model에 대해 [해당 포스트](https://ratsgo.github.io/generative%20model/2017/12/17/compare/)를 읽고 정리하는 글이다.
{: .notice}

### 1. Discriminative model

> 데이터 X가 주어졌을 때, 레이블 Y가 나타날 조건부 확률 p(Y/X)를 직접적으로 반환하는 모델

여기서 주요하게 볼 부분은 데이터가 주어졌을 때, 그에 대한 레이블 Y가 모델에 주어져 학습이 이루어진다는 것이다. 즉, 지도학습의 범주에 속하며 데이터 X에 대한 레이블 Y를 잘 구분하는 결정경계를 학습하는 것이 목표가 된다. discriminative model은 generative model에 비해 가정이 단순하고, 데이터의 양이 충분하다면 좋은 성능을 내는 것으로 알려져 있다. 선형회귀와 로지스틱 회귀가 대표적인 예시이다.



### 2. Generative model

> 데이터 X가 생성되는 과정을 두개의 확률모형 p(Y), p(X/Y)로 정의하고, 베이즈룰을 사용해 p(Y/X)를 간접적으로 도출하는 모델

해당 모델의 특징은 레이블 Y에 대한 정보가 있어도, 없어도 구축할 수 있다는 것이다. 전자는 지도학습 기반의 generative model이라 하며, 선혈판별분석이 대표적이고, 후자를 비지도학습 기반의 generative model이라 하며 가우시안믹스처모델, 토픽모델링이 대표적인 사례이다. 또한, generative model은 distribution을 학습하는 것을 목표로 하며, 베이지안 추론과 마찬가지로 학습데이터가 많을수록 discriminative model과 비슷한 성능을 가지는 경향이 있다.아울러 generative model은 p(X/Y)를 정의하기 때문에 이를 활용해 X를 샘플링 할 수 있다.



### 📍Distribution learning



데이터 분포를 학습하는 것에 대한 예시는 다음과 같다. 우리가 가진 데이터가 사람 얼굴 이미지(3x64x64)라고 가정하고, 이러한 벡터를 어떠한 기준 x로 나열한다면 아래와 같은 데이터 분포가 나타날 것이다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/knowledge/dis_vs_gen/dis_gen_1.png?raw=true" width="400" height="200"></p>

이때 만약 우리의 데이터 셋에 동양인 이미지가 많이 포함되었다면, 검은색 머리색을 가진 사진이 데이터셋에서 등장할 확률이 높아질 것이다. 즉, 가장 높은 확률값을 나타내는 Pdata(x3)에 해당하는 x3의 지점에서 데이터를 추출한다면 검은색 머리색을 가진 사진이 나올 확률이 높을 것이다. 반면 Pdata(x4)는 금색이라던가, 다른 인종의 머리색을 가진 사진이 나올 확률이 높을 것이다.

generative model의 목적 중 하나는 데이터의 분포를 학슴하는 것라고 하였다. 이는 모델에 데이터를 넣으면 실제 데이터의 확률에 가까운 값을 반환하는 것과 동일하다. 이를 도식화한 그림은 아래와 같다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/knowledge/dis_vs_gen/dis_gen_2.png?raw=true" width="400" height="200"></p>

### 3. Difference

아래 그림은 discriminative model과 generative model 간의 차이를 직관적으로 나타낸 것이다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/knowledge/dis_vs_gen/dis_gen_4.png?raw=true" width="400" height="200"></p>

### 👀 요약

1. generative model은 사후확률을 간접적으로, disciriminative model은 직접적으로 도출한다.
2. generative model은 데이터 분포를, disciriminative model은 결정경계를 학습한다.
