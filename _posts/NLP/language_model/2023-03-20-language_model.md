---
layout: single
title:  'LM(1) 언어모델이란?'
toc: true
categories: [Language Model]
tags: []

---

언어모델의 첫번째 Chapter에서는 언어모델의 정의와 그 종류에 대해 알아보고, 이를 이해하는데 초점을 둔다.
{: .notice}

## 1. 언어모델(Language Model)

### 1.1 언어모델의 정의

👀 **Definition 1**

````
언어 모델은 주어진 단어들을 보고 다음 단어의 확률을 할당하는 것이다.
````



즉, 어떤 parameter로 이루어진 모델과 단어의 나열(=sequence)이 있을 때, 다음에 올 단어를 예측하는 것이다. 이를 수학적으로 표현하면 아래와 같다.


$$
P(w_n | w_1, ... ,w_{n-1};\theta)
$$


👀 **Definition2**

````
언어 모델은 단어 시퀀스에 대한 확률분포를 가르킨다.
````

또한, 언어 모델은 n개의 단어로 이루어진 sequence가 있을 때, m개의 단어로 이루어진 sequence가 나타날 확률을 할당한다. 이에 대한 예시는 아래와 같다.

📍 **Example**

> P(Today is Wednesday) = 0.01<br>P(Today Wendnesday is) = 0.0001

위 두 정의는 word, sequence의 차이만 있을 뿐, 확률을 할당한다는 공통점이 있다. 확률을 사용한다는 것은 context-dependent 즉, 우리가 모델을 학습시키는 데이터에 의존적이게 된다. 따라서 domain 혹은 task에 따라 전혀 다른 모델이 구성된다.

### 1.2 언어 모델의 종류

언어모델에는 통계적 방식을 사용한 방식과 신경망을 사용한 방식이 있다. 다음 포스트를 통해 두 방식에 대한 차이를 알아보고 더 나아가 언어모델이 발전한 흐름에 대해 알아보도록 한다.

### 참조

https://wikidocs.net/21687

https://ratsgo.github.io/from%20frequency%20to%20semantics/2017/09/16/LM/

