---
layout: single
title:  'Continuous distribution (3) Gamma Distribution'
toc: true
categories: [Probability Distribution]
tags: [Discrete, Geometric]
---

여러 분포들에 대한 소개
{: .notice}

## 1. Definition

> 사건이 서로 독립적일 때, 단위 시간 동안 발생하는 사건의 횟수가 포아송 분포를 따르고, 이 사건들이 일어나기 까지의 총 대기 시간을 모델링하는 확률 분포

- 확률변수 X: 어떤 사건이 여러 번($\alpha$) 발생하는 데 걸리는 시간
- 형상 매개변수 $\alpha$와 $\beta$가 주어져야 함
  - $\alpha (k)$: 사건의 발생 횟수 (지수분포의 개수)
  - $\beta (\theta)$: 단위 시간당 사건의 발생 횟수

👀 def

> If $X_1, ..., X_{\alpha}$ are independent random variables each having an exponential distribution with parameter $\beta$, then the random variable $X = X_1 + ... + X_{\beta}$ has a gamma distribution with parameter $\alpha$ and $\beta$.




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

📍 **감마함수로부터 감마분포 유도**

{% raw %}
$$
\Gamma(\alpha) = \int^\infty_0 x^{\alpha -1} e^{-x}dx \\
$$
{% endraw %}

- 위 식에서 확률변수 X=x라 할 때, 구간 0에서 $\infity$ 까지의 적분은 1이 되어야 함
- 양변을 $\Gamma(\alpha)$로 나눔

{% raw %}
$$
1 =\int^\infty_0 \frac {1} {\Gamma(\alpha)}x^{\alpha -1} e^{-x}dx \\
f(x) = \frac {1} {\Gamma(\alpha)}x^{\alpha -1} e^{-x} \\
X \sim \text{Gamma}(\alpha, 1)
$$
{% endraw %}

- CDF에서 $f(x)$만을 나타낸 것

### 3. Theta

