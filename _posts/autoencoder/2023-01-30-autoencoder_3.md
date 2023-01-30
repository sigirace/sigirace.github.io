---
layout: single
title:  'Autoencoder의 모든것의 모든것 (3) Manifold Learning'
toc: true
categories: Autoencoder
tags: [Autoencoder, Deep Learning, MLE, MSE, Cross Entropy]

---

본 게시물은 이활석님의 [강의](https://www.youtube.com/watch?v=o_peo6U7IRM&t=4)를 보고 정리하는 글이다.
{: .notice}

<div class="notice">
<li><a href="https://sigirace.github.io/autoencoder/autoencoder_1/">Autoencoder의 모든것의 모든것 (1) 오토인코더란?</a></li>
<li><a href="https://sigirace.github.io/autoencoder/autoencoder_2/">Autoencoder의 모든것의 모든것 (2) Maximum Likelihood 관점의 Deep Learning</a></li>
</div>


## 3. Manifold Learning

### 3.1 Introduction

**Manifold란?**<br>Manifold는 training DB 자체의 고차원 데이터를 공간에 뿌렸을때, 데이터를 error 없이 잘 아우르는 subspace를 의미한다. 이러한 subspace를 잘 찾는 것이 manifold learning이 되고, 이를 projection 시키면 차원이 축소된다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_22.png?raw=true" width="650" height="400"></p>

Manifold는 원 데이터의 정보를 유지하며 차원을 **잘** 줄이고 싶은 것이 목적이다. 예를들어 100차원을 2차원으로 줄일 때, 뒤에 98 차원을 날려버리는 것은 좋은 방법이 아니다. Manifold는 데이터 차원축소의 관점에서 크게 4가지로 사용된다.

1. Data compression: 데이터를 압축해서 가지고 있다면 공간을 아낄 수 있음
2. Data visualization: 데이터를 시각화 할 필요가 있을 때 사용함
3. **Curse of dimensionality**: 차원의 저주를 회피하기 위해
4. **Discovering most important features**: 차원을 축소하여 정보를 잘 압축했다면 중요 정보만 보전되었을 것이니 주요 feature라고 생각

### 3.2 Objective

#### 3.2.1 Data compression

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_23.png?raw=true" width="650" height="400"></p>

Autoencoder(AE)를 사용하여 데이터를 압축하였을 때, 기존의 JPEG 방식보다 좋은 성능을 보였음을 증명하는 논문이다. Bit rate는 압축하였을 때의 파일 사이즈이고, PSNR은 복원후의 화질(품질)을 의미한다.

#### 3.2.2 Data visualization

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_24.png?raw=true" width="650" height="400"></p>

t-SNE는 가장 고전적인 방법 중 하나이며, 예시는 28*28의 이미지 데이터를 3차원으로 표현한 것이다. visualization의 목적은 데이터 혹은 머신러닝 결과에 대해 직관을 얻는 것이다.

















