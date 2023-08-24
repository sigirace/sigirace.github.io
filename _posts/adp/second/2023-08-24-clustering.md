---
layout: single
title:  'ADP 실기 13장 Cluster analysis'
toc: true
categories: [ADP]
tags: [ADP 실기]


---

본 게시물은 군집분석에 대해 소개한다.
{: .notice}

## 1. 군집분석

### 1.1 Concept

> 객체의 유사성을 측정하여 대상집단을 분류하는 통계적 기법으로 종속변수가 없는 비지도 학습

### 1.2 vs 요인분석

- 군집분석: 객체 간의 상이성을 규명하고 군집의 특징을 파악
- 요인분석: 데이터의 유사한 변수를 묶어 다중공선성을 줄이는 목적

### 1.3 종류

- 계층적 군집분석
- 비계층적 군집분석

## 2. 계층적 군집분석

### 2.1 Concept

> n개의 군집으로 시작해 점차 군집의 개수를 줄여나가 군집의 개수를 선택하는 것으로, 군집의 거리를 계산하는 방법에 따라 연결법이 달라짐

### 2.2 종류

- 최단 연결법: 거리행렬에서 거리가 가장 가까운 데이터를 묶어서 군집 형성
- 최장 연결법: 데이터와의 거리를 계산할 때, 최장 거리로 계산
- 평균 연결법: 데이터와의 거리를 계산할 때, 평균 거리로 계산
- 중심 연결법: 두 군집의 거리를 두 군집의 중심 간 거리로 계산
- 와드 연결법: 군집 내 편차들의 제곱합에 근거를 두고 군집화
  - 데이터의 크기가 너무 크지 않다면 주로 와드 연결법 사용
  - 군집 내 편차는 작고 군집 간 편차는 크게 군집화 시키는 것이 정보의 손실(SSE)를 최소화 시킬 수 있음
  - 계산량이 많지만 군집 크기를 비슷하게 만들며 해석력이 좋음

### 2.3 Methods

1. linkage

````
linkage(y, method=‘single’, metric=‘euclidean’)
````

- y: 데이터 프레임 값
- method: single-최단/ complete-최장/ average-평균/ centroid-중심/ ward-와드
- metric: 연결법에 사용되는 거리 방법
  - euclidean, seuclidean(표준화), mahalanobis, chebyshev, cityblock, canberra, minkowski, jaccard, cosine

2. dendrogram

````
dendrogram(Z, orientation=‘top’, labels=None, color_threshold=None, get_leaves=True)
````

- Z: linkage 결과
- orientation: 덴드로그램 시각화 방식
  - top, bottom, left, right

📍 **color threshold**

- `color_threshold`는 계층적 군집분석에서 덴드로그램(Dendrogram)에 사용되는 파라미터로, 클러스터들을 색으로 구분할 때 사용
-  `color_threshold`는 트리에서 클러스터들을 그룹화할 때 어떤 거리를 기준으로 색을 변경할지를 지정하는 값으로, 값보다 더 높은 거리에 있는 클러스터들은 같은 색으로 표시되며, 이를 통해 클러스터들의 계층적 구조를 시각화할 수 있음
-  `color_threshold`를 설정하면 덴드로그램에서 클러스터 간의 유사성을 시각적으로 파악하기 쉬우며, 이를 어떻게 설정하느냐에 따라 클러스터들이 얼마나 세분화되는지 결정할 수 있음
  - 높은 `color_threshold` 값을 선택하면 클러스터들이 더 큰 그룹으로 결합되어 덴드로그램이 더 간단해짐
  - 낮은 `color_threshold` 값을 선택하면 클러스터들이 더 세분화되어 덴드로그램이 더 복잡해짐
- `color_threshold`의 설정은 분석 목적 및 데이터 구조에 따라 다를 수 있으며, 어떤 거리를 시각적으로 강조하고자 하는지에 따라 조정됨
- 일반적으로 데이터 포인트나 클러스터 간의 거리를 고려하여 `color_threshold` 값을 선택하며, 이를 통해 클러스터의 계층적 구조를 이해하고 데이터를 해석하는 데 도움을 줌

