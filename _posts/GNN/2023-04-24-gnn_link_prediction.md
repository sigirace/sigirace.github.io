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

- Link prediction을 위한 몇가지 이론 중 GNN layer가 사용되는 GraphSAGE
- GNN 모델을 확장하여 heterogeneous graphs를 처리하는 방법
- Link prediction을 위한 노드 임베딩의 접근 방식

