---
layout: single
title:  'Graph Neural Networks: Link Prediction (part2)'
toc: true
categories: [Graph Neural Network]
tags: [GNN]

---

이번 포스팅에서는 Graph Neural Network(=GNN)의 link prediction에 대해 알아본다. 해당 포스트는 GNN의 기본적인 개념에 대한 이해를 필요로 한다.
{: .notice}

## 1. Introduction

실생활의 많은 문제들이 노드와 엣지의 네트워크로서 모델링 될 수 있기 때문에, 그래프 신경망은 문제해결을 위한 강력한 접근 방식을 제공한다. 이를 활용한다면 효과적으로 학습이 가능하기에 일반적인 ML 알고리즘들이 실패했던 복잡한 문제들을 풀 수 있다. 이러한 맥락에서 GNN의 첫번째 포스트는 네트워크에서 엔티티를 분류하거나 연속적인 속성을 예측할때의 장점들에 대해 이야기 하였다. 그러나 만약 노드들 간의 관계를 예측하는 것이라면 어떨까?

📍**실제 사례**

> 기업은 그들이 제공하는 상품에 대한 고객의 만족도를 예측하고, 이를 통해 고객에게 상품을 제안한다.<br>SNS는 두 사용자간의 관계를 예측하여 새로운 관계를 맺는 것을 제안한다.<br>화학자들은 새로운 약물을 발견하거나 여러 약물을 복용할 때, 예상치 못한 부작용을 피하기 위해 분자간의 상호작용을 연구한다.

GNN의 이전 포스트에서는 homogeneous graphs(=단일 유형의 노드만 존재하는 그래프)만을 고려했다. 그런데 위 예시에서 기업이 다양한 고객에게 다양한 유형의 제품을 제공해야 하는 것 처럼 네트워크가 다른 유형의 노드를 포함한다면 어떨까? 이러한 네트워크를 일반적으로 heterogeneous graph라고 한다. 이번 포스팅에서는 heterogeneous graphs에 대한 link prediction을 위한 GNN을 구축하는데 중점을 둔다. 이를 설명하기 위해 사용자가 동영상에 부여할 등급을 예측하는 추천 활용 사례를 사용할 것이며, 그래프 기반 모델과 협업 필터링간의 비교를 통해 GNN의 이점을 설명할 것이다.

👀 **알게 될 것**

> SAGEGraph는 무엇이며 GCN의 접근 방식을 얼마나 개선하는가?<br>GNN 모델을 사용하여 link prediction은 어떻게 수행되는가?<br>GNN 모델을 실제 문제에 어떻게 적용할 수 있는가?<br>

## 2. Link Predcition

이번 chatper에서는 실제 문제에 적용하기 위해 아래 세가지 이론을 알아보는 것을 목표로 한다

- Link prediction을 위한 GNN 방법론 중 하나인 GraphSAGE
- GNN 모델을 확장하여 heterogeneous graphs를 처리하는 방법
- Link prediction을 위한 노드 임베딩의 접근 방식

### 2.1 GraphSAGE

#### 2.1.1 vs GCN

먼저 GCN에서 GraphSAGE로 방법론의 전환 이유에 대해 알아본다. GCN은 학습 프레임워크로 인해 아래의 어려움을 겪고 있다.

GCNs suffer from several issues caused by their very learning framework:

1. **대규모 네트워크 학습**: GCN에서 임베딩을 학습시키기 위해선 모든 노드의 정보가 필요하다. 따라서 모델을 배치 단위로 학습할 수 없고, 이는 대규모 데이터 처리시 한계가 존재한다.
2. **신규 노드의 일반화**: GCN은 고정된 단일 그래프를 가정한다. 그러나 신규 노드는 빠르게 생성되기 때문에 실제 애플리케이션에 적용하는데 한계가 존재한다. (예: Twitter의 게시물, YouTube의 비디오 등)

즉, GCN은 실제 어플리케이션에 적용하기 실용적이지 못하다. 반면 GraphSAGE는 GCN과 동일한 수학적 원리를 바탕으로 이러한 한계점들을 개선하였다. 

#### 2.1.2 GraphSAGE algorithm

GraphSAGE는 각 노드의 개별 임베딩을 학습하는 것 대신, 이웃하는 노드의 특징을 샘플링(sampling)과 집계(aggregating)함으로서 임베딩을 생성하는 함수를 학습한다. 

1. **Sampling**: 모델은 주어진 노드의 전체 이웃들을 학습하는 것 대신, 고정된 크기의 이웃 집합을 균일하게 샘플링한다.
2. **Aggregating**: 노드는 그들의 이웃 정보를 함수를 통해 집계한다. (논문에서는 세가지 집계함수를 다룸)

