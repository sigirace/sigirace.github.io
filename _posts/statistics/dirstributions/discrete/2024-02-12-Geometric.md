---
layout: single
title:  'Discrete distribution (3) Geometric Distribution'
toc: true
categories: [Probability Distribution]
tags: [Discrete, Geometric]
---

여러 분포들에 대한 소개
{: .notice}

## 1. Definition

> 베르누이 시행에서 처음 성공까지 시도한 횟수 X의 확률 분포

## 2. PMF

$$
f_x(x) = p(1-p)^{x-1}
$$

- p: 성공 확률
- x: 성공까지 총 독립시행 횟수

📍**CDF**

$$
P(X \leq k) = 1-(1-p)^{k}
$$

- X의 횟수 제한이 없기 때문에 몇번 이하 등을 사용해 CDF 계산을 많이 함

## 3. Theta

$$
X \sim \text{Geo}(p)
$$

- p: 성공 확률

## 4. Summary statistics

- Expectation: $\frac{1}{p}$
- Variance: $\frac{1-p}{p^2}$

📍 **Expectation vs Variacne**

- 기하분포에서 평균은 첫 번째 성공이 나타나기까지의 평균 시행 횟수
- 기하분포에서 분산은 첫 번째 성공이 나타나기까지의 시행 횟수의 변동성
- 변동성이기 때문에 평균에서 얼마나 벗어날 수 있는지 대략적으로 파악 할 뿐 수치적으로 보장하지 않음

📍 **Example**

> 피파온라인에서 금카 강화 성공 확률은 7%이다. 이때, 10번 이하의 시도로 강화를 성공할 확률은?

$$
P(X \leq 10) = \sum_{x=1}^{10}P(X=x) \\
= \sum_{x=1}^{10}[(0.07)\cdot(0.93)^{x-1}] \\
= 0.07 \cdot \sum_{x=1}^{10}(0.93)^{x-1} \\
= 0.07 \cdot (\frac{(0.93)^0 \cdot (1-0.93^{10})}{1-0.93}) \\
= 0.516
$$

- 약 51.6%의 확률로 10번 이내에 성공할 수 있음
- 그러나 변동이 약 189로 매우 큼

## 5. Visualization

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom

def plot_geometric_distribution(p):
    x = np.arange(1, 21)  # Consider the first 20 trials
    geometric_pmf = geom.pmf(x, p)

    plt.bar(x, geometric_pmf, color='orange')
    plt.title(f'Geometric Distribution (p = {p})')
    plt.xlabel('Number of Trials until First Success')
    plt.ylabel('Probability')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

p = 0.1
plot_geometric_distribution(p)
```

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/statistics/distributions/geo1.png?raw=true" width="600" height="400"></p>

- 지수 분포와 유사함