3. fcluster

````
fcluster(Z, t, criterion=‘distance’)
````

- Z: linkage 결과
- t: flat clusters 형성할 때 적용하는 임계값, 덴드로그램의 color_threshold와 일치하게 설정하면 그 값에 따른 군집 결과 확인 가능
- criterion
  - inconsistent: 군집의 값이 t보다 작거나 같으면 모든 하위 항목이 동일한 군집에 속함 (=모든 노드가 자체 클러스터에 할당)
  - distance: 각 군집의 관측 값이 t보다 작은 거리를 가지도록 평면 군집을 형성 (=하나로 묶이는 것을 막음)

### 2.4 Implementation

😗 **미국 도시의 범죄율별 계층적 클러스터링**

````python
import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from matplotlib import pyplot as plt
US = pd.read_csv("https://raw.githubusercontent.com/ADPclass/ADP_book_ver01/main/data/USArrests.csv")
US.columns = ['State', 'Murder', 'Assault', 'UrbanPop', 'Rape']
labelList=US.State.tolist()
US.head()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/cl/cl1.png?raw=true" width="250" height="150"></p>

📍 **최단 연결법**

````python
# 최단 연결법
single = linkage(US.iloc[:, 1::], metric ='euclidean', method='single')
# 덴드로그램 그리기
plt.figure(figsize=(10, 7))
dendrogram(single,
    orientation='top',
    labels=labelList,
    distance_sort='descending',
    color_threshold=25, #군집의 수를 설정하는 Height 값 설정
    show_leaf_counts=True)
plt.axhline(y=25, color='r', linewidth=1) 
#Height 값에 따라 선을 그어 적절한 군집 수 설정
plt.show()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/cl/cl2.png?raw=true" width="700" height="400"></p>

- 덴드로그램을 그릴 시, t 값의 기준을 25로 군집화 시켰을 때 6개의 군집이 생김을 예상
- 왼쪽 군집은 다수의 객체를 가지나 오른쪽 3개의 군집은 1개의 객체만을 가짐

📍 **와드 연결법**

````python
# 와드 연결법
ward = linkage(US.iloc[:, 1::], metric ='euclidean', method='ward')
# 덴드로그램 그리기
plt.figure(figsize=(10, 7))
dendrogram(ward,
            orientation='top',
            labels=labelList,
            distance_sort='descending',
            color_threshold=250,
            show_leaf_counts=True)
plt.axhline(y=250, color='r', linewidth=1) 
#Height 값에 따라 선을 그어 적절한 군집 수 설정
plt.show()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/cl/cl3.png?raw=true" width="700" height="400"></p>

- 와드 연결법을 수행할 시, 덴드로그램을 통해 군집을 해석하기 쉬운 장점이 있음

````python
# state마다 어떤 군집에 설정되었는지 확인
assignments = fcluster(ward, 250, 'distance')
assignments
````

````
array([1, 1, 1, 2, 1, 2, 3, 1, 1, 2, 3, 3, 1, 3, 3, 3, 3, 1, 3, 1, 2, 1,
       3, 1, 2, 3, 3, 1, 3, 2, 1, 1, 1, 3, 3, 2, 2, 3, 2, 1, 3, 2, 2, 3,
       3, 2, 2, 3, 3, 2], dtype=int32)
````

````python
US['cluster'] = assignments
US[US.columns.drop('State')].groupby('cluster').mean()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/cl/cl4.png?raw=true" width="450" height="200"></p>

- 군집간의 특징을 위와 같이 파악할 수 있음

## 3. 비계층적 군집분석

### 3.1 Concept

> 계층적 군집분석은 순차적이지만 비계층적 군집분석은 랜덤하게 군집을 묶어가는 알고리즘을 사용하며, 거리 계산의 알고리즘에 따라 군집분석의 명칭이 달라짐

## 4. K-means

### 4.1 Concept

> 속성의 개수가 적은 단순한 데이터에 많이 활용되는 알고리즘, 각 클러스터와 거리 차이의 분산을 최소화 하는 방식으로 작동

