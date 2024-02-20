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

{% raw %}
$$
f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right), \quad (-\infty \leq x \leq \infty)
$$
{% endraw %}

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

