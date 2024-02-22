---
layout: single
title:  'Continuous distribution (4) Beta Distribution'
toc: true
categories: [Probability Distribution]
tags: [Continuous, Beta]

---

여러 분포들에 대한 소개 [참조사이트](https://mathnotes.tistory.com/5)
{: .notice}

## 1. Definition

> 0과 1 사이의 값에 대한 확률분포

- 확률변수 X: 성공 확률과 같이 비율을 나타내는 0과 1사이의 값
- 두 매개변수 $\alpha$와 $\beta$가 주어져야 함
  - $\alpha , \beta$: 성공과 실패에 해당하는 모수, 형상척도
  - 두 변수에 따라 다양한 분포의 형태를 나타냄
- 베이지안 통계에서 사전 분포나 사후 분포로 활용

## 2. PDF

{% raw %}
$$
f(x; \alpha, \beta) = \frac {x^{\alpha-1}(1-x)^{\beta-1}} {\Beta(\alpha, \beta)} \\
0 \leq x \leq 1, \alpha, \beta > 0 (real)
$$
{% endraw %}

- $\alpha , \beta$: 성공과 실패에 해당하는 모수, 형상척도

📍 **베타함수**

{% raw %}
$$
\Beta(\alpha, \beta)= \frac {\Gamma(\alpha)\Gamma(\beta)} {\Gamma(\alpha+\beta)} \\
= \int^{1}_{0}x^{\alpha-1}(1-x)^{\beta-1}ds
$$

## 3. Theta

$$
X \sim \Beta(\alpha, \beta)
$$

- $\alpha , \beta$: 성공과 실패에 해당하는 모수, 형상척도
- $\Beta(\alpha , \beta)$일때, 성공, 실패 횟수를 $(\alpha-1, \beta-1)$로 볼 수 있음

## 4. Summary Statistics

- Expectation: $\frac {\alpha} {\alpha + \beta}$
- Variance: $\frac {\alpha \beta} {(\alpha + \beta)^2 (\alpha + \beta + 1)}$

## 5. Visualization

````python
from scipy.stats import beta
import matplotlib.pyplot as plt
import numpy as np

# alpha와 beta 매개변수 설정
params = [
    (1, 1),  # 균등 분포
    (0.5, 0.5),
    (2, 3),
    (5, 1),
    (2, 2)
]

# x 축 값 설정: 0부터 1까지
x = np.linspace(0, 1, 100)

plt.figure(figsize=(12, 8))

# 각 (alpha, beta) 조합에 대해 베타 분포의 PDF를 그래프로 표시
for (a, b) in params:
    y = beta.pdf(x, a, b)
    plt.plot(x, y, label=f'α={a}, β={b}')

plt.title('Beta Distribution for Various α and β Values')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()
plt.show()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/statistics/distributions/be1.png?raw=true" width="600" height="500"></p>

- $\alpha, \beta$가 (1,1)인 경우 uniform distribution임을 알 수 있음
- $\alpha, \beta$가 0보다 작으면 제품 고장률에 대한 분포로 볼 수 있음
  - 제품이 처음에는 고장이 많이나다가 안정기에 들고 연식이 오래되면 다시 고장 확률 증가
- $\alpha, \beta$가 같으면 정규분포 형태를 띔

## 6. Usage

- 베타분포는 베이즈 추정법에서 사전분포(=prior)로 자주 이용됨
- 모수에 따라 다양한 확률분포를 그릴 수 있기에 다양한 prior를 나타낼 수 있음
- 베타분포는 이항분포의 켤레사전분포로 계산에 용이함

📍**Example1: 리그오브레전드 승률**

> 나는 영어이름이 Jayce일 정도로 제이스 장인이다. 이번 시즌에만 1000판을 박아서 520승 480패 승률 52%를 기록했다. 티어는 알려줄 수 없지만 이정도면 제이스 장인임이 분명하다. 그런데 한 친구녀석이 자기는 3승 2패로 승률 60%라고 나와 동등하거나 그 이상이라는 도발을 하였다. 나는 도저히 믿을 수 없어 확률을 사용해 친구를 야지주려고 한다.

- 베타분포 모델링

$$
X_{me} \sim \text{Beta}(521, 481) \\
X_{friend} \sim \text{Beta}(4, 3)
$$

👀 **분포 시각화**

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/statistics/distributions/be4.png?raw=true" width="600" height="500"></p>

- 나의 승률은 약 0.5에서 매우 밀집되어 있음
- 친구의 승률은 0.6에서 가장 밀집되어 있으나, 분산이 매우 큼
- 즉, 내 승률은 언제든 0.5로 나올 수 있으나, 친구의 승률은 분산이 크기 때문에 믿음직스럽지 못함



📍 **Example2: 메이플스토리 주문서 확률**

> 메이플스토리에는 장갑 공격력 주문서가 매우 고가에 팔리고 있다. 노가다 목장갑에 10% 확률의 주문서가 발리는 순간 인생 역전 꽃길 시작이기 때문이다. 나도 흙수저 인생에서 벗어나기 위해 갖은 노가다와 사채를 통해 주문서를 10장 구매하였는데 모두 한줌재가 되어 사라지고 말았다. 빈털터리가 된 나는 확률조작임을 의심하며 친구들에게 물어보았다. 친구들은 내가 10연펑을 한 사실을 모르며 주문서에 대해 다음과 같은 의견을 제시하였다.
>
> 😗: 확률이니까 0~1사이의 값을 가지지 않을까?
>
> ☹️: 붙, 펑 50%임
>
> 😀: 체감상 10%는 주작임 더 낮을듯
>
> 이제 베이즈 추정법을 통해 실제 10% 주문서가 성공할 확률을 추정해보자.

- 주문서가 발릴 확률을 확률변수 $\theta$로 설정
- 베이즈 추정법

{% raw %}
$$
f_{(\theta | X)}(\theta | x)= \frac {f_{(X | \theta)}(X | \theta) f_{\theta}(\theta)}{f_X(x)}
$$

{% endraw %}

- $f_{(\theta | X)}(\theta | x)$: 사후확률, posterior
  - 데이터 X를 관측한 후 업데이트된 확률변수의 분포
  - 주문서 트라이 후 성공확률에 대한 분포
- $f_{(X | \theta)}(X | \theta)$ : 가능도, likelihood
  - 확률변수 $\theta$에 대한 사전분포가 맞다는 가정 하에 관측되어야 할 데이터 X의 분포
  - prior에 대한 예측이 옳다고 했을 때, 결과물이 나타내야할 모습
- $f_{\theta}(\theta)$: 사전확률, prior
  - 데이터 X를 관측하기 전 확률변수 $\theta$의 분포에 대한 예상
  - 친구들이 생각하는 주문서 성공 확률에 대한 분포
- $f_X(x)$: 사후확률, posterior
  - 확률변수 $\theta$를 추정하기 위해 얻은 데이터 $X$의 분포
  - 주문서 트라이 후 결과

<br>

📍 **Step1. 사전확률**

베이즈 추정법의 출발점은 사전확률을 정의하는 것

- 친구 😗의 예상 ☞ 확률이니까 0~1사이의 값을 가지지 않을까?
  - 0~1까지 뭐가 나올지 모름
  - prior: uniform distribution
- 친구 ☹️의 예상 ☞ 붙, 펑 50%임
  - prior: x축이 50%인 지점에서 가장 높은 확률값을 가짐
- 친구 😀의 예상 ☞ 체감상 10%는 주작임 더 낮을듯
  - prior: x축이 10% 아래에서 가장 높은 확률 값을 가짐

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

x = np.linspace(0, 1, 1000)

# 각 베타 분포의 매개변수 설정
a1, b1 = 1, 1 # uniform
rv1 = beta(a1, b1)
frv1 = rv1.pdf(x)

a2, b2 = 5, 5 # 50%
rv2 = beta(a2, b2)
frv2 = rv2.pdf(x)

a3, b3 = 2, 21 # 10%보다 낮은 5%..?
rv3 = beta(a3, b3)
frv3 = rv3.pdf(x)

# 베타 분포 그리기
plt.plot(x, frv1, label='😗`s priror', color='r')
plt.plot(x, frv2, label='😕`s priror', color='b')
plt.plot(x, frv3, label='😄`s priror', color='g')
plt.xlabel('$\\theta$')
plt.ylabel('$f(\\theta)$')
plt.grid()
plt.legend()
plt.show()
```

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/statistics/distributions/be2.png?raw=true" width="600" height="500"></p>

<br>

📍 **Step2. 가능도**

주문서는 성공, 실패에 대한 것이기 때문에 이항분포를 가능도로 정의

- 성공 확률인 $\theta$인 주문서를 n번 트라이하였을 때 관측되는 성공횟수를 $X$라고 함

$$
X \sim \text{Bin}(n, p) \\
f_{(x | \theta)} = \binom {n} {x} \theta^x (1-\theta)^{n-x}
$$

<br>

📍 **Step3. 증거**

- 증거는 주어진 조건이므로 변하지 않는 상수임
- 따라서 비례기호를 통해 posterior를 아래와 같이 정의할 수있음

{% raw %}
$$
f(\theta | x) \propto f(x | \theta) f(\theta)
$$
{% endraw %}

<br>

📍 **켤례사전분포**

- 위 식을 전개하면 아래와 같이 표현 됨

{% raw %}
$$
f(\theta | x) \propto \theta^x (1-\theta)^{n-x} \cdot \theta^{\alpha-1}(1-\theta)^{\beta-1} \\
f(\theta | x) \propto \theta^{\alpha+x+1} \cdot (1-\theta)^{\beta - x + n-1}
$$
{% endraw %}

- 따라서 posterior의 분포는 $\Beta(\alpha + x, \beta - x + n)$으로 베타분포로 정의 할 수 있음
- 이렇게 prior와 posterior이 같은 연산을 나타내는 경우 켤례사전분포라고 함

<br>

📍 **Step4. 사후확률**

- 관측된 데이터를 통해 사후확률을 업데이트

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

theta = np.linspace(0, 1, 1000)
trial = 10
success = 0
failure = trial - success

a_alpha, a_beta = 1, 1
a_prior = beta(a_alpha, a_beta).pdf(theta)
a_posterior = beta(a_alpha + success, a_beta + failure).pdf(theta)

b_alpha, b_beta = 5, 5
b_prior = beta(b_alpha, b_beta).pdf(theta)
b_posterior = beta(b_alpha + success, b_beta + failure).pdf(theta)

c_alpha, c_beta = 2, 21
c_prior = beta(c_alpha, c_beta).pdf(theta)
c_posterior = beta(c_alpha + success, c_beta + failure).pdf(theta)

fig, ax = plt.subplots(1, 3)
fig.set_figwidth(1000 / fig.dpi)
fig.set_figheight(200 / fig.dpi)

ax[0].plot(theta, a_prior, color="r", label="prior: Beta(1,1)=0~1")
ax[0].plot(theta, a_posterior, color="r", alpha=0.3, label="posterior: Beta(1,11)")
ax[0].set_xlabel(r"$\theta$")
ax[0].set_ylabel(r"f($\theta$)")
ax[0].set_title("A")
ax[0].legend(fontsize=8, frameon=False, loc="upper center")
ax[0].set_xlim(0, 1.5)
ax[0].set_ylim(0, 15)

ax[1].plot(theta, b_prior, color="b", label="prior: Beta(5,5)=50%")
ax[1].plot(theta, b_posterior, color="b", alpha=0.3, label="posterior: Beta(5,15)")
ax[1].set_xlabel(r"$\theta$")
ax[1].set_title("B")
ax[1].legend(fontsize=8, frameon=False, loc="upper center")
ax[1].set_xlim(0, 1.5)
ax[1].set_ylim(0, 15)

ax[2].plot(theta, c_prior, color="g", label="prior: Beta(2,21)=under 10%")
ax[2].plot(theta, c_posterior, color="g", alpha=0.3, label="posterior: Beta(2,31)")
ax[2].set_xlabel(r"$\theta$")
ax[2].set_title("C")
ax[2].legend(fontsize=8, frameon=False, loc="upper center")
ax[2].set_xlim(0, 1.5)
ax[2].set_ylim(0, 15)
```

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/statistics/distributions/be3.png?raw=true" width="1000" height="300"></p>

- 각자 예상했던 prior에 기반해 확률변수 $\theta$의 확률분포를 업데이트 한 결과
- 친구들은 내가 트라이한 주문서 데이터를 통해 $\theta$의 확률분포가 저럴 것이다라고 다시 생각하게 됨

