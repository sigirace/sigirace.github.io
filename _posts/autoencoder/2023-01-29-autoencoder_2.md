---
layout: single
title:  'Autoencoder의 모든것의 모든것 1-2'
toc: true
categories: Autoencoder
tags: [Autoencoder, Deep Learning, MLE, MSE, Cross Entropy]
---

본 게시물은 이활석님의 [강의](https://www.youtube.com/watch?v=o_peo6U7IRM&t=4)를 보고 정리하는 글이다.
{: .notice}

<div class="notice">
<h3>강의 리스트</h3>
<li><a href="https://sigirace.github.io/autoencoder/autoencoder_1/">Autoencoder의 모든것의 모든것 1-1</a></li>
</div>



## 2. Revisit Deep Neural Networks

해당 Chapter에서는 DNN이 MLE와 동일함을 보이기 위해 DNN을 풀어 설명한다.

### 2.1 Classic Machine Learning

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_4.png?raw=true" width="650" height="400"></p>

고전적인 머신러닝의 접근방식은 데이터에서 추상화된 정보를 뽑는 것이다. 이를 위해 먼저 데이터를 모은다. 다음으로 문제를 해결할 모델을 정의하고, 모델의 파라미터를 설정한다. 이후 모델에서 나온 정보와 실제 정보의 다른 정도를 계산(measure)하는 loss function을 정의한다. 학습단계에서는 모델을 규정짓는 파라미터를 바꿔가며 앞서 수집한 training data들에 대해 로스가 최소가 되는 파라미터를 찾는다. 마지막으로 test data에 대해 정보 값을 추정한다. 이 과정에서 주요하게 볼 부분은 입력이 고정되면 출력 또한 고정된다는 것이다.

### 2.2 Deep Neural Networks

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_5.png?raw=true" width="650" height="400"></p>

딥러닝에서 데이터를 모으는 부분은 고전적 머신러닝과 동일하다. 모델을 정의하는 부분은 역시나 문제에 맞는 딥러닝 모델들을 사용한다. 이때 학습해야 할 파라미터는 주로 네트워크를 구성하는 weight와 bias이다. 이후 loss function을 정의하는 부분에서 딥러닝은 backpropagation으로 인한 제약조건이 생긴다. 이는 backpropagation에 대한 아래 두 가지의 가정 때문이다.

```
1. 전체 training data의 loss는 sample data로 부터 나온 loss의 합과 같다.
    ☞ sample loss의 곱/ 나누기 등등으로 하는 경우는 가정하지 않는다.
2. loss에 들어가는 파라미터는 네트워크의 마지막 출력과 실제 정보 뿐이다.
    ☞ 네트워크 중간의 출력 값으로 계산하는 경우는 가정하지 않는다.
```

이로인해 딥러닝에서 사용하는 loss function은 MSE와 Cross Entropy 뿐이다. 

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_6.png?raw=true" width="650" height="400"></p>

training data 전체의 loss를 최소화 시키는 파라미터를 찾는 학습 방식은 대부분 optimal problem을 찾는 가장 간단한 방식인 gradient descent을 사용한다. 이는 step by step으로 점차 정답에 가까워지는 iterative method이다. 이러한 방식을 위해서는 아래의 질문에 대한 정의가 필요하다.

```
1. 현재 파라미터에서 어떻게 update 할 것인가
    ☞ loss가 줄어들기만 하면 update
2. 언제 파라미터 update를 stop 할 것인가
    ☞ loss가 더 이상 줄어들지 않으면 stop
```

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_7.png?raw=true" width="650" height="200"></p>

파라미터를 바꿔 loss를 줄이는 것은 알겠으나 파라미터의 차원은 네트워크가 깊어질수록 커지게 된다. 이때 gradient descent 방식으로 파라미터를 조정한다면 각각을 얼마만큼 바꿔줘야 하는지에 대한 문제에 마주친다. 이에 대한 해답은 다음과 같다.

#### [Taylor expansion](https://darkpgmr.tistory.com/59)

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_7_1.png?raw=true" width="400" height="150"></p>

테일러 급수 또는 테일러 전개는 어떤 미지의 함수 f(x)를 근사 다항 함수로 표현하는 것이다. 해당 수식의 x를 $\theta + \Delta \theta$로 $a$를 $\theta$로 치환하면 위의 gradient descent과 동일하게 된다. ($\bigtriangledown L$ 은 미분의 의미)

#### Approximation

이는 Taylor Expansion에서 1차 미분만 사용하여 $L(\theta + \Delta \theta)$를 근사한 것이다. 이때 더 많은 차수를 사용한다면 approximation error가 작아지게 된다. 하지만 계산이 복잡하고 시간이 오래 걸리기 때문에 딥러닝에서는 1차 미분항까지만 사용한다. 근사 다항식의 $L(\theta)$를 왼쪽 항으로 옮겨 구한 변화량 $\Delta L$은 앞서 loss는 항상 작아지는 방향으로 움직이는 것으로 정의하였기 때문에 음수가 되길 원한다. 따라서 만약 파라미터의 변화량 $\Delta \theta$가 $-n \bigtriangledown L$(Loss의 미분값)이라면 파라미터의 변화로 인한 Loss의 변화량 $\Delta L$은 언제나 음수이게 된다. 

(추가)<br>미분값들은 데이터 포인트에서 미분을 한 것이기 때문에 더 많은 차수를 사용할 수록 approximation error가 작아지게 된다. 

#### Learning rate

이때 앞에 있는 learning rate $-n$은 매우 작은 값을 취하게 된다. 이는 앞의 approximation 시에 1차 미분만을 사용하였기 때문에 만약 데이터 포인트에서 멀어지는 변화를 갖게 되면 근사값 오차가 커지게 된다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_8.png?raw=true" width="650" height="400"></p>

Training DB, 현재 파라미터 그리고 그에대한 loss function이 있다. 모든 training data에 대한 loss는 sample loss의 합으로 가정하였기 때문에 위와 같은 식이 도출된다. 이때 각 sample의 수가 고정인 N이라고 하면 평균 gradient로 redefinition 할 수 있다. (Loss 값이 음수임은 변함이 없기 때문) 만약 데이터의 수가 많이 전체에 대한 연산이 불가능 할 경우 랜덤하게 M개의 batch로 평균 gradient를 구한다. 이는 전체에 대한 gradient와 배치에 대한 gradient가 같을 것이라고 기대하는 것이다. 마지막으로 구한 gradient 값과 learning rate를 곱해 update를 진행한다.

**Step, Epoch**<br>1번 update되는 것을 step, 모든 training data를 다 훑으면 epoch이라고 함

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_9.png?raw=true" width="600" height="350"></p>

Deep neural network에서 학습해야 할 파라미터는 (W,b)이며 이는 layer로 구성되어 연결되어 있다. 이를 미분하는 과정은 복잡하기에 Backpropagation Algorithm을 사용한다. 해당 알고리즘은 output layer부터 각 layer 까지 error signal을 구하는 것이다.  첫번째 output layer의 error signal은 먼저 cost를 network 출력 값으로 미분한다. 이는 **loss function은 network 출력단에 해당하는 함수**에 대한 가정 때문이다. 다음으로 activation function의 미분에 입력으로 들어간 값을 대입하여 나온 결과와 element wise 곱을 해준다. 이후 각 layer는 앞에서 전달받은 error signal(about W)과 연산을 통해 계산한다. 

파라미터 갱신을 위해 궁금한것은 각 layer 별로 (W,b)에 대한 gradient(미분값)이다. 이는 앞선 backpropagation 과정에서 구하였는데, bias에 대한 미분값은 error signal 그 자체이고 weight에 대한 미분값은 error signal과 그 네트워크 layer의 입력으로 들어가는 값과의 곱으로 구할 수 있다. 이러한 과정을 통해 편하고 빠르게 파라미터 갱신을 위한 미분을 진행할 수 있다.

### 2.2.1 View-Point 1: Backpropagation

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_10.png?raw=true" width="650" height="400"></p>

앞의 내용에서 말했듯 Loss function은 backpropagation을 만족하는 대표적인 두가지인 mean square error 또는 cross entropy를 쓴다. 그러면 두 loss 중 어떤것이 좋은가에 대한 기준이 되는 두가지 관점이 있는데, 하나는 Bacpropagation 관점이고 다른 하나는 Maximum likelyhood 관점이다. 먼저 Backpropagation 관점에 대한 해석은 아래와 같다.

**Tpye 1: MSE**<br>Input 1이 layer 1개를 거친 후 activation function을 거쳐 output이 0인 NN이 있다고 가정한다. 이후 초기값을 서로 다르게 하여 학습을 진행하는데, 그래프를 보면 초기값을 (0.6, 0.9)로 준 것의 output이 0.09로 (2,2)로 준 것보다 학습이 더 잘 되었음을 확인할 수 있다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_11.png?raw=true" width="650" height="250"></p>

이는 초기값이 다르기 때문인데 이유는 다음과 같다. 먼저 backpropagation의 수식을 보면 항상 activation function의 미분값이 들어가 있음을 알 수 있다. 해당 NN에서 사용한 activation function은 파란 선인 sigmoid이므로 미분한 것의 그래프는 빨간 선과 같다. 그래프를 보면 학습이 잘된 것은 미분값이 어느정도 값이 있는 것임을 알 수 있다. 반대로 학습이 잘 되지 않은 것은 미분값이 0에 가까움을 알 수 있다. 학습을 진행하며 activation function의 미분값이 0에 가깝다는 것은 최종적으로 계산된 gradient 값이 0에 가깝고(항상 activation function의 미분값이 들어가 있기 때문에), 파라미터의 변화량이 미미하다는 것이다.

**Gradient Vanishing**<br>activation function의 미분값은 maximum 1/4 정도 된다. 따라서 만약 layer가 깊게 쌓인 경우, 앞서 설명하였듯 activation function의 미분값이 항상 곱해지기 때문에 (최대)1/4씩 여러번 곱해지다보면 0에 가까워져 입력단에서는 거의 변화가 일어나지 않는 형상이 발생한다. 이러한 현상을 gradient vanishing이라고 한다. 따라서 최근에는 Relu를 activation function으로 사용여 gradient vanishing problem을 어느정도 완화시킨다.

**Tpye 2: Cross Entropy**

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_12.png?raw=true" width="650" height="400"></p>

Cross Entropy에서는 MSE와 다르게 수식상 activation function의 미분값이 사라지게 된다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_13.png?raw=true" width="650" height="400"></p>

따라서 학습을 할 때, 초기값에 둔감하게 반응하게 된다. 

결과적으로 Backpropagation 관점의 해석일 때는 Cross Entropy가 (모두 그런 것은 아니지만) 초기값에 둔감하므로 학습에 좀 더 용이하다는 결론을 내릴 수 있다.

### 2.2.2 View-Point 2: Maximum Likelihood

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_14.png?raw=true" width="650" height="400"></p>

Loss function에 대한 두번째 관점은 Maximum Likelihood이며 이는 네트워크 출력값에 대한 해석이 중요하다. 결국 네트워크의 출력값 $f_{ /theta }(x)$이 정답이랑 가깝길 바라기에 다른 정도를 loss function으로 정의하여 풀었는데, 이를 다르게 해석하면 **네트워크의 출력값이 있을때(given), 원하는 정답이 나올 확률이 높길 바란다 **로 볼 수 있다. 따라서 확률분포에 대한 likelihood가 maximize되고 싶기에 확률분포 모델을 정의하여야 한다. 즉, conditional probability에 대한 모델을 정의해야 하며, 학습은 확률분포를 정의하는 파라미터 $\theta$를 추정하는 과정이 된다. 

> **[예시]** <br>정의한 확률분포 모델이 가우시안이고 표준편차를 무시한다면 theta 2일때 나온 네트워크 출력값은 어떤 가우시안 분포의 평균이라 볼 수 있고, 이와 매핑되는 가우시안 분포를 그릴 수 있게 되며, 이때 training db에 있는 고정된 값 y에 대한 likelihood를 구할수 있게 된다. 만약 학습을 통해 theta 1의 출력값으로 평균값이 바뀌게 된다면 y의 likelihood는 더 큰 값을 가지게 될 것이다. 이러한 관점에서 likelihood가 최대가 되는 point는 평균(출력값)과 y가 같을 때 임을 알 수 있다. (MSE와 똑같은 얘기이나 관점만 확률적으로 바꾼 것이다.) 

이러한 가정에서 Loss function을 보면 -log가 붙은 negative log likelihood임을 알 수 있다. (-)가 붙은 이유는 **probability가 커질수록 loss가 작아져야** 하기 때문이고, log가 붙은 이유는 backpropagation의 제약 조건인 **loss는 각 샘플의 loss의 합**을 만족시키기 위해서이다. 이러한 loss function을 정의하여 찾은 $\theta$는 확률분포 모델을 정의하는 파라미터이기에 결국 확률분포 모델을 찾은 것이라고 볼 수 있다. 이는 확률분포를 통한 샘플링을 할 수 있음을 의미한다. 고전적인 machine learning에서는 고정 입력, 고정 출력이나 이러한 관점에서는 확률 분포를 찾은 것이기 때문에 샘플링(=다양한 출력)이 가능해진다. 이는 autoencoder의 관점에서 중요한데, 한가지 입력에 대해 다양한 출력을 내는 것이 가능해야 하기 때문이다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/autoencoder/autoencoder1_15.png?raw=true" width="650" height="200"></p>

Loss function을 negative log likelihood로 정의하였는데, 이것이 앞에서 이야기한 Backpropagation의 두가지 제약조건을 충족시키는지 알아본다.



https://junstar92.tistory.com/156

BGD -> https://geniewishescometrue.tistory.com/entry/Gradient-Descent, https://light-tree.tistory.com/133

gradient -> https://velog.io/@abrahamkim98/Deep-Learning%EA%B8%B0%EC%B4%88-2.-Loss-Function

확률분포 샘플링 -> https://gils-lab.tistory.com/92

probability vs likelihood -> https://jjangjjong.tistory.com/41
