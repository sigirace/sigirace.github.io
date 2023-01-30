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

☀️ **Manifold란?**<br>Manifold는 training DB 자체의 고차원 데이터를 공간에 뿌렸을때, 데이터를 error 없이 잘 아우르는 subspace를 의미한다. 이러한 subspace를 잘 찾는 것이 manifold learning이 되고, 이를 projection 시키면 차원이 축소된다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_22.png?raw=true" width="650" height="400"></p>

Manifold는 원 데이터의 정보를 유지하며 차원을 잘 줄이고 싶은 것이 목적이다. 예를들어 100차원을 2차원으로 줄일 때, 뒤에 98 차원을 날려버리는 것은 좋은 방법이 아니다. Manifold는 데이터 차원축소의 관점에서 크게 4가지로 사용된다.

1. Data compression: 데이터를 압축해서 가지고 있다면 공간을 아낄 수 있음
2. Data visualization: 데이터를 시각화 할 필요가 있을 때 사용함
4. <mark style='background-color: #fff5b1'>Curse of dimensionality</mark>: 차원의 저주를 회피하기 위해
5. <mark style='background-color: #fff5b1'>Discovering most important features</mark>: 차원을 축소하여 정보를 잘 압축했다면 중요 정보만 보전되었을 것이니 주요 feature라고 생각

### 3.2 Objective

#### 3.2.1 Data compression

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_23.png?raw=true" width="650" height="400"></p>

Autoencoder(AE)를 사용하여 데이터를 압축하였을 때, 기존의 JPEG 방식보다 좋은 성능을 보였음을 증명하는 논문이다. Bit rate는 압축하였을 때의 파일 사이즈이고, PSNR은 복원후의 화질(품질)을 의미한다.

#### 3.2.2 Data visualization

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_24.png?raw=true" width="650" height="400"></p>

t-SNE는 가장 고전적인 방법 중 하나이며, 예시는 28*28 차원의 이미지 데이터를 3차원으로 표현한 것이다. visualization의 목적은 데이터 혹은 머신러닝 결과에 대해 직관을 얻는 것이다.

#### 3.2.3 Curse of dimensionality

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_25.png?raw=true" width="650" height="400"></p>

📍 **예시**

> Training DB에 sample data가 8개 들어있으며, 각 sample의 범위는 0~10 그리고 sample 하나가 1이라는 공간 하나를 차지한다고 가정한다. 만약 이를 1차원 공간에서 다루게 되면 10이라는 공간 중에 80%는 값이 있는 것이나, 2차원 공간에서 다룰시에는 100이라는 공간 중 8%의 정보만을 가지고 있다. 이렇듯 공간의 차원이 늘어남에 따라 정보의 밀도가 급격하게 줄어드는 것(=차원이 늘어날 수록 많은 데이터가 필요함)을 차원의 저주라고 한다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_26.png?raw=true" width="650" height="400"></p>

👀 **Manifold learning의 가정**

```
Training DB에 있는 데이터를 공간상에 나타냈을 때, 이를 잘 표현하는 subspace가 있을 것이다. 
```

위 그림에서 롤처럼 표시된 공간은 전체 공간에 대한 subspace이고, 이는 원래 공간보다 저차원일 것이다. 따라서 가정과 같이 데이터를 잘 나타내는 subspace(=manifold)를 잘 찾을 수 있다면, 데이터의 압축 혹은 저차원으로의 변경이 효과적일 것이다. 이러한 manifold를 찾는 것이 manifold learning이라고 한다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_27.png?raw=true" width="650" height="400"></p>

위의 가정이 올바른 것인지에 대한 이미지를 통해 직관적으로 설명한다. 200 * 200 RGB의 차원의 공간은 수치적으로 10^96329개의 이미지를 표현할 수 있다. 만약 manifold 가정과 반대로 모든 이미지들이 골고루 잘 분포되어 있다면 (=데이터가 잘 표현되는 subspace가 없다면) 샘플링시에 우리가 볼법한 이미지들이 추출될 것이다. 하지만 결과는 위와같은 noise들만 샘플링 됨을 확인할 수 있다. 이는 manifold learning의 가정처럼 데이터들이 일정 공간에 몰려 있음을 의미한다.

📍 **예시**

> 200*200 RGB 공간에서 사람의 얼굴은 표현 가능하며 이들은 일정 공간에 몰려있을 것이다. 마찬가지로 스케치로 그린 얼굴은 그들의 공간에 몰려있으나 사람의 얼굴과 조금 떨어져 있을 것이다. 더하여 폰트, 글씨 등도 해당 공간에서 표현가능하나 이들은 앞선 그림들과는 전혀 다른 공간에 몰려있을 것이다.

Manifold를 잘 찾았다는 것은 유사한 이미지간의 관계성을 잘 찾았다는 것이다. 더하여 확률분포들 또한 잘 찾았다면 샘플링시 기존 training DB에 없는 것들이 나타나게 된다.

#### 3.2.4 Discovering most important features

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_28.png?raw=true" width="650" height="400"></p>

☀️ **MNIST**<br>28*28 차원의 데이터들이 분포되어 있는 것들을 잘 아우르는 2차원 subspace(=manifold)를 잘 찾았다면 각 숫자 두개가 어떤 dominent한 feature일 것이다. 

1:07:11







https://kh-mo.github.io/notation/2019/03/10/manifold_learning/
