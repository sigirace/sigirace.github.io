---
layout: single
title:  'Sampling (4) Markov Chanin Monte Carlo가 뭐야?'
toc: true
categories: [Sampling]
tags: [MCMC, Markov Chain, Monte Carlo]

---

본 게시물은 공돌이의 수학정리노트의 [Markov Chain Monte Carlo](https://angeloyeo.github.io/2020/09/17/MCMC.html)을 참고하여 작성하였다.
{: .notice}

## 1. Introduce

### 1.1 Markov Chain

👀 **Definition**

> 과거와 현재 상태가 주어졌을 때, 미래 상태의 조건부 확률 분포가 과거 상태와는 독립적으로 현재 상태에 의해서만 결정된다.

- Markov Chain은 이산 시간 확률 과정

- 상태의 변화를 전이라고 함

📍 **수학적 표현**

$$
Pr(X_n = x_n | X_{n-1} = x_{n-1}, ...,X_1=x_1) \\
= Pr(X_n=x_n | X_{n-1}=x_{n-1})
$$

- 조건부 확률 확인

- 메모리가 1인 Markov chain 표현

- 메모리가 1이면 상태는 이전의 상태에만 의존함

📍 **Example**

```python
import numpy as np

# 상태 정의
states = ['Sunny', 'Rainy']

# 전이 확률 행렬: P[i, j]는 상태 i에서 j로 전이할 확률
# P = [
#  [Sunny -> Sunny, Sunny -> Rainy],
#  [Rainy -> Sunny, Rainy -> Rainy]
# ]
P = np.array([
    [0.9, 0.1],  # Sunny에서 Sunny로, Sunny에서 Rainy로
    [0.5, 0.5]   # Rainy에서 Sunny로, Rainy에서 Rainy로
])

# 초기 상태 (Sunny로 시작)
current_state = 0  # 'Sunny' 상태의 인덱스

# 마르코프 체인 시뮬레이션
num_steps = 10  # 시뮬레이션할 단계 수
for step in range(num_steps):
    print(f"Step {step}: {states[current_state]}")
    current_state = np.random.choice([0, 1], p=P[current_state])

print(f"Final State: {states[current_state]}")
```

```
Step 0: Sunny
Step 1: Rainy
Step 2: Rainy
Step 3: Sunny
Step 4: Sunny
Step 5: Rainy
Step 6: Sunny
Step 7: Sunny
Step 8: Sunny
Step 9: Rainy
Final State: Rainy
```

### 1.2 Monte Carlo

👀 **Definition**

> Monte Carlo method는 반복된 무작위 추출을 이용하여 값을 수리적으로 근사하는 알고리즘을 부르는 용어이다.

- 무수한 수행을 통해 수치적으로 계산하기 어려운 값을 근사하려는 방법론

📍 **근사화 이유**

- 계산하려는 값이 닫힌 형식(=closed form)으로 표현되지 않을 경우

- 수리적으로 복잡할 경우

📍**Note: closed form**

- 주어진 문제가 일반적으로 알려진 함수나 수학 연산으로 해를 구할 수 있는 식

- 혹은 해석이 가능한 식 (ex 무한개의 더하기라도 $\sum$으로 표현하여 해석)

📍**Example**

원의 넓이를 구하는 예시로 몬테 카를로 근사 방법에 대해 알아본다.

```python
import random

def estimate_pi(num_samples):
    inside_circle = 0
    for _ in range(num_samples):
        x, y = random.random(), random.random()  # 0과 1 사이의 무작위 점 생성
        distance = x**2 + y**2  # 원점으로부터의 거리 계산
        if distance <= 1:  # 단위 원 내부에 있는지 판단
            inside_circle += 1
    pi_estimate = 4 * inside_circle / num_samples  # π 값 추정
    return pi_estimate

# 10000번의 시행으로 π 추정
pi_estimate = estimate_pi(10000)
print(f"Estimated π: {pi_estimate}")
```

```
Estimated π: 3.138
```

📍 **Visualization**

```python
import matplotlib.pyplot as plt
import random

def estimate_pi_and_points(num_samples):
    inside_circle_x = []
    inside_circle_y = []
    outside_circle_x = []
    outside_circle_y = []

    inside_circle = 0
    for _ in range(num_samples):
        x, y = random.random(), random.random()  
        distance = x**2 + y**2  
        if distance <= 1:  
            inside_circle += 1
            inside_circle_x.append(x)
            inside_circle_y.append(y)
        else:
            outside_circle_x.append(x)
            outside_circle_y.append(y)

    pi_estimate = 4 * inside_circle / num_samples  
    return pi_estimate, inside_circle_x, inside_circle_y, outside_circle_x, outside_circle_y

num_samples = 10000
pi_estimate, inside_x, inside_y, outside_x, outside_y = estimate_pi_and_points(num_samples)

# Plotting
plt.figure(figsize=(6, 6))
plt.scatter(inside_x, inside_y, color='blue', s=1, label='Inside circle')
plt.scatter(outside_x, outside_y, color='red', s=1, label='Outside circle')
plt.xlabel('X')
plt.ylabel('Y')
plt.title(f"Monte Carlo Estimation of π (Estimate: {pi_estimate})")
plt.legend()
plt.axis('equal') 
plt.show()
```

![](https://github.com/sigirace/page-images/blob/main/statistics/sampling/mcmc/mc1.png?raw=true)

### 1.3 Markov Chain Monte Carlo (MCMC)

👀**Definition**

> Markov chain에 기반하여 확률 분포로부터 원하는 분포의 정적 분포를 갖는 표본을 추출하는 알고리즘

- MCMC는 표본을 추출하는 방법 ☞ Sampling

- Sampling: 확률 분포로부터 표본을 추출하는 것

📍**Requirements**

- Sampling을 위한 target 분포(=확률분포)가 있어야 함

- Target distirubtion은 아래와 같다고 가정

$$
f(x) = 0.3 \cdot e^{-0.2 x^2} + 0.7 \cdot e^{-0.2(x - 10)^2}
$$

## 2. Sampling Process

### 2.1 Random Initialization

- Sample space에서 random point를 선택

📍 **Example**

```python
import matplotlib.pyplot as plt
import numpy as np

def target_distribution(x):
    return 0.3 * np.exp(-0.2 * x**2) + 0.7 * np.exp(-0.2 * (x - 10)**2)

x = np.linspace(-10, 20, 1000)
target_pdf = target_distribution(x)
initial_point = 7

plt.figure(figsize=(10, 6))
plt.plot(x, target_pdf, label='Target Distribution $f(x)$', linewidth=2)
plt.scatter(initial_point, 0, color='red', label='Initial Point')
plt.xlabel('x')
plt.ylabel('Density')
plt.legend()
plt.show()
```

![](https://github.com/sigirace/page-images/blob/main/statistics/sampling/mcmc/mc2.png?raw=true)

- Sample space 중 initial point로 7 선택

📍**Note: Sample space**

- 실험 결과에서 가능한 모든 결과의 집합

- ex) 동전 던지기의 샘플공간 ☞ {앞, 뒤}

- ex) 주사위 던지기의 샘플공간 ☞ {1, 2, 3, 4, 5, 6}

- ex) 정규분포의 샘플공간 ☞ {$-\infty, \infty$}

