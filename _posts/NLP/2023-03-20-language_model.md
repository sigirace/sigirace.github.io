---
layout: single
title:  '1. 언어모델이란?'
toc: true
categories: [Language Model]
tags: [LM]

---

언어모델의 첫번째 Chapter에서는 언어모델의 정의와 그 종류에 대해 알아보고, 이를 이해하는데 초점을 둔다.

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



## 2. 언어모델의 종류



다음으로는 언어모델의 종류에 대해 알아본다.



### 2.1 통계적 언어모델



전통적 언어 모델은 통계적으로 접근하는 방식을 사용하였다. 통계적 언어모델(Statistical Language Model)은 줄여서 SLM이라고도 한다.



#### 2.1.1 문장에 대한 확률



문장은 단어들의 연결로 이루어진다. 단어들의 연결은 문맥을 이루며, 뜬금없는 경우가 아니라면 어떤 단어들의 연결 뒤에는 특정 단어가 나올 확률이 높다. 따라서 문장의 확률은 어떤 단어의 나열이 주어졌을 때, 다음 단어가 나올 확률인 조건부 확률의 곱으로 구성된다.


$$
P(w_1, w_2, w_3, ... ,w_n) = \prod_{n=1}^{n}P(w_n|w1,...,w_{n-1})
$$


📍**Example**

> P(My dog is very cute) = P(My) * P(dog/My) * P(is/My dog) * P(very/My dog is) * P(cute/ My dog is very)



#### 2.1.2 카운트 기반의 접근

문장의 확률을 구하기 위해 다음 단어에 대한 예측 확률을 모두 곱하는 방식을 사용한다. 이때, 다음 단어에 대한 예측 확률은 카운트 기반 확률을 사용한다. 



📍**Example**

> 학습시키는 전체 데이터에서 My dog is very가 100번 등장했고, 그 다음 cute가 30번 등장했다면 My dog is very가 나왔을때, cute가 나올 확률 P(cute/ My dog is very)은 30%이다.



#### 2.1.3 희소문제

모델은 학습을 통해 전체 데이터의 확률 분포를 근사하는 특징을 가지고 있다. 동일하게 언어 모델은 코퍼스(=학습 데이터)를 통해 실생활에서 사용되는 언어의 확률 분포를 근사하려고 한다. 하지만 언어 모델을 만들기 위해 카운트 기반의 확률을 사용한다면, 언어 모델을 현실에 근사시키기 어려운 문제에 마주치게 된다. 만약 My dog is very very cute라는 문장을 예측한다면 수식은 아래와 같을 것이다.


$$
P(cute|\ My\ dog\ is\ very\ very) = \frac{P(My\ dog\ is\ very\ very\ cute)}{P(My\ dog\ is\ very\ very)}
$$


그런데 만약 구성된 코퍼스에 My dog is very very cute라는 단어 나열이 한번도 등장하지 않았다면, P(My dog is very very cute)의 확률은 0일 것이다. 또한 My dog is very very라는 단어의 나열이 한번도 등장하지 않았다면, 해당 문장의 확률은 정의 될 수 없다, 하지만 현실에서 해당 문장은 충분히 나올 수 있으며 심지어 빈번히 사용될 수 도 있다. 이처럼 코퍼스에 위와 같은 문장이 없는 이유로 언어 모델이 문장을 전혀 예측할 수 없는 문제를 희소문제라고 한다.

위 문제를 완화하는 방법으로 바로 이어서 배우게 되는 n-gram 언어 모델이나, 스무딩, 백오프 같은 일반화 기법이 존재한다. 하지만 어떤 기법을 사용하여도 희소문제라는 한계에 부딪혔으며 결국 통계적 언어 모델에서 인공 신경망 언어 모델로 트렌드가 바뀌게 된다.

### 2.2 N-gram 언어모델



### 2.3 신경망 언어모델





### 참조

https://wikidocs.net/21687

https://ratsgo.github.io/from%20frequency%20to%20semantics/2017/09/16/LM/

https://wikidocs.net/45609

