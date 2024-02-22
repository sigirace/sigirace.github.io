---
layout: single
title:  'Continuous distribution (3) Gamma Distribution'
toc: true
categories: [Probability Distribution]
tags: [Continuous, Gamma]
---

여러 분포들에 대한 소개
{: .notice}

## 1. Definition

> 사건이 서로 독립적일 때, 단위 시간 동안 발생하는 사건의 횟수가 포아송 분포를 따르고, 이 사건들이 일어나기 까지의 총 대기 시간을 모델링하는 확률 분포

- 확률변수 X: 어떤 사건이 여러 번($\alpha$) 발생하는 데 걸리는 시간
- 형상 매개변수 $\alpha$와 $\beta$가 주어져야 함
  - $\alpha (k)$: 사건의 발생 횟수 (지수분포의 개수)
  - $\beta (\theta)$: 단위 시간당 사건의 발생 횟수

👀 definition

> If $X_1, ..., X_{\alpha}$ are independent random variables each having an exponential distribution with parameter $\beta$, then the random variable $X = X_1 + ... + X_{\beta}$ has a gamma distribution with parameter $\alpha$ and $\beta$.

- 감마분포는 지수분포의 합으로 나타낼 수 있음
- 사건들이 발생하는 데 걸리는 시간의 총 합




## 2. PDF

$$
f(x; \alpha, \beta) = \frac {\beta^\alpha} {\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x}, \;\; \text{for }x>0
$$

- $\alpha (k)$: 사건의 발생 횟수 (지수분포의 개수)
- $\beta (\theta)$: 단위 시간당 사건의 발생 횟수

📍 **감마함수**

{% raw %}
$$
\Gamma(\alpha) = \int^\infty_0 x^{\alpha -1} e^{-x}dx \\
\Gamma(1) = \int^\infty_0 e^{-x} dx = 1 \\
\Gamma(\alpha) = (\alpha -1) \Gamma(\alpha -1) \\
\Gamma(\alpha +1) = \alpha \Gamma(\alpha)
$$
{% endraw %}

- 감마함수는 factorial을 식수 및 복소수로 확장한 것

📍 **감마함수로부터 감마분포 유도**

{% raw %}
$$
\Gamma(\alpha) = \int^\infty_0 x^{\alpha -1} e^{-x}dx \\
$$
{% endraw %}

- 위 식에서 확률변수 X=x라 할 때, 구간 0에서 $\infty$ 까지의 적분은 1이 되어야 함
- 양변을 $\Gamma(\alpha)$로 나눔

{% raw %}
$$
1 =\int^\infty_0 \frac {1} {\Gamma(\alpha)}x^{\alpha -1} e^{-x}dx \\
f(x) = \frac {1} {\Gamma(\alpha)}x^{\alpha -1} e^{-x} \\
X \sim \text{Gamma}(\alpha, 1)
$$
{% endraw %}

- CDF에서 $f(x)$만을 나타낸 것

## 3. Theta

$$
X \sim \text{Gamma}(\alpha, \beta)
$$

- $\alpha (k)$: 사건의 발생 횟수 (지수분포의 개수), 형상 매개변수
- $\beta (\theta)$: 단위 시간당 사건의 발생 횟수, 척도 매개변수

## 4. Summary Statistics

- Expectation: $\frac {\alpha} {\lambda}$
- Variance: $\frac {\alpha} {\lambda^2}$

## 5. Visualization

````python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

# 형상 매개변수(alpha/k)와 척도 매개변수(beta/theta) 설정
alpha_values = [1, 2, 3, 5]  # 형상 모수
beta_values = [1, 2, 3, 5]  # 척도 모수 (여기서는 1/beta를 척도로 사용함)

x = np.linspace(0, 20, 1000)  # x 축 값 범위 설정

# 베타(척도 모수) 고정, 알파(형상 모수) 변화 시각화
plt.figure(figsize=(14, 6))
beta_fixed = 1  # 베타 고정
for alpha in alpha_values:
    y = gamma.pdf(x, a=alpha, scale=1/beta_fixed)
    plt.plot(x, y, label=f'α (k)={alpha}, β (θ)={beta_fixed}')
plt.title(f'Gamma Distribution with β (θ) Fixed at {beta_fixed}')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()

# 알파(형상 모수) 고정, 베타(척도 모수) 변화 시각화
plt.figure(figsize=(14, 6))
alpha_fixed = 2  # 알파 고정
for beta in beta_values:
    y = gamma.pdf(x, a=alpha_fixed, scale=1/beta)
    plt.plot(x, y, label=f'α (k)={alpha_fixed}, β (θ)={beta}')
plt.title(f'Gamma Distribution with α (k) Fixed at {alpha_fixed}')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/statistics/distributions/gam2.png?raw=true" width="600" height="500"></p>

- 형상 모수가 클 수록 분포가 완만해짐
- 사건의 수가 증가함에 따라, 해당 사건들이 발생하는 데 필요한 총 시간의 분포가 넓어짐
- 사건들이 발생하는 데 걸리는 총 시간이 길어질 확률이 높아진다는 것을 의미

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/statistics/distributions/gam1.png?raw=true" width="600" height="500"></p>

- 척도 모수가 클 수록 분포가 완만해짐
- 척도 모수가 크다 ☞ $\lambda$가 작다
- 단위 시간당 사건 발생 비율이 낮아짐을 의미하며, 결과적으로 사건이 발생하기까지의 시간이 길어질 확률이 높아짐

