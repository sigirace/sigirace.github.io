---
layout: single
title:  'Continuous distribution (1) Normal Distribution'
toc: true
categories: [Probability Distribution]
tags: [Discrete, Geometric]
---

여러 분포들에 대한 소개
{: .notice}

## 1. Definition

> 평균과 표준편차를 매개변수로 하여, 이를 중심으로 대칭적인 종 모양의 연속 확률 분포

<br>

📍**특징**

- 오류 분포를 포함한 여러 자연 현상을 직접 모델링하기 위한 확률분포

- 중심극한정리로 이용하며 단순하고 정확한 근사 가능

<br>

## 2. PDF



- $\mu$: 평균

- $\sigma^2$: 분산

<br>

## 3. Theta

$$
X \sim N(\mu, \sigma^2)
$$

- $\mu$: 평균

- $\sigma^2$: 분산

<br>

## 4. Summary Statistics

- Expectation: $\mu$
- Variance: $\sigma^2$

<br>

## 5. Visualization

```python
import math
from matplotlib import pyplot as plt

def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu)**2 / 2 / sigma**2) / (sqrt_two_pi * sigma))
xs = [x / 10.0 for x in range(-50,50)]

plt.plot(xs,[normal_pdf(x,sigma=1) for x in xs],'-',label='mu=0,sigma=1')
plt.plot(xs,[normal_pdf(x,sigma=2) for x in xs],'--',label='mu=0,sigma=2')
plt.plot(xs,[normal_pdf(x,sigma=0.5) for x in xs],':',label='mu=0,sigma=0.5')
plt.plot(xs,[normal_pdf(x,mu=-1) for x in xs],'-.',label='mu=-1,sigma=1')
plt.legend()
plt.title('Various Normal pdfs')
plt.show()
```

[normal1]

## 6. Standard Normal Distribution

> 정규분포에서 평균을 0으로 분산을 1로 설정하여 표준화를 수행한 분포

<br>

📍 **PDF**

<br>

📍**Transform**

$$

$$

<br>

📍**Calculate Probability**

- 확률 분포가 정규분포인 경우 표준정규분포로 치환하여 특정 범위의 확률을 쉽계 계산 할 수 있음
