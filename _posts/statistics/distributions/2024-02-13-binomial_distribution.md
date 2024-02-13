```yaml
layout: single
title:  'Binomial Distribution'
toc: true
categories: [Statistics]
tags: [PDF, PMF]
```

이항분포에 대한 정리
{: .notice}

## 1. Definition

> 연속된 n번의 독립적 시행에서 각 시행이 확률 p를 가질 때(=베르누이 시행)의 확률 분포

📍**베르누이 시행**

- 두 가지 결과가 있는 단일 시행
- ex) 동전 던지기 -> {앞, 뒤}
- n=1일 때 이행 분포는 베르누이 분포와 동일

## 2. PMF

$$
f_x(x) = \binom{n}{x}p^x(1-p)^{n-x}
$$

- p: 성공 확률
- n: 시행 횟수
- x: 성공 횟수
- $\binom{n}{x}$: 이항계수

📍**조합**

$$
C(n, r) = \binom{n}{r} = \frac{n!}{r!(n-r)!}


$$

📍**순열**

$$
P(n, r) = \frac{n!}{(n-r)!}
$$

📍**독립**

- n개의 확률의 곱으로 표현
- 서로 다른 사건의 확률을 곱할 수 있다는 것은 독립을 의미

$$
\text{독립} : \, P(A \cap B) = P(A) \cdot P(B) \\
\text{일반} : \, p(A \cap B) = p(A) \cdot p(B | A)
$$

📍 **독립 항등 분포(i.i.d)**

- 각 독립 변수가 같으면서 (=항등)
- 서로 영향을 미치지 않음 (=독립)

## 3. Theta

$$
X \sim \text{Bin}(n, p) \\
\text{Bern}(p) = \text{Bin}(1,p)
$$

- p: 성공 확률
- n: 시행 횟수

## 4. Summary statistics

- Expectation: $np$
- Variance: $np(1-p)$

## 5. Visualization

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

def plot_binomial_distribution(n, p):
    x = np.arange(0, n+1)
    binomial_pmf = binom.pmf(x, n, p)

    plt.bar(x, binomial_pmf, color='skyblue')
    plt.ylim(0, 1)
    plt.title(f'Binomial Distribution (n = {n}, p = {p})')
    plt.xlabel('Number of Successes')
    plt.ylabel('Probability')
    plt.xticks(x)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

n = 10
probabilities = [0.1, 0.5]

for p in probabilities:
    plot_binomial_distribution(n, p)
```

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/statistics/distributions/bi1.png?raw=true" width="600" height="400"></p>

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/statistics/distributions/bi2.png?raw=true" width="600" height="400"></p>

👀 **N이 충분히 크면??**

- n이 100 이상일 경우 정규분포와 유사함을 알 수 있음

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/statistics/distributions/bi3.png?raw=true" width="600" height="400"></p>

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/statistics/distributions/bi4.png?raw=true" width="600" height="400"></p>
