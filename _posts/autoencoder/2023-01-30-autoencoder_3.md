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
4. <mark style='background-color: #f6f8fa'>Curse of dimensionality</mark>: 차원의 저주를 회피하기 위해
5. <mark style='background-color: #f6f8fa'>Discovering most important features</mark>: 차원을 축소하여 정보를 잘 압축했다면 중요 정보만 보전되었을 것이니 주요 feature라고 생각

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

28*28(=784) 차원의 손글씨 이미지들을(=MNIST) 잘 아우르는 2차원 subspace(=manifold)가 있다고 가정하면, 각 축은 어떤 domimant한 feature일 것이다. Manifold를 잘 찾았다면 feature 또한 잘 찾은 것이라고 볼 수 있다. 이때의 feature는 unsupervised learning이기 때문에 자동으로 찾아진다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_29.png?raw=true" width="650" height="400"></p>

왼쪽 그림의 고차원 공간에서 manifold를 찾고 오른쪽 그림의 저차원으로 차원축소를 하였을 때, 같은 distance metric이라도 결과가 달라짐을 볼 수 있다. 이때 거리가 가깝다는 의미는 각 차원마다 달라지게 되는데, 원본인 고차원 공간에서는 단순히 데이터 공간상에서 가깝다는 의미이다. 반면 저차원의 manifold에서는 dominant한 feature들이 가깝다고 볼 수 있다.

📍 **예시**

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_30.png?raw=true" width="650" height="400"></p>

- 1번과 3번그림의 데이터 공간상의 중간 지점은 2번 그림의 위치이나 이는 의미상 가운데가 아님
- 의미가 없는(손이 두개, 잔상) 이유는 manifold에서 벗어났기 때문

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_31.png?raw=true" width="650" height="400"></p>

- manifold에서 중간의 위치에 있다면 의미적으로 중간에 있음을 알 수 있음

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_32.png?raw=true" width="650" height="400"></p>

Feature를 잘 찾는 다는 것을 다르게 표현하면 Entangled(섞여있음) / Disentangled(안섞여있음)로 표현한다. 만약 MNIST 데이터를 2D로 압축했다면, 가장 dominant한 feature는 숫자가 다른 것이다. 만약 학습이 잘 되었다면 manifold를 visualize 했을 때, 명확히 구분(=Disentangled)되어야 한다.

### 3.3 Dim Reduction

#### 3.3.1 Texanomy

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_33.png?raw=true" width="650" height="400"></p>

#### 3.3.2 PCA

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_34.png?raw=true" width="650" height="400"></p>

PCA는 원 데이터를 sample공간에 뿌리고, project시에 분산이 최대가 되는 plane을 찾는 것이다. Projection에 대한 수식을 보면 원래 데이터 sample에다가 평균을 뺀다. 이는 covariance matrix를 eigenvalue decomposition하기 때문이다. W는 eigenvalue 큰 element로 eigenvector를 찾아 원하는 차원 수 만큼 큰 순서대로 뽑아 W matrix 구성하여 projection하면 차원이 축소된다. 이러한 수식은 DNN과 유사한데, Autoencoder가 PCA를 포함하는 방법론이기 때문이다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_35.png?raw=true" width="650" height="400"></p>

PCA는 linear hyperplane에 projection 하기 때문에 왼쪽 상단과 같이 꼬여있는 데이터 분포에 대해서는 entangled 되어있음을 볼 수 있다. 이러한 데이터 분포는 Non-linear 차원축소 방식을 사용하면 disentangled 될 수 있다.

#### 3.3.3 Isomap & LLE

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_36.png?raw=true" width="650" height="400"></p>

Isomap과 LLE의 첫번째 step은 주변의 data를 clustering 하는 과정에서 시작한다. 그 이유는 데이터 공간상에서 가까우면 manifold 상에서도 가까울 것이라고 가정하기 때문이다.

### 3.4 Density Estimation

Autoencoder는 density estimaiton임을 앞장에서 확인하였다.

#### 3.4.1 Parzen Winodws

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_37.png?raw=true" width="650" height="400"></p>

1:15:54





















[의미를 보존하는 공간, manifold](https://kh-mo.github.io/notation/2019/03/10/manifold_learning/)

[PCA & eigenvector & eigenvalue](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=jinp7&logNo=221312142481)

[PCA 강필성](https://www.youtube.com/watch?v=bEX6WPMiLvo&list=PLetSlH8YjIfWMdw9AuLR5ybkVvGcoG2EW&index=4)

[Kernel/Kernel trick(커널과 커널트릭)](https://sanghyu.tistory.com/14)

https://jayhey.github.io/novelty%20detection/2017/11/02/Novelty_detection_Gaussian/

https://jayhey.github.io/novelty%20detection/2017/11/03/Novelty_detection_MOG/

https://jayhey.github.io/novelty%20detection/2017/11/08/Novelty_detection_Kernel/

[밀도추정](https://blog.mathpresso.com/mathpresso-%EB%A8%B8%EC%8B%A0-%EB%9F%AC%EB%8B%9D-%EC%8A%A4%ED%84%B0%EB%94%94-14-%EB%B0%80%EB%8F%84-%EC%B6%94%EC%A0%95-density-estimation-38fd7ef729bb)

[커널밀도추정](https://seongkyun.github.io/study/2019/02/03/KDE/)