### 2.2 Recommend

- Initial point를 중심으로 하는 제안분포 생성
  
  - Metropolis일 경우 symmetric한 확률분포를 사용하며 대부분 정규분포 사용
  
  - 정규분포의 너비는 연구자의 선택에 따라 임의로 설정

- 제안분포에서 새로운 샘플 포인트를 추출

- 제안된 샘플 포인트와 그 포인트에서의 타겟 분포의 값 비교
  
  - ${f(x_1) \over f(x_0)}>1$ 일 경우 accept

- Accept일 경우 샘플 포인트를 중심으로 과정 반복

- Reject일 경우 다음 step으로 이동

📍**Note: MCMC 방법에 따른 분포의 형태**

- Metropolis: symmetric한 확률 분포 사용 ☞ ex) 정규분포

- Hastings: 일반적인 확률 분포

📍**Note: Hasting 알고리즘**

- 제안분포를 g(x)라고 할 때 아래와 같이 정규화
  
  - $\frac{\frac{f(x_1)}{g(x_1 \mid x_0)}}{\frac{f(x_0)}{g(x_0 \mid x_1)}}$



📍**Example: 제안분포 생성**

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def target_distribution(x):
    return 0.3 * np.exp(-0.2 * x**2) + 0.7 * np.exp(-0.2 * (x - 10)**2)

x = np.linspace(-10, 20, 1000)
target_pdf = target_distribution(x)
initial_point = 7

normal_dist = norm.pdf(x, initial_point, 2)

