---
layout: single
title:  'Discrete distribution (1) Bernoulli Distribution'
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
X \sim Bern(p)
$$

- p: 성공 확률

## 4. Summary statistics

- Expectation: $p$
- Variance: $p(1-p)$

## 5. Visualization

````python
import numpy as np
import matplotlib.pyplot as plt

def plot_bernoulli_distribution(p):
    bernoulli_pmf = [1-p, p]

    labels = ['Failure (0)', 'Success (1)']

    plt.bar(labels, bernoulli_pmf, color=['red', 'blue'])
    plt.ylim(0, 1)
    plt.title(f'Bernoulli Distribution (p = {p})')
    plt.ylabel('Probability')
    plt.show()

for p in [0.2]:
    plot_bernoulli_distribution(p)
````

  <p align="center"><img src="https://github.com/sigirace/page-images/blob/main/statistics/distributions/b1.png?raw=true" width="600" height="400"></p>
