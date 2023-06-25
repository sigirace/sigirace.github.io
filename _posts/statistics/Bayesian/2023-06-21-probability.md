---
layout: single
title:  'Probability Theory (3) Probability'
toc: true
categories: [Statistics]
tags: [Measure, Bayesian]

---

본 게시물은 최성준 교수님의 확률론 강의를 정리하는 글이다.
{: .notice}

## 1. Probability

👀 **Terminology**

1. Random Experiment: 불확실성을 내포하는 실험 또는 과정 ex) 주사위 던지기
2. outcomes: 실험에서 가능한 결과들 ex) 주사위 던지기 실험시 outcomes는 1, 2, 3, 4, 5, 6
3. sample point(w): 실험에서 하나의 결과를 나타내는 것 ex) 주사위를 던졌을 때 나오는 샘플 중 하나인 3
4. sample space(Ω): 실험에서 가능한 모든 결과의 집합 ex) 주사위 던지기 실험시 {1, 2, 3, 4, 5, 6}

📍 **Example**

  <p align="center"><img src="https://github.com/sigirace/page-images/blob/main/statistics/probability/p1.png?raw=true" width="600" height="300"></p>

- 주사위 던지기 실험에서 sample space는 {1, 2, 3, 4, 5, 6}으로 정의됨
- sample space에 대한 measure를 정의

☀️ **Conditions of a sample space**

outcomes들이 (*비공식적으로*) 아래 조건을 만족해야만 sample space(Ω)가 됨

1. mutually exclusive: sample point가 서로 독립
2. collectively exhaustive: outcomes가 실험의 모든 결과를 포함
3. 관심있는 것에 대해 세분화가 필요함 ex) 주사위 실험에서 홀수를 관심있게 본다면 {1,3,5}

👀 **Definition of Probability**

  <p align="center"><img src="https://github.com/sigirace/page-images/blob/main/statistics/probability/p2.png?raw=true" width="600" height="200"></p>

- 결국 확률은 sample space 위에서 정의된 set function

## 2. Probability Allocation Function

👀 **Definition**

> probability에 대한 aximos를 만족하는 특정 사건에 대한 probability

📍**pmf, pdf**

  <p align="center"><img src="https://github.com/sigirace/page-images/blob/main/statistics/probability/p3.png?raw=true" width="600" height="200"></p>

- Large P is set function: 어떤 사건(set)에 대한 확률
- small p is probability allocation function(paf)

## 3. Conditional Probability

👀 **Definition**

  <p align="center"><img src="https://github.com/sigirace/page-images/blob/main/statistics/probability/p4.png?raw=true" width="600" height="100"></p>

- conditional probability는 bayesian statistics로 형성됨

👀 **Bayes`s Rule**

  <p align="center"><img src="https://github.com/sigirace/page-images/blob/main/statistics/probability/p6.png?raw=true" width="600" height="100"></p>

☀️ **Chain rule**

  <p align="center"><img src="https://github.com/sigirace/page-images/blob/main/statistics/probability/p5.png?raw=true" width="600" height="300"></p>

☀️ **Likelihood, posterior, prior**

  <p align="center"><img src="https://github.com/sigirace/page-images/blob/main/statistics/probability/p7.png?raw=true" width="600" height="250"></p>

## 4. Independent

  <p align="center"><img src="https://github.com/sigirace/page-images/blob/main/statistics/probability/p8.png?raw=true" width="600" height="300"></p>
