---
layout: single
title:  'Continuous distribution (2) Exponential Distribution'
toc: true
categories: [Probability Distribution]
tags: [Continuous, Exponential]

---

여러 분포들에 대한 소개
{: .notice}

## 1. Definition

> 사건이 서로 독립적일 때, 일정 시간 동안 발생하는 사건의 횟수가 포아송 분포를 따른다면 다음 사건이 일어날 때 까지의 대기 시간 t의 확률분포

- 기대값 $\lambda$가 주어져야 함

## 2. PDF

{% raw %}
$$
f(x; \lambda) = \begin{cases} \lambda e^{-\lambda x} \ (\text{where} x \geq 0) \\ 0 \;\;\;\;\;\;\;\; (\text{where} x \lt 0) \end{cases}
$$

{% endraw %}

- $\lambda$: 단위 시간 동안 발생하는 사건의 횟수 (=기대값)

## 3. Theta

$$
X \sim \text{Exp}(\lambda)
$$

- $\lambda$: 단위 시간 동안 발생하는 사건의 횟수 (=기대값)

## 4. Summary Statistics

- Expectation: $\frac {1} {\lambda}$
- Variance: $\frac {1} {\lambda^2}$

## 5. Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

# 람다 값 설정
lambdas = [0.5, 1, 1.5, 2]

x = np.linspace(0, 3, 1000)

# 각 람다에 대한 PDF 계산 및 그래프 그리기
for lam in lambdas:
    pdf = lam * np.exp(-lam * x)
    plt.plot(x, pdf, label=f'λ = {lam}')

plt.title('Probability Density Function of Exponential Distributions')
plt.xlabel('x')
plt.ylabel('PDF')
plt.legend()
plt.show()
```

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/statistics/distributions/ep1.png?raw=true" width="600" height="400"></p>

- lambda는 y축에 표시됨
- lambda가 클수록 기울기가 가파름 ☞ 사건이 빨리 발생할 확률이 높음

<br>

📍**PDF & CDF**

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

lambda_param = 1.0
x = np.linspace(0, 10, 1000)

pdf = expon.pdf(x, scale=1/lambda_param)
cdf = expon.cdf(x, scale=1/lambda_param)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(x, pdf, 'r-', label=f'PDF (lambda={lambda_param})')
plt.title('Probability Density Function of Exponential Distribution')
plt.xlabel('x')
plt.ylabel('Density')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x, cdf, 'b-', label=f'CDF (lambda={lambda_param})')
plt.title('Cumulative Distribution Function of Exponential Distribution')
plt.xlabel('x')
plt.ylabel('Probability')
plt.legend()

plt.tight_layout()
plt.show()
```

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/statistics/distributions/ep2.png?raw=true" width="1000" height="400"></p>

<br>

📍**지수분포와 포아송분포의 관계**

- Poisson Distribution: 단위 시간에서 평균 횟수가 $\lambda$일 때, 사건의 발생 횟수 x에 대한 분포

$$
f(x) = \frac {e^{-\lambda} \lambda^x} {x!}
$$

- 단위 시간을 t로 확장 ☞ 단위 시간에서 평균 $\lambda$이므로 t로 확장시 기대값은 $\lambda t$

$$
f(x) = \frac {e^{-\lambda t} {\lambda t}^x} {x!}
$$

✏️ **x = 0 일 경우**

<br>
$$
f(0) = e^{-\lambda t}
$$

- 단위 시간 t에서 사건이 일어나지 않을 확률
- 즉, 사건 발생까지의 대기시간이 단위 시간인 t보다 클 확률과 같음

✏️ **여사건 표현**

<br>
$$
1 - f(0) = 1 - e^{-\lambda t}
$$

- 단위 시간 t 동안 사건이 1회라도 일어날 확률
- 즉, 사건 발생까지의 대기시간이 단위 시간인 t보다 작을 확률과 같음
- 이는 지수함수의 정의를 통해 CDF로 해석 될 수 있음

$$
P(0 \leq x \leq t) = 1 - e^{-\lambda t}
$$

- PDF를 구하기 위해서 미분 수행

$$
g(t) = \frac {d} {dt} (1 - e^{-\lambda t}) = \lambda e^{-\lambda t}
$$

☀️ **정리**

- 포아송 분포의 사건 발생 확률을 통해 CDF를 유도하였고, 이를 미분하여 지수함수의 PDF 도출