### 4.2 Algorithm

1. 초기값 설정
   - 군집의 개수인 k의 초기값을 미리 설정해야 함
   - 임의의 k개의 점이 군집의 중심이 됨
2. 클러스터 설정
   - 데이터로부터 각 클러스터들의 중심까지의 유클리드 거리를 게산해 가장 가까운 클러스터를 찾아 데이터를 할당
3. 클러스터 중심 재조정
   - 클러스터의 중심을 각 클러스터에 있는 데이터들의 무게중심 값으로 재설정
4. 종료조건
   - 2~3을 반복
   - 알고리즘의 중심 변화가 작을 때 중지

### 4.3 Properties

- 알고리즘이 쉽고 간단
- 변수가 많을 경우 군집화 정도가 떨어짐 ☞ 차원축소 고려
- 군집수 K를 판단하여 적용해야 함

### 4.4 Optimal cluster number

1. 콜린스키 하라바츠 스코어
   - 모든 클러스터에 대한 클러스터간 분산과 클러스터 내 분산의 합의 비율
   - 점수가 높을수록 좋은 성능
2. 엘보우
   - 클러스터 내 오차제곱합(SSE)을 클러스터 개수마다 비교
   - 반목문을 통해 K를 늘려가며 계산
   - SSE가 급격히 줄어드는 부분(=기울기가 소실되는 구간)을 elbow로 판단하고 최적의 클러스터 개수로 지정

### 4.5 Implementation

😗 **Iris 데이터의 분류**

````python
# 필요한 모듈
import pandas as pd 
from sklearn.cluster import KMeans
# 데이터 로드
iris = pd.read_csv("https://raw.githubusercontent.com/ADPclass/ADP_book_ver01/main/data/iris.csv")
X = iris.drop('target',axis=1)
X
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/cl/cl5.png?raw=true" width="500" height="250"></p>

📍 **Initial K를 찾기 위한 실험**

````python
# 클러스터별 콜린스키 하라바츠 결과 비교
from sklearn.metrics import calinski_harabasz_score
for k in range(2, 10):
    kmeans_model = KMeans(n_clusters=k, random_state=1).fit(X)
    labels = kmeans_model.labels_
    print(calinski_harabasz_score(X, labels))
````

````
513.3038433517568
560.3999242466402
529.1207190840455
494.0943819140987
471.65021087892444
448.33207182773526
436.92028527534933
407.12343463976123
````

- K=3일때 가장 높은 score

````python
import matplotlib.pyplot as plt
def elbow(X):
    sse=[]
    for i in range(1, 11):
        km = KMeans(n_clusters=i, random_state=1)
        km.fit(X)
        sse.append(km.inertia_)

    plt.plot(range(1,11), sse, marker='o')
    plt.xlabel('The Number of Clusters')
    plt.ylabel('SSE')
    plt.show()
    print(sse)
elbow(X)
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/cl/cl6.png?raw=true" width="700" height="400"></p>

````
[680.8244, 152.36870647733903, 78.94084142614602, 57.34540931571816, 46.535582051282056, 39.18020672938385, 34.36574278696132, 30.207410380445552, 28.250910589410594, 26.604622627348977]
````

- K값이 2에서 3으로 갈 때에 기울기 소실이 발생

👀 **K=3이 최적의 군집수**

````python
#최적의 k로 K-Means 군집화 실행
km = KMeans(n_clusters =3, random_state=1)
km.fit(X)
# 할당된 군집을 iris 데이터에 추가
new_labels = km.labels_
iris['cluster'] = new_labels
iris[iris.columns.drop('target')].groupby(['cluster']).mean()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/cl/cl7.png?raw=true" width="400" height="150"></p>

- 군집의 결과 확인을 위해 ANOVA 분석을 수행하는 것이 좋음
- 시각화도 쉽게 확인할 수 있는 방법

📍 **시각화 비교**

````python
# k-means 시각화 
# 군집결과 시각화
import seaborn as sns
import matplotlib.pyplot as plt
sns.pairplot(iris,
            diag_kind='kde',
            hue="cluster", 
            corner =True, 
            palette='bright')