#### 2.1.3 Aggregator

- **Mean aggregator**

  이웃 노드 벡터들의 평균으로 집계하는 방식으로, 간단하고 효율적이며 논문에서 수행된 실험에서 좋은 성과를 내었다.

- **LSTM aggregator**

  LSTM 아키텍처의 표현 방식을 활용할 수 있는 잠재력을 가지고 있다. 그래프를 LSTM에 적용하기 위해 노드들을 임의의 순열로 나열해야 한다.

- **Pooling aggregator**

  Fully Connected Neural Network을 사용하는 방식이다. 이웃 노드들의 벡터들은 fc 연산(=transformation)및 max pooling을 거친 후 집계된다. 이 또한 논문에서 수행된 실험에서 좋은 성과를 내었다.

Sampling과 Aggregating은 모든 노드에 대해 K회 반복되며, 일반적으로 K=2이면 충분한 것으로 알려져있다. 이러한 수행이 반복되면 노드는 그래프의 더 먼 이웃에서 점점 더 많은 정보를 얻게 될 것이다. 아래는 K=2일때의 프로세스를 보여준다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/gnn/link_predict/lp1.png?raw=true" width="500" height="300"></p>

Aggregating에서 사용된 가중치는 노드가 아닌 iteration k에 국한된다. 그러므로 아직 나타나지 않은 노드들에 대한 일반화를 가능하게 한다.

**요약하면, GraphSAGE는 이웃 노드들을 샘플링하여 GCN을 구성한 것으로 간주할 수 있다.**

### 2.2 Heterogeneous Graphs

앞서 Heterogeneous Graph는 다른 유형의 노드를 포함한 그래프라고 소개하였다. 이를 예제와 함께 설명하고, 임베딩을 구성하는 방법에 대해 알아본다.

#### 2.2.1 Architecture

User와 Movie 그리고 User가 Movie를 평가한 Rating 및 Movie의 Title이 있다고 가정하면, 아래와 같은 설계를 할 수 있다.

- **Goal**: 특정 사용자가 최신 영화에 부여할 수 있는 Rating을 예측한다. 이는 가장 높은 Rating의 Movie를 제안하는 추천시스템으로 활용할 수 있다.
- **Modeling**: User 노드와 Movie 노드가 있는 그래프로 모델링 할 수 있다. 또한 User가 Movie에 Rating을 지정한 경우 간선으로 연결될 수 있다.
- **Task**: Modeling을 통해 생성된 User와 Movie 노드 간 연결인 Rating을 예측한다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/gnn/link_predict/lp2.png?raw=true" width="500" height="400"></p>

#### 2.2.2 Library

이러한 설계에서 Graph는 User와 Movie 두가지 유형의 노드를 포함한 Hetrogeneous Graph이다. 따라서 모델은 두 노드에 대한 임베딩을 동시에 학습할 수 있어야 한다. 이를 위한 방법 중 하나는 Homogeneous Graph에 적용될 수 있는 GNN 모델을 가져와 각 유형에서 개별적으로 작동하도록 하는 것이다. 이는 아래 그림에서 자세히 설명되어 있다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/gnn/link_predict/lp3.png?raw=true" width="500" height="400"></p>

이는 PyTorch Geometric에 구현되어있는 기본 아키텍처이다. 라이브러리는 모든 GNN 모델을 Heterogeneous Graph에 적용될 수 있도록 변환하는 기능을 제공한다. 자세한 내용은 [여기](https://pytorch-geometric.readthedocs.io/en/latest/notes/heterogeneous.html)에서 확인할 수 있다.

### 2.3 Link Prediction

마지막으로 구성한 노드의 임베딩을 통해 간선인 Rating을 예측(Link predcition)하는 두가지 방법을 알아본다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/gnn/link_predict/lp4.png?raw=true" width="500" height="300"></p>

#### 2.3.1 Linear layer

대표적인 방법은 User와 Movie의 임베딩 벡터를 concatenate시킨 후 Rating을 예측하는 linear layer를 구성하는 것이다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/gnn/link_predict/lp5.png?raw=true" width="500" height="300"></p>

#### 2.3.2 The other alternative consist of other

- 만약 두 임베딩의 차원이 같고 출력이 1차원이라면 단순한 dot product를 계산할 수 있다. 이는 두 노드 사이에 간선이 있는지를 파악하는 유형으로 sns에서 친구추천에 사용하는 방법이다.
-  Learning a trainable matrix *W = (W¹, …, W^k)*.