---
layout: single
title:  'Sampling (3) Rejection Sampling이 뭐야?'
toc: true
categories: [Sampling]
tags: [Rejection Sampling, PDF, CDF, Uniform Distribution]

---

본 게시물은 공돌이의 수학정리노트의 [Rejection Sampling]([Rejection Sampling - 공돌이의 수학정리노트 (Angelo's Math Notes)](https://angeloyeo.github.io/2020/09/16/rejection_sampling.html))을 참고하여 작성하였다.
{: .notice}

## 1 Definition

> Rejection Sampling은 target 분포의 PDF는 알고 있으나, 이를 수학적으로 계산하여 직접 샘플링 하는 것이 매우 어렵거나 불가능할 때 효율적으로 샘플링하기 위해 사용되는 방법이다.

- target 확률 분포 f(x)의 확률 밀도 함수(=pdf)를 알고 있어야 함

## 2 Requirements

Rejection Sampling을 수행하기 위한 준비물은 아래 3가지이다.

- Target distribution: 목표 확률 분포는 sampling의 target
- Proposal distribution: 제안 분포는 쉽게 샘플을 추출할 수 있는 분포 (ex. uniform distribution)
- Envelope function: 덮개 함수는 제안 분포를 상수배한 것으로 목표 확률 분포를 모두 포함함

## 3 Example

- Target distribution $f(x)$가 아래와 같다고 가정

$$
f(x) = 0.3 \cdot e^{-0.2 x^2} + 0.7 \cdot e^{-0.2(x - 10)^2}


$$

- Proposal distribution $g(x)$는 unifrom distiribution으로 설정

- Proposal distribution에 상수배를 취해, envelope distribution이 target distribution을 모두 포함할 수 있도록 함

📍 **Note1: Target distribution**

- 주어진 target distribution은 실제 $(-\infty, \infty)$ 의 구간에서 적분시 전체 면적이 1이 아니기에 확률 밀도라고 보긴 어려움

- 그러나 sample을 추출하기 어려운 분포라는 뜻으로 사용함

- CDF및 CDF의 역함수를 구하기 힘들기에 inverse cdf 방식도 어려움

📍**Note2: Proposal distribution**

- Target distribution과 유사한 형태의 제안 분포를 설정하는 것이 좋음

- 그러나 uniform distribution을 사용하는 것이 직관적으로 이해하기 쉬움

📍 **Visualization**

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

def target_distribution(x):
    return 0.3 * np.exp(-0.2 * x**2) + 0.7 * np.exp(-0.2 * (x - 10)**2)

x = np.linspace(-10, 20, 1000)
target_pdf = target_distribution(x)

domain = [-7, 17]
proposal_pdf = uniform.pdf(x, loc=domain[0], scale=domain[1]-domain[0])

max_target = np.round(np.max(target_pdf),2)
max_proposal = np.round(np.max(proposal_pdf), 2)

enveloping_constant = max_target/ max_proposal
enveloping_function = proposal_pdf * enveloping_constant

# 시각화
plt.figure(figsize=(10, 6))
plt.plot(x, target_pdf, label='Target Distribution $f(x)$', linewidth=2)
plt.plot(x, proposal_pdf, label='Proposal Distribution (Uniform)', linestyle='--')
plt.plot(x, enveloping_function, label='Enveloping Function', linestyle='-.')
plt.xlabel('x')
plt.ylabel('Density')
plt.legend()
plt.show()
```

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/statistics/sampling/reject/r1.png?raw=true" width="600" height="300"></p>

## 4 Sampling

1. Proposal distribution $g(x)$에서 sample($x_0$)을 하나 추출

2. Target distribution $f(x)$와 envelope function $Mg(x)$의 함수 값을 비교
   
   - $f(x_0)/Mg(x)$ 연산을 수행

3. Domain이 $(0,1)$인 새로운 unifrom distiribution의 sample($y_0$)을 추출

4. $y_0$ 와 앞서 연산한 $f(x_0)/Mg(x_0)$을 비교

5. $y_0 \lt f(x_0)/Mg(x_0)$ 이면 $(x_0, y_0)$를 accpet, 아니면 reject

📍**Note: Likelihood**

- $f(x_0)/Mg(x)$의 범위는 $(0,1)$

- 이때, $f(x_0)$의 값이 클 수록 신규 uniform distribution에서 추출된 sample($y_0$)보다 높은 값을 가질 가능성이 올라감

- 즉, sample $(x_0)$가 target distribution의 분포에서 나왔을 likelihood가 높아짐

📍**Visualization**

```python
proposal_pdf_value = 1 / (domain[1] - domain[0])
accepted = []
rejected = []

def rejection_sampling():
    # 제안 분포에서 하나의 샘플 x0 추출
    x0 = uniform(low=domain[0], high=domain[1])

    # smaple x0에 대해 f(x0)와 Mg(x0)의 값 비교
    f_x0 = target_distribution(x0)
    Mg_x0 = enveloping_constant * proposal_pdf_value
    compare_value = f_x0/Mg_x0

    # 균일 분포에서 랜덤한 값 추출
    y_0 = uniform(low=0, high=1)

    # 기각 채택 여부 결정
    if y_0 < compare_value:
        accepted.append((x0, y_0))
    else:
        rejected.append((x0, y_0))

# sampling 1000번 수행
N = 1000
for i in range(0, N):
    rejection_sampling()

plt.plot([x[0] for x in accepted], [x[1] for x in accepted], 'go')  # Plot Accepted Points
plt.plot([x[0] for x in rejected], [x[1] for x in rejected], 'ro')  # Plot Rejected Points
plt.show()
```

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/statistics/sampling/reject/r2.png?raw=true" width="600" height="300"></p>

- Target distribution과 유사하게 sampling이 수행된 것을 알 수 있음

🏃 **Next Step**

- 다음으로는 Markov Chain Monte Carlo, MCMC sampling에 대해 알아보자