plt.show()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/cl/cl8.png?raw=true" width="900" height="600"></p>

````python
# 원본 데이터 iris target 시각화
import seaborn as sns
import matplotlib.pyplot as plt
sns.pairplot(iris.drop(columns=['cluster']),
            diag_kind='kde',
            hue="target",
            corner =True, 
            palette='bright')
plt.show()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/cl/cl9.png?raw=true"  width="900" height="600"></p>

- 시각화를 통해 차이가 없음을 확인

## 5. 혼합분포 군집분석

### 5.1 Concept

> 데이터가 K개의 모수적 모형의 가중합으로 표현되는 모집단 모형으로부터 나왔다는 가정 하에 군집분석을 진행

- k개의 각 모형은 군집이며 데이터는 이중 어느 모형에서 나왔을 확률이 높은지에 따라 군집의 분류
- 공분산 행렬, likelihood 개념 사용
- k-means는 원형으로 군집화된 데이터에 적합
- DBSCAN은 반달 형태의 데이터에 적합(실생활에 거의 없음)
- 대부분의 데이터는 정규분포의 형태를 지니기에 혼합분포 군집분석이 적합

### 5.2 Pros and cons

1. 장점
   - k-means 보다 통계적으로 엄밀한 결과 (확률분포)
   - 군집을 몇개의 모수로 표현 가능
   - 서로 다른 크기나 모양의 군집을 찾을 수 있음
2. 단점
   - 군집의 크기가 너무 작으면 추정의 정도가 떨어짐
   - 데이터가 커지면 EM 알고리즘의 시간/계산 비용이 증가
   - 이상치에 민감하기에 사전 전처리 필요
   - 유형들의 분포가 정규분포와 차이가 크면 결과가 좋지 못함

### 5.3 EM Algorithm

1. 초기값 설정: 필요한 모수에 대해 초기값 설정
2. E: 잠재변수 Z의 기대치를 계싼 (= X가 특정 군집에 속할 확률 계산)
3. M: 잠재변수 Z의 기대치를 이용해 파라미터를 추정 (계산된 확률을 통해 모수를 재추정)
4. 반복 정지: 수렴조건이 만족될 때 까지 E와 M을 반복
   - 수렴조건 - MLE

### 5.4 Parameters

````python
class sklearn.mixture.GaussianMixture(n_components=1, *, covariance_type=‘full’, 
tol=0.001, reg_covar=1e-06, max_iter=100, n_init=1, init_params=‘kmeans’, 
weights_init=None, means_init=None, precisions_init=None, random_state=None, 
warm_start=False, verbose=0, verbose_interval=10)
````

- n_complements: 예상 군집 수 설정
- max_iter: 수행할 EM 반복 횟수

### 5.5 Implementation

😗 **Iris 데이터의 혼합분포 군집**

````python
# 필요한 모듈
import pandas as pd
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.mixture import GaussianMixture
# 데이터 업로드
iris = pd.read_csv("https://raw.githubusercontent.com/ADPclass/ADP_book_ver01/main/data/iris.csv")
df = iris.drop('target',axis=1)
# 데이터 스케일링
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)
# 가우시안 혼합모델 구축
gmm = GaussianMixture(n_components =3)
gmm.fit(df_scaled)
gmm_labels = gmm.predict(df_scaled)
gmm_labels
````

````
array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 0, 2, 0, 2, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
````

- 혼합분포 군집분석은 정규분포 기반의 군집분석이므로 데이터를 스케일링하여 모델학습이 필요

````python
df['gmm_cluster'] = gmm_labels
# 군집의 변수별 통계량 확인
clusters = [0, 1, 2]
df.groupby('gmm_cluster').mean()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/cl/cl10.png?raw=true"  width="400" height="150"></p>

````python
# 군집결과 시각화
import seaborn as sns
import matplotlib.pyplot as plt
sns.pairplot(df,
            diag_kind='kde',
            hue="gmm_cluster",
            corner =True, 
            palette='bright')
plt.show()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/cl/cl11.png?raw=true"  width="900" height="600"></p>
