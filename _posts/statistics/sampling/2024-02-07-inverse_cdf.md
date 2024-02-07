---
layout: single
title:  'Sampling (2) Inverse CDF Sampling이 뭐야?'
toc: true
categories: [Statistics]
tags: [Inverse CDF Sampling, PDF, CDF, Uniform Distribution]

---



## 1. CDF

Inverse CDF sampling을 알아보기 전에 CDF의 성질에 대해 알아본다.

### 1.1 Definition

$$
F_X(x) = p[X \leq x]
$$

- 대문자 F는 CDF 함수의 이름을 나타냄
- 아래첨자 대문자 X는 확률변수
- 괄호 안의 argument 소문자 x는 X에 대입되는 실제 값
- 우변의 의미는 확률변수 X가 x보다 같거나 작은 값을 가질 확률

### 1.2 Properties

- 양의 무한대, 음의 무한대 값에서 CDF의 값은 각각 다음과 같음

$$
F_X(-\infty) = 0, F_X(\infty) = 1
$$

- 이는 확률의 합이 1이 된다는 사실로 부터 도출됨
- 따라서 CDF는 0 부터 1 사이의 값을 가질 수 있음



## 2. Inverse CDF Method

### 2.1 Method

CDF의 속성을 통해 알 수 있듯 어떤 확률 분포의 CDF는 확률 변수의 모든 가능한 값에 대해서 0~1 사이의 값을 도출한다. 이때, 동일하게 0~1 사이의 값을 가지는 uniform distribution의 sampling 결과를 사용하여 CDF의 역함수를 통해 목표 확률 분포에서 어떤 값에 해당하는지 알 수 있다. 이는 아래의 식을 본다면 좀 더 직관적으로 이해할 수 있을 것이다.
$$
F(X) \equiv U \sim Uniform(0,1) \\
\Leftrightarrow F(X) \bullet F^{-1}(X) = F^{-1}(U) \\
\Leftrightarrow X = F^{-1}(U)
$$
위 식을 하나하나 살펴보자
$$
F(X) \equiv U \sim Uniform(0,1) \\
☞ 어떤 \ 확률 \ 분포 \ f(x)의 \ CDF \ F(X)는 \ Uniform \ Distribution과 \ 동일한 \ 결과를 \ 가짐 \\
\\
F(X) \bullet F^{-1}(X) = F^{-1}(U) \\
☞ 양 \ 변의 \ CDF의 \ 역함수를 \ 취함 \\
\\
X = F^{-1}(U) \\
☞ 확률 \ 변수 \ X는 \ CDF의 \ 역함수에 \ Unifrom \ Distribution의 \ 결과를 \ input으로 \ 넣으면 \ 구할 \ 수 \ 있음
$$
즉, sampling이 쉬운 uniform distribution과 CDF의 특성을 활용한 트릭으로 목표 확률 분포의 sampling을 수행할 수 있게 된다.



### 2.2 Example

좀 더 직관적인 이해를 위해 지수 분포(exponential distribution)에 inverse CDF sampling을 적용해 본다. Exponential distribution은 아래와 같은 식으로 표현할 수 있다.


$$
f_X(x)=e^{-x}
$$


먼저, 확률 변수 X에 대한 sampling을 위해 pdf의 cdf를 구해본다.


$$
F(x) = \int_0^x f(x) dx\\
= \int_0^x e^{-x^{\prime}} dx^{\prime}\\
= [- e^{-x^{\prime}}]_0^x \\
= 1 - e^{-x}
$$


이때, CDF의 결과는 uniform distribution에 속하므로 F(x)를 원소 u로 치환한 뒤 역함수를 구한다.
$$
u = 1-e^{-x} \\
e^{-x} = 1 - u \\
- x = ln(1-u) \\
x = - ln(1-u)
$$
이를 통해 uniform distiribution에서 sampling 된 특정 값을 CDF의 역함수의 입력 값으로 사용하게 되면 원래의 확률 변수의 sampling이 가능함을 알 수 있다. 조금 더 정리를 하면 아래와 같다.
$$
u_i = U(0,1) \\
x_i = inverseCDF(u_i) \\
= - ln(1-u_i)
$$


### 2.3 Visualization

위 내용을 python을 통해 시각화해본다.

````python
import numpy as np
import matplotlib.pyplot as plt

# 지수 분포 역함수
def inverse_cdf_exponential(u, lambd=1):
    return -np.log(1 - u) / lambd

# 균등 분포 무작위 샘플링
u_sampled_30 = np.random.uniform(0, 1, 30)

# 역함수 샘플링 수행
samples_exp_30 = inverse_cdf_exponential(u_sampled_30, lambd=1)

# plot range 설정
samples_index_30 = np.arange(1, 31)

plt.figure(figsize=(12, 8))
plt.scatter(samples_index_30, u_sampled_30, color='blue', label='Uniform Distribution Sampling')
plt.scatter(samples_index_30, samples_exp_30, color='green', label='Exponential Distribution Sampling')
for i, (u, exp) in enumerate(zip(u_sampled_30, samples_exp_30), 1):
    plt.plot([i, i], [u, exp], 'r--')
plt.title('Mapping Uniform Sampling to Exponential Sampling with 30 Samples')
plt.xlabel('Sampling Index')
plt.ylabel('Value')
plt.legend()
plt.show()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/statistics/sampling/inverse_cdf/1.png?raw=true" width="600" height="300"></p>

- 파란 점은 uniform distribution에서 sampling한 값
  - sampling 결과가 0 ~ 1 사이에 위치함
- 녹색 점은 파란 점을 입력으로 한 inverse CDF의 결과 값
  - sampling 결과가 exponential distribution을 따름

이제 이러한 과정을 매우 많이 반복하게 되면 exponential distribution의 확률 밀도에 맞게 sampling이 수행됨을 알 수 있다.

```python
import numpy as np
import matplotlib.pyplot as plt

# 지수분포의 역CDF(Inverse CDF) 함수 정의
def inverse_cdf_exponential(u, lambd=1):
    return -np.log(1 - u) / lambd

# 균등 분포에서 무작위 샘플링
u = np.random.uniform(0, 1, 1000)

# 지수분포 샘플링
samples = inverse_cdf_exponential(u, lambd=1)

# 결과 시각화
plt.hist(samples, bins=50, density=True, alpha=0.6, color='g')
plt.title('Histogram of Exponentially Distributed Samples')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
```

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/statistics/sampling/inverse_cdf/2.png?raw=true" width="600" height="300"></p>

### 2.3 Limitation

Inverse CDF 방법을 통해 직관적으로 와닿지 않던 sampling에 대해 이해하고 수행해 볼 수 있었다. 그러나 해당 방법은 아래와 같은 한계점이 존재한다.

- 주어진 pdf에 대해 cdf를 계산하는 것은 적분 연산이 필요함
- cdf를 계산할 수 있어도 역함수를 구해야함

즉, 수식을 통해 샘플링을 수행하는 것은 어려운 일이며 이를 해결하기 위한 다양한 sampling 방법들이 존재한다.

🏃 **Next Step**

- Inverse CDF 방법 외 다른 sampling 방법들을 알아보자
- 가장 기초적인 **Rejection Sampling**을 배워보자

