## Lora



## 0. Abstract

중요한 NLP 패러다임은 일반적인 도메인 데이터에서의 대규모 pretraining과 특정한 태스크 또는 도메인에서의 적용으로 구성된다. 대규모 모델을 pre-train 할 때, 모델의 모든 파라미터를 재학습하는 것은 실행하기 어렵다. 예시로 GPT-3 175B를 사용할 경우 downtask 마다 175B의 파라미터를 fine-tuned 수행하여야 하는데, 이는 엄청난 비용을 발생시킨다. 제안한 Low-Rank Adaptation (LoRA)는 pretrained model의 가중치를 고정하고, Transformer 구조의 각 layer에 학습 가능한 rank decomposition matrices를 삽입하여 downstream task에서의 학습가능한 파라미터 수를 크게 줄인다. 이는 Adam을 사용해 fine tuning한 GPT-3 175B와 비교하여, LoRA는 parameter를 10,000배, GPU의 메모리 사용량을 3배 줄일 수 있다. LoRA는 더 적은 parameter를 가지고 있음에도 불구하고, finetuning model인 RoBERTa, DeBERTa, GPT-2, GPT-3과 동등하거나 더 나은 성능을 보인다. 본 논문은 language model adaptation(언어 모델 적응, 학습)에서의 rank-deficiency를 경험적 조사로 제공하여 LoRA의 효능을 입증한다. 마지막으로 LoRA를 PyTorch 모델과 통합하기 쉽게 하는 패키지를 공개하며, RoBERTa, DeBERTa, 그리고 GPT-2에 대한 구현 및 모델 체크포인트를 https://github.com/microsoft/LoRA에서 확인할 수 있다.

📍 language model adaptation

- 거대한 코퍼스에 모델을 사전학습시키고, downstream task에 대해 finetuning하는 transfer learning을 수행하는 것



## 1. Introduction



[1]

NLP에서의 많은 애플리케이션은 하나의 대규모 pre-trained language model을 다수의 downstream에 적용하는것에 의존한다. 이는 보통 pre-trained model의 parameter를 모두 업데이트하는 fine-tuning을 통해 이루어진다. Fine tuning의 주요한 단점은 새로운 model이 원래의 model만큼 많은 parameter를 가지고 있다는 것이다. Parameter가 많은 대규모 model이 몇개월마다 학습됨에 있어, 이러한 단점은 GPT-2, RoBERTa 등의 모델에서는 단순히 불편함이었으나, GPT-3와 같이 175B의 학습 parameter를 가진 모델에서는 크리티컬한 배포 문제를 야기한다.

[2]

많은 연구자들은 일부 parameter를 학습시키거나 새로운 작업을 별도의 모듈에서 학습시키는 방식으로 이를 완화하고자 했다. 이를통해 각 작업마다 pre-trained model 외에 추가로 작은 수의 특정 parameter만을 불러오고 저장하면 되므로, 배포 시 운영 효율성을 크게 향상 시킬 수 있다. 그러나 기존 기술은 모델 깊이를 확장하여 추론 지연을 야기하거나 모델의 사용 가능한 시퀀스 길이를 줄이게 된다. 더하여 이러한 방법은 fine-tuning 기준을 충족시키지 못해 효율성과 품질 사이의 trade-off를 초래한다.

[3]

본 논문은 학습된 과도한 parameter 모델이 사실은 저차원에 위치하고 있다는 것을 보여주는 연구에서 영감을 받아 model의 학습 동안의 가중치의 변화 또한 "intrinsic rank"를 가지고 있다고 가설을 세웠으며, 이는 논문의 핵심인 Low-Rank Adaption(LoRA) 접근법으로 이어진다. LoRA는 학습 과정 동안 dense layer의 가중치를 직접 변경하는 대신, 해당 layer의 변화를 나타내는 rank decomposition matrices를 최적화함으로써 간접적으로 model의 행동을 조정한다. 예를들어 GPT-3 175B의 경우 전체 rank가 12,288로 높은 경우에도 매우 낮은 랭크(하나 또는 두개)만으로 충분하기 때문에, LoRA가 저장공간 및 효율성 측면에서 모두 효과적이라고 볼 수 있다.

[4]

LoRA 프로세스의 여러 가지 주요 장점은 아래와 같다.

- pre-trained model은 공유를 통해 다양한 소규모 LoRA 모듈을 구축하는 데 사용될 수 있다. 또한 공유된 모델을 고정하고, 그림 1의 행렬 A와 B를 교체하는 방식을 통해 효율적으로 task를 전환할 수 있으며, 저장소의 크기와 task 변경시 오버헤드를 줄일 수 있다.
- LoRA는 대부분의 parameter에서 gradient를 계산하거나 optimzer의 상태를 유지할 필요가 없으므로 학습을 더 효과적으로 만들고 하드웨어 진입장벽을 3배 가까이 줄인다. 대신 사용하는 더 작은 low-rank matrices만을 최적화 한다.
- 단순한 선형 설계를 통해 배포된 low-rank matrices를 고정된 weight와 병합할 수 있게 하며, 이를 통해 fully fine-tuned model에 비교하여 추론 지연을 야기하지 않는다.
- LoRA는 이전의 많은 방법들과 독립적이므로 결합되어 사용될 수 있다.



## 2. Problem Statement

[1]

