---
layout: single
title:  'Probability Theory (4) Random Variable'
toc: true
categories: [Statistics]
tags: [Measure, Bayesian]


---

본 게시물은 최성준 교수님의 확률론 강의를 정리하는 글이다.
{: .notice}

### 👀 Definition

> random variable은 mesurable한 Ω(sample space) 위에서 정의된 real-valued function이다.

- **real-valued function**: sample space에 있는 원소를 다른 공간의 실수와 매핑시킴
- **mesurable**: sample space에 있는 원소들의 공간에 대해 면적을 구할 수 있음

☀️ **sample space vs sigma field**

- sample space는 실험에서 가능한 모든 결과의 집합 ex) 주사위 던지기 실험의 경우 sample space는 {1,2,3,4,5,6}
- sigma filed는 sample space의 부분 집합들로 구성된 집합, 사건(event)의 집합을 표현하기 위해 사용 ☞ 사건의 집합
- 즉, sigma filed는 sample space의 부분 집합을 다루기 위해 axioms 존재
- 확률은 sigma field 위에서 정의되며 sigma filed의 사건들에 대한 확률 값을 할당하며, 확률 실험의 결과를 수학적으로 다룰 수 있게 함

☀️ **probability space**

😗[Image1]

- **probability space**는 sample space, sigma field 그리고 확률 측도로 구성되어 있음
- 확률 측도는 sigma field의 각 사건에 대해 확률 값을 할당하는 함수

📍**Example**

😗[Image2]

- 실험은 주사위 던지기
- 실험에 대한 sample space는 {1,2,3,4,5,6}
- sigma field는 sample space의 power set
- radnom variable X에 대한 확률 계산: P(X<=10)은 sample space의 부분집합인 {1,2,4,6}에 대한 probabilty measure

random variables에 대한 추가적인 정리
{: .notice}

## 1. Random Variable

### 1.1 Definition

- random variable은 random experiment로 나타날 수 있는 모든 outcome(=sample space)에 대해 실수를 매핑하는 real-valued function
- 이때, 매핑하는 기준에 따라 같은 random experiment일지라도 다른 random variable이 정의됨

### 1.2 Range

- random varialbe이 가능한 실수의 집합의 범위

📍**Example**

> 동전을 5번 던지는 실험에서 random variable X는 동전의 앞면의 개수<br>이때의 sample space는 {TTTTT, TTTTH, TTTHH, ... , HHHHH}
> 
> X(TTTTT) = 0, X(TTHTT) = 1 ..
> 
> Range(X) = {0, 1, 2, 3, 4, 5}

## 2. Discrete Random Variables

### 2.1 Definition

- 셀 수 있는 range를 가진 random variable

## 3. PMF

### 3.1 Definition

> 확률 질량 함수(probability mass function, PMF)는 이산 확률 변수의 분포를 나타며, 특정 값에 대한 확률을 나타내는 함수이다.

$$
R_x=\{x_1, x_2, x_3, ...\}
$$

- random variable X의 value가 $x_1, x_2, x_3, ...$
- $\{X=x_k\}$일 사건(event) A는 sample space에 존재하는 outcome s로 만들어진 집합(=sigma field)
- 이처럼 discrete random variable에 대해 사건 A가 나타날 확률을 공식으로 표현한 것이 PMF

📍**Example**

> 동전을 두개 던지는 실험에서 관측된 앞면의 수를 random variable X라고 정의했을 때, PMF는 아래와 같이 정의할 수 있음
> 
> 1. sample space S 정의
> 
> $$
> S=\{HH, HT, TH, TT\}
> $$
> 
> 2. X의 range
> 
> $$
> R_x = \{0, 1, 2\}
> $$
> 
> 3. pmf 정의
> 
> $$
> P_x(0) = P(X=0)=P(\{TT\}) = \frac{1}{4} \\
P_x(1) = P(X=1)=P(\{HT, TH\}) = \frac{1}{2} \\ 
P_x(2) = P(X=2)=P(\{HH\}) = \frac{1}{4} \\
> $$

### 3.2 Probability Distribution

😗[image1]

- discrete random variable의 pmf를 probability distribution(=확률분포)라고도 함

### 3.3 Properties of PMF

😗[image2]

## 4. CDF

### 4.1 Definition

- probability distribution의 누적된 값
- PMF는 discrete random variable에서 사용할 수 있으나, CDF는 다양한 variable에서 사용 가능함

😗[image3]

📍**Example**

> PMF example에 대한 CDF

😗[image4]