plt.figure(figsize=(10, 6))
plt.plot(x, target_pdf, label='Target Distribution $f(x)$', linewidth=2)
plt.plot(x, normal_dist, label='Normal Distribution $N(initial\_point, 2)$', linewidth=2, linestyle='--')
plt.scatter(initial_point, 0, color='red', label='Initial Point')
plt.axvline(x=initial_point, color='gray', linestyle='--', label='Center of Normal Distribution')
plt.xlabel('x')
plt.ylabel('Density')
plt.legend()
plt.show()
```

![](https://github.com/sigirace/page-images/blob/main/statistics/sampling/mcmc/mc3.png?raw=true)

📍**Example: 신규 포인트 추천**

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def target_distribution(x):
    return 0.3 * np.exp(-0.2 * x**2) + 0.7 * np.exp(-0.2 * (x - 10)**2)

x = np.linspace(-10, 20, 1000)
target_pdf = target_distribution(x)
initial_point = 7

normal_dist = norm.pdf(x, initial_point, 2)

def recommend(x_0, target_distribution):
    x_1 = np.random.normal(x_0, 2)

    f_x_0 = target_distribution(x_0)
    f_x_1 = target_distribution(x_1)

    if f_x_1 / f_x_0 > 1:
        return (x_1, f_x_1), (x_0, f_x_0), True
    else:
        return (x_1, f_x_1), (x_0, f_x_0), False

new_points, initial_points, is_accepted = recommend(initial_point, target_distribution)

plt.figure(figsize=(10, 6))
plt.plot(x, target_pdf, label='Target Distribution $f(x)$', linewidth=2)
plt.plot(x, normal_dist, label='Normal Distribution $N(initial\_point, 2)$', linewidth=2, linestyle='--')
plt.scatter(initial_points[0], 0, color='red')
plt.scatter(initial_points[0], initial_points[1], color='red', label='Initial Point')
plt.scatter(new_points[0], 0, color='green')
plt.scatter(new_points[0], new_points[1], color='green', label='new Point')
plt.xlabel('x')
plt.ylabel('Density')
plt.legend()
plt.show()
```

![](https://github.com/sigirace/page-images/blob/main/statistics/sampling/mcmc/mc4.png?raw=true)

- Accept인 경우

![](https://github.com/sigirace/page-images/blob/main/statistics/sampling/mcmc/mc5.png?raw=true)

- Reject인 경우

### 2.3 Resurrection

- 일명 **패자부활전**으로 reject된 샘플들을 무조건 이용하지 않는 것이 아니라 통계적으로 수용할 수 있도록 함

- 원래 샘플을 x_1, 제안분포를 통해 새로 제안받은 샘플을 x_2라 할 때 다음을 비교
  
  - ${f(x_1) \over f(x_0)}>u$
  
  - 이때 u는 uniform distribution $U_{(0,1)}$에서 추출한 임의의 샘플

📍**Note: Why doing resurrection?**

- 앞서 recommend 과정에서 accpet되는 조건은 새로운 샘플이 target distribution에서 더 큰 값을 가지고 있어야 함

- 샘플은 계속해서 target distribution 의 높은 부분으로 수렴함

- 패자부활전 없이는 낮은 확률을 가진 샘플들이 추출되지 않는 문제가 발생함

## 3. Visualization

```python
# 필요한 라이브러리 재설정
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from scipy.integrate import quad


# 목표 분포 정의
def target_distribution(x):
    return 0.3 * np.exp(-0.2 * x**2) + 0.7 * np.exp(-0.2 * (x - 10)**2)

x_domain = [-7, 17]

# MCMC Metropolis 알고리즘 정의
def metropolis_algorithm(target_distribution, initial_point, num_samples, step_size=2):
    samples = [initial_point]
    current_point = initial_point

    for i in range(num_samples - 1):
        new_point = np.random.normal(current_point, step_size)
        if x_domain[0] <= new_point <= x_domain[1]:
            f_current = target_distribution(current_point)
            f_new = target_distribution(new_point)
            acceptance_ratio = f_new / f_current

            u = np.random.uniform(0, 1)
            if acceptance_ratio > u:
                samples.append(new_point)
                current_point = new_point
            else:
                samples.append(current_point)
        else:
            samples.append(current_point)

    return samples

# 실행 매개변수 설정
num_samples = 5000
initial_point = 7

# 알고리즘 실행
samples = metropolis_algorithm(target_distribution, initial_point, num_samples)

# -7부터 17까지 목표 분포의 적분 계산
integral_result, _ = quad(target_distribution, x_domain[0], x_domain[1])

integral_result

# 샘플 히스토그램 생성 (정규화 없이)
counts, bin_edges = np.histogram(samples, bins=int(30 / 0.5), density=False)
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

# 적분 결과를 사용하여 히스토그램 정규화
total_samples = len(samples)
normalized_counts = (counts / total_samples) * (integral_result / np.diff(bin_edges))

plt.figure(figsize=(10, 6))
plt.plot(x, target_pdf, label='Target Distribution', linewidth=2)
plt.bar(bin_centers, normalized_counts, width=np.diff(bin_edges)[0], alpha=0.5, color='orange', label='MCMC Samples (Normalized by Integral)')
plt.scatter(initial_point, target_distribution(initial_point), color='red', zorder=5, label='Initial Point')
plt.xlabel('x')
plt.ylabel('Density')
plt.legend()
plt.title('MCMC Sampling with Histogram Normalized by Integral Result')
plt.show()
```

![](https://github.com/sigirace/page-images/blob/main/statistics/sampling/mcmc/mc6.png?raw=true)

- MCMC의 metropolis 방식에 따른 sampling 수행 결과

🏃**Next Step**

- MCMC는 Sampling 뿐 아니라 확률분포의 파라미터를 추정할 수 있음

- MCMC를 이용한 Bayesian estimation에 대해 알아봄