본 논문의 제안은 훈련 목표에 구애받지 않는 반면, 동기부여 사례로서 언어 모델링에 초점을 맞춘다. 아래는 언어 모델링 문제와 특히 특정 프롬프트가 주어졌을 때 조건부 확률의 최대화에 대한 간략한 설명이다.

[2]

Parameter로 $\Phi$를 사용하는 pre-trained autoregressive language model $P_{\Phi}(y \mid x)$이 주어졌다고 가정한다. 예를들어 GPT와 같이 Transformer 구조를 기반으로 구성된 $P_{\Phi}(y \mid x)$는 일반적으로 다양한 작업을 수행할 수 있다. 이 pre-trained model을 요약, 기계독해(MRC) 그리고 자연어를 SQL로 변환시키는 NL2SQL등 특정 downstream으로 학습시키는 것을 생각해보자. 각 downstream task는 context-target 쌍으로 구성된 $Z=\{(x_i, y_i)\}_{i=1,...,N}$을 학습시키는 것으로 나타낼 수 있으며, 이때 $x_i, y_i$는 token의 sequence이다. 예를들어 NL2SQL에서 $x_i$는 자연어로 작성된 쿼리이고, $y_i$는 그로부터 생성된 SQL이다. 또한, 요약에서 $x_i$는 문서 혹은 기사이고 $y_i$는 그에 대한 요약이다. Full fine-tuning 동안 모델은 pre-trained model의 weight인 $\Phi_0$으로 초기화되며, 조건부 언어 모델의 목적함수를 최대화하는 방향으로 gradient를 반복적으로 $\Phi_0 + \Delta \Phi$와 같이 업데이트한다.
$$
\underset{\Phi}{\text{max}} \sum_{(x,y) \in Z} \sum^{\mid y\mid}_{t=1} log (P_{\Phi}(y_t \mid x,y_{<t}))
$$


Full fine-tuning의 가장 중요한 단점중 하나는 각 downstrem task마다 각기 다른 parameter인 $\Delta \Phi$(이는 $\Phi$와 차원이 같음)를 학습해야한다는 것이다. 그러므로 만약 pre-trained model이 175B parameter($\Phi$)를 보유한 GPT와 같이 매우 크다면, 저장 및 배포가 실현 불가능할 만큼 어렵게 된다.

[3]

본 논문에서 우리는 적용한다 parameter에 효율적인 접근을 특정 작업에 특화적인 파라미터를  본 논문에서는 parameter의 변화량 $\Delta \Phi$를 $\Theta$라는 더 작은 parameter로 인코딩하여 효율적인 접근을 적용한다. 여기서 $\Delta \Phi = \Delta \Phi(\Theta)$는 $\Theta$에 의해 결정되는 parameter 변화량을 의미하며, $\Theta$의 크기는 pre-trained model의 초기 parameter인 $\Phi_0$에 비해 훨씬 작다. 이로써 $\Delta \Phi$를 찾는 작업은 더 작은 차원인 $\Theta$를 최적화 하는 작업으로 바뀌게 된다.
$$
\underset{\Phi}{\text{max}} \sum_{(x,y) \in Z} \sum^{\mid y \mid}_{t=1} log(p_{{\Phi_0} + \Delta \Phi(\Theta)}(y_t \mid x,y_{<t}))
$$


뒤의 세션에서, $\Delta \Phi$를 인코딩하기 위한 low-rank 표현을 제시하며 이는 계산 그리고 저장의 효율성을 모두 갖추고 있다. 예를들어 pre-trained model이 GPT-3 175B일 때, 학습될 parameter의 크기 $\mid \Theta \mid$는 원래의 크기 $\mid \Phi_0 \mid$의 0.01% 수준이다.



## 3. Aren't Existing Solutions Good Enough?

The problem we set out to tackle is by no means new.

- 본 논문에서 해결하고자 하는 문제는 새로운 것이 아니다.

Since the inception of transfer learning, dozens of works have sought to make model adaptation more parameter- and compute-efficient.

- Transfer learning의 시작부터, 여러 연구들은 모델의 학습을 parameter, 계산 측면에서 효율적으로 만들고자 시도했다.



Using language modeling as an example, there are two prominent strategies when it comes to efficient adaptations: adding adapter layers (Houlsby et al., 2019; Rebuffi et al., 2017; Pfeiffer et al., 2021; R¨uckl´e et al., 2020) or optimizing some forms of the input layer activations (Li & Liang, 2021; Lester et al., 2021; Hambardzumyan et al., 2020; Liu et al., 2021). 



- Language model을 예로들자면, 두 가지의 저명한 전략들이 있다 효율적인 학습에 대해
- adapter layer를 추가하는것 또는 
- input layer의 최적화하는것 몇 input 형태를



언어 모델링을 예로 들 때, 효율적인 적응에 있어서 두 가지 주요 전략이 있습니다: 어댑터 레이어 추가하기 (Houlsby et al., 2019; Rebuffi et al., 2017; Pfeiffer et al., 2021; R¨uckl´e et al., 2020) 또는 입력 레이어 활성화의 일부 형태를 최적화하기 (Li & Liang, 2021; Lester et al., 2021; Hambardzumyan et al., 2020; Liu et al., 2021). 





However, both strategies have their limitations, especially in a large-scale and latency-sensitive production scenario.



그러나, 두 전략 모두 대규모 및 대기 시간에 민감한 생산 시나리오에서는 특히 한계를 가지고 있습니다.
