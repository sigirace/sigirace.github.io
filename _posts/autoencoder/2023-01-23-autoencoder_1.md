---
layout: single
title:  'Autoencoder의 모든것의 모든것 1'
toc: true
categories: Autoencoder
tags: [Autoencoder]


---

본 게시물은 이활석님의 [강의](https://www.youtube.com/watch?v=o_peo6U7IRM&t=4)를 보고 정리하는 글이다.
{: .notice}

## 1. Introduction

### 1.1 Autoencoder

  <p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_0.png?raw=true" width="300"></p>

```
An autoencoder is a type of artificial neural network used to learn efficient codings of unlabeled data (unsupervised learning). The encoding is validated and refined by attempting to regenerate the input from the encoding. The autoencoder learns a representation (encoding) for a set of data, typically for dimensionality reduction, by training the network to ignore insignificant data (“noise”). 
```

<center>출처: https://en.wikipedia.org/wiki/Autoencoder</center>

autoencoder는 레이블이 없는 데이터의 효율적인 코딩을 학습(=unsupervised learning)하는 데 사용되는 인공 신경망의 한 유형이다. 인코딩으로부터 Input을 재생성하려는 시도를 통해 인코딩은 검증되고 정제된다. 일반적으로 autoencoder는 차원축소를 위해 중요하지 않은 데이터(noise)를 무시하도록 훈련시킴으로써 데이터 셋에 대한 **representation**(인코딩)을 학습한다.

#### keywords

1. Unsupervised learning

2. Representation learning 

   = Efficient coding learning

3. **Dimensionality reduction**

4. Generative model learning

autoencoder의 중요한 task는 **Dimensionality reduction**이며 최근에는 Generative model learning으로도 사용하고 있다. 

### 1.2 Nonlinear dimensionality reduction(NLDR)

```
Nonlinear dimensionality reduction, also known as manifold learning, refers to various related techniques that aim to project high-dimensional data onto lower-dimensional latent manifolds, with the goal of either visualizing the data in the low-dimensional space, or learning the mapping (either from the high-dimensional space to the low-dimensional embedding or vice versa) itself. The techniques described below can be understood as generalizations of linear decomposition methods used for dimensionality reduction, such as singular value decomposition and principal component analysis.
```

<center>출처: https://en.wikipedia.org/wiki/Nonlinear_dimensionality_reduction</center>

Manifold learning으로 알려진 비선형 차원 축소는 고차원의 데이터를 낮은 차원의 잠재적인 mainfold들로 투영, 시각화 및 매핑을 학습하는 것을 목표로 한다. 이러한 기법은 svd 그리고 pca와 같이 차원 축소를 위한 linear decomposition의 일반화로 이해할 수 있다. (manifold의 정의는 이 [블로그](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=coniecual&logNo=221417921857)를 참조)

#### keywords

1. Unsupervised learning

2. Nonlinear Dimensionality reduction

   = Representation learning

   = Efficient coding learning

   = **Feature extraction**

   = **Manifold learning**

3. Generative model learning

### 1.3 Representation learning

  <p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_1.png?raw=true" width="400" height="270"></p>

<center>출처: http://videolectures.net/kdd2014_bengio_deep_learning/</center>

벤지오 교수님의 기술 분류표 상에서 autoencoder는 representation learning에 속한다고 한다. 

### 1.4 ML density estimation

  <p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_2.png?raw=true" width="400" height="270"></p>

<center>출처: http://www.iangoodfellow.com/slides/2016-12-04-NIPS.pdf</center>

이안 굳펠로우가 만든 분류표를 보면 Variational(variational autoencoder)이 Maximum Likelihood에 속함을 알 수 있다.

### 1.6 Summary

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_3.png?raw=true" width="600" height="350"></p>

입력과 출력이 동일한 값을 만드는 네트워크 구조를 가지고 있으면 autoencoder라 칭하는데, 이때 관계되는 키워드를 아래의 4개로 정리할 수 있다.

#### keywords

1. Unsupervised learning
2. Manifold learning
3. Generative model learning
4. ML density estimation

위 네가지 키워드가 어떻게 관계가 있는지 살펴보면, 먼저 autoencoder는 **1. unsupervised learning**으로 학습이 이루어지고 이때 loss를 최소화 하기 때문에 학습을 시키는 loss function에 대한 해석이 **4. Maximum Likelihood densiti estimation**과 관계있게 된다. 이렇게 학습한 autoencoder에서 입력 부분을 보면 차원 축소이기 때문에 **2. Manifold learning**, 출력 부분을 보면 생성 모델이기 때문에 **3. Generative model learning**의 개념과 관련이 있다.

## 2. Revisit Deep Neural Networks







https://junstar92.tistory.com/156
