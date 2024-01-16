---
layout: single
title:  'Discrete distribution (1) Bernoulli distribution'
toc: true
categories: [Probability Distribution]
tags: [Discrete, Bernoulli]
---

여러 분포들에 대한 소개
{: .notice}

## 1. Definition

> 베르누이 시행을 거쳐 나온 결과에 대한 확률 분포

📍**베르누이 시행**

- 두 가지 결과가 있는 단일 시행
- ex) 동전 던지기 -> {앞, 뒤}

## 2. PMF

$$
P(X=x)=p^x(1−p)^{(1−x)}=
\begin{cases}
p \quad\quad (x=1)\\
1-p\;(x=0)\;
\end{cases}
$$

- p: 성공 확률
- x: 관측된 결과

## 3. Theta

$$
X 	\sim Bern(p)
$$

- p: 성공 확률

## 4. Summary statistics

- Expectation: $p$
- Variance: $p(1-p)$

## 5. Visualization

````python
import numpy as np
import matplotlib.pyplot as plt

# 베르누이 분포를 시각화하는 함수
def plot_bernoulli_distribution(p):
    # 베르누이 확률 질량 함수 (PMF)
    bernoulli_pmf = [1-p, p]

    # 결과를 나타내는 라벨
    labels = ['Failure (0)', 'Success (1)']

    # 그래프 생성
    plt.bar(labels, bernoulli_pmf, color=['red', 'blue'])
    plt.ylim(0, 1)
    plt.title(f'Bernoulli Distribution (p = {p})')
    plt.ylabel('Probability')
    plt.show()

# 여러 성공 확률에 대한 베르누이 분포 시각화
for p in [0.2]:
    plot_bernoulli_distribution(p)
````

  <p align="center"><img src="https://github.com/sigirace/page-images/blob/main/statistics/distributions/b1.png?raw=true" width="600" height="400"></p>
