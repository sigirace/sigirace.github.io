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

> An autoencoder is a type of artificial neural network used to learn efficient codings of unlabeled data (unsupervised learning). The encoding is validated and refined by attempting to regenerate the input from the encoding. The autoencoder learns a representation (encoding) for a set of data, typically for dimensionality reduction, by training the network to ignore insignificant data (“noise”). 

<center>출처: https://en.wikipedia.org/wiki/Autoencoder</center><br>

autoencoder는 레이블이 없는 데이터의 효율적인 코딩을 학습(=unsupervised learning)하는 데 사용되는 인공 신경망의 한 유형이다. 인코딩으로부터 Input을 재생성하려는 시도를 통해 인코딩은 검증되고 정제된다. 일반적으로 autoencoder는 차원축소를 위해 중요하지 않은 데이터(noise)를 무시하도록 훈련시킴으로써 데이터 셋에 대한 **representation**(인코딩)을 학습한다.

```markdown
[keywords]
1. Unsupervised learning
2. Representation learning
   = Efficient coding learning
3. Dimensionality reduction
4. Generative model learning
```

autoencoder의 중요한 task는 **Dimensionality reduction**이며 최근에는 Generative model learning으로도 사용하고 있다. 

### 1.2 Nonlinear dimensionality reduction(NLDR)

> Nonlinear dimensionality reduction, also known as manifold learning, refers to various related techniques that aim to project high-dimensional data onto lower-dimensional latent manifolds, with the goal of either visualizing the data in the low-dimensional space, or learning the mapping (either from the high-dimensional space to the low-dimensional embedding or vice versa) itself. The techniques described below can be understood as generalizations of linear decomposition methods used for dimensionality reduction, such as singular value decomposition and principal component analysis.

<center>출처: https://en.wikipedia.org/wiki/Nonlinear_dimensionality_reduction</center><br>



Manifold learning으로 알려진 비선형 차원 축소는 고차원의 데이터를 낮은 차원의 잠재적인 mainfold들로 투영, 시각화 및 매핑을 학습하는 것을 목표로 한다. 이러한 기법은 svd 그리고 pca와 같이 차원 축소를 위한 linear decomposition의 일반화로 이해할 수 있다. (manifold의 정의는 이 [블로그](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=coniecual&logNo=221417921857)를 참조)

```markdown
[keywords]
1. Unsupervised learning
2. Nonlinear Dimensionality reduction
   = Representation learning
   = Efficient coding learning
   = Feature extraction
   = Manifold learning
3. Generative model learning
```

### 1.3 Representation learning

  <p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_1.png?raw=true" width="400" height="270"></p>

<center>출처: http://videolectures.net/kdd2014_bengio_deep_learning/</center><br>

벤지오 교수님의 기술 분류표 상에서 autoencoder는 representation learning에 속한다고 한다. 



### 1.4 ML density estimation

  <p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_2.png?raw=true" width="400" height="270"></p>

<center>출처: http://www.iangoodfellow.com/slides/2016-12-04-NIPS.pdf</center><br>

이안 굳펠로우가 만든 분류표를 보면 Variational(variational autoencoder)이 Maximum Likelihood에 속함을 알 수 있다.



### 1.6 Summary

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_3.png?raw=true" width="600" height="350"></p>

입력과 출력이 동일한 값을 만드는 네트워크 구조를 가지고 있으면 autoencoder라 칭하는데, 이때 관계되는 키워드를 아래의 4개로 정리할 수 있다.

```markdown
[keywords]
1. Unsupervised learning
2. Manifold learning
3. Generative model learning
4. ML density estimation
```

위 네가지 키워드가 어떻게 관계가 있는지 살펴보면, 먼저 autoencoder는 **1. unsupervised learning**으로 학습이 이루어지고 이때 loss를 최소화 하기 때문에 학습을 시키는 loss function에 대한 해석이 **4. Maximum Likelihood densiti estimation**과 관계있게 된다. 이렇게 학습한 autoencoder에서 입력 부분을 보면 차원 축소이기 때문에 **2. Manifold learning**, 출력 부분을 보면 생성 모델이기 때문에 **3. Generative model learning**의 개념과 관련이 있다.



## 2. Revisit Deep Neural Networks

### 2.1 Classic Machine Learning

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_4.png?raw=true" width="600" height="350"></p>

전통적인 머신러닝의 접근방식은 데이터에서 추상화된 정보를 뽑는 것이다. 이를 위해 먼저 데이터를 모은다. 다음으로 문제를 해결할 모델을 정의하고, 모델의 파라미터를 설정한다. 이후 모델에서 나온 정보와 실제 정보의 다른 정도를 계산(measure)하는 loss function을 정의한다. 학습단계에서는 모델을 규정짓는 파라미터를 바꿔가며 앞서 수집한 training data들에 대해 로스가 최소가 되는 파라미터를 찾는다. 마지막으로 test data에 대해 정보 값을 추정한다. 이 과정에서 주요하게 볼 부분은 입력이 고정되면 출력 또한 고정된다는 것이다.

### 2.2 Deep Neural Networks

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_5.png?raw=true" width="600" height="350"></p>

데이터를 모으는 부분은 고전적 머신러닝과 동일하다. 모델을 정의하는 부분은 역시나 문제에 맞는 딥러닝 모델들을 사용한다. 이때 학습해야 할 파라미터는 주로 네트워크를 구성하는 weight와 bias이다. 이후 loss function을 정의하는 부분에서 딥러닝은 backpropagation으로 인한 제약조건이 생긴다. 이는 backpropagation에 대한 아래 두 가지의 가정 때문이다.

```
1. 전체 training data의 loss는 sample data로 부터 나온 loss의 합과 같다.
    ☞ sample loss의 곱/ 나누기 등등으로 하는 경우는 가정하지 않는다.
2. loss에 들어가는 파라미터는 네트워크의 마지막 출력과 실제 정보 뿐이다.
    ☞ 네트워크 중간의 출력 값으로 계산하는 경우는 가정하지 않는다.
```

이로인해 딥러닝에서 사용하는 loss function은 MSE와 Cross Entropy 뿐이다. 

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_6.png?raw=true" width="600" height="350"></p>

training data 전체의 loss를 최소화 시키는 파라미터를 찾는 학습 방식은 대부분 optimal problem을 찾는 가장 간단한 방식인 gradient descent을 사용한다. 이는 step by step으로 점차 정답에 가까워지는 iterative method이다. 이러한 방식을 위해서는 아래의 질문에 대한 정의가 필요하다.

```
1. 현재 파라미터에서 어떻게 update 할 것인가
    ☞ loss가 줄어들기만 하면 update
2. 언제 파라미터 update를 stop 할 것인가
    ☞ loss가 더 이상 줄어들지 않으면 stop
```

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_7.png?raw=true" width="600" height="350"></p>

파라미터를 바꿔 loss를 줄이는 것은 알겠으나 파라미터의 차원은 네트워크가 깊어질수록 커지게 된다. 이때 gradient descent 방식으로 파라미터를 조정한다면 각각을 얼마만큼 바꿔줘야 하는지에 대한 문제에 마주친다. 이에 대한 해답은 다음과 같다.

#### [Taylor expansion](https://darkpgmr.tistory.com/59)

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_7_1.png?raw=true" width="400" height="150"></p>

테일러 급수 또는 테일러 전개는 어떤 미지의 함수 f(x)를 근사 다항 함수로 표현하는 것이다. 이를 gradient descent에 적용하면 x를 $\theta$













https://junstar92.tistory.com/156
