---
layout: single
title:  'ADP 실기 8장 KNN Clustering'
toc: true
categories: [ADP]
tags: [ADP 실기]


---

본 게시물은 KNN Clustering에 대해 소개한다.
{: .notice}

## 1. KNN Classifier

### 1.1 Concept

> 새로운 데이터에 대해 가장 가까운 K개의 데이터의 군집을 확인하고 분류

- 유클리디안 거리: 데이터간 거리 측정을 위해 사용
- Noise: K의 개수가 작아 경계가 뚜렷하지 않은 경우 발생하는 오류

### 1.2 Parameters

````python
class sklearn.neighbors.KNeighborsClassifier(n_neighbors=5, *, weights=‘uniform’, 
algorithm=‘auto’, leaf_size=30, p=2, metric=‘minkowski’, metric_params=None, 
n_jobs=None) 
````

- n_neighbors: K
- weight: uniform-모든 데이터들이 동등한 가중치, distance-거리상 가까운 데이터가 큰 가중치를 가짐
- algorithm: 거리계산을 위한 알고리즘, 트리 알고리즘을 사용
- leaf_size: BallTree, KDTree에 전달된 리프의 크기
- metric: 거리 계산 메트릭

📍 **KNN에서 Tree 구조를 사용하는 이유**

>  데이터가 클 경우 매번 거리계산을 수행하기 부담스러움, 따라서 트리 구조로 데이터를 정렬한다면 가까운 데이터를 빠르게 찾을 수 있음

### 1.3 Methods

- fit(X,y)
- get_params
- kneighbors([X, n_neighbors, return_distance])
  - X: 데이터(n_queries, n_features), 입력하지 않으면 모든 데이터에 대해 수행
  - n_neighbors: 이웃의 개수, 입력하지 않을 경우 생성자의 K
  - return_distance: 거리 반환 여부
- score(X, y[,sample_weight]): 정확도

### 1.4 Implementation

😗 **데이터 불러오기**

````python
import pandas as pd
liver = pd.read_csv("https://raw.githubusercontent.com/ADPclass/ADP_book_ver01/main/data/indian_liver_patient.csv")
print(liver.Dataset.unique())
liver.head()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/knn/knn1.png?raw=true" width="800" height="200"></p>

````python
# 성별 분류 전처리
import numpy as np
liver.Gender = np.where(liver.Gender=='Female',0,1)
liver.head()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/knn/knn2.png?raw=true" width="800" height="150"></p>

````python
# 결측치 확인
print(liver.isna().sum())
````

````
Age                           0
Gender                        0
Total_Bilirubin               0
Direct_Bilirubin              0
Alkaline_Phosphotase          0
Alamine_Aminotransferase      0
Aspartate_Aminotransferase    0
Total_Protiens                0
Albumin                       0
Albumin_and_Globulin_Ratio    4
Dataset                       0
````

````python
# 결측치 처리
liver.dropna(axis=0, inplace=True)
print(liver.isna().sum())
````

````
Age                           0
Gender                        0
Total_Bilirubin               0
Direct_Bilirubin              0
Alkaline_Phosphotase          0
Alamine_Aminotransferase      0
Aspartate_Aminotransferase    0
Total_Protiens                0
Albumin                       0
Albumin_and_Globulin_Ratio    0
Dataset                       0
````

````python
# train-test 분리
from sklearn.model_selection import train_test_split
x=liver[liver.columns.difference(['Dataset'])]
y=liver['Dataset']
train_x, test_x, train_y, test_y = train_test_split(x,y,stratify=y, 
train_size=0.7, random_state=1)
print(train_x.shape, test_x.shape, train_y.shape, test_y.shape)
````

````
(405, 10) (174, 10) (405,) (174,)
````

````python
# 모델링
from sklearn.neighbors import KNeighborsClassifier
clf=KNeighborsClassifier(n_neighbors=15, weights='uniform')
clf.fit(train_x, train_y)
````

````python
# 평가
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
pred=clf.predict(test_x)
test_cm=confusion_matrix(test_y, pred)
test_acc=accuracy_score(test_y, pred)
test_prc=precision_score(test_y, pred)
test_rcll=recall_score(test_y, pred)
test_f1=f1_score(test_y, pred)
print(test_cm)
print('\n')
print('정확도\t{}%'.format(round(test_acc*100,2)))
print('정밀도\t{}%'.format(round(test_prc*100,2)))
print('재현율\t{}%'.format(round(test_rcll*100,2)))
````

````
[[106  18]
 [ 39  11]]
정확도	67.24%
정밀도	73.1%
재현율	85.48%
````



## 2. KNN Regressor

### 2.1 Concept

> 특정 X에서 직선을 그려 가까운 K개수 만큼의 데이터를 구해 평균을 취하고, 이들을 연결하여 회귀선을 그림

- 단순 평균의 집합일 뿐이기에 종속변수에 대한 회귀계수를 확인 할 수 없음
- 주로 시계열에서 사용됨

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/knn/knn3.png?raw=true" width="600" height="400"></p>

### 2.2 Parameters

````python
class sklearn.neighbors.KNeighborsRegressor(n_neighbors=5, *, 
weights=‘uniform’, algorithm=‘auto’, leaf_size=30, p=2, 
metric=‘minkowski’, metric_params=None, n_jobs=None)
````

- classifier와 동일

### 2.3 Methods

- classifier와 동일

### 2.4 Implementation

😗 **데이터 불러오기**

````python
import numpy as np
# 임의의 샘플데이터 생성하기
np.random.seed(0)
X = np.sort(5 * np.random.rand(400, 1), axis=0)
T = np.linspace(0, 5, 500)[:, np.newaxis]
y = np.sin(X).ravel()
print(X[:10])
print(T[:10])
print(y[:10])
````

````
[[0.02347738]
 [0.05713729]
 [0.05857042]
 [0.06618429]
 [0.08164251]
 [0.08214815]
 [0.09260897]
 [0.093949  ]
 [0.09596599]
 [0.10053773]]
[[0.        ]
 [0.01002004]
 [0.02004008]
 [0.03006012]
 [0.04008016]
 [0.0501002 ]
 [0.06012024]
 [0.07014028]
 [0.08016032]
 [0.09018036]]
[0.02347522 0.05710621 0.05853694 0.06613598 0.08155185 0.08205579
 0.09247665 0.09381086 0.09581876 0.10036845]
````

````python
# 타깃데이터에 노이즈 추가하기
y[::1] += 1 * (0.5 - np.random.rand(400))
````

````python
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(X,y,train_size=0.7, 
random_state=1)
print(train_x.shape, test_x.shape, train_y.shape, test_y.shape)
````

````
(280, 1) (120, 1) (280,) (120,)
````

````python
from sklearn.neighbors import KNeighborsRegressor
knn_uni = KNeighborsRegressor(n_neighbors=20, weights='uniform')
knn_dis = KNeighborsRegressor(n_neighbors=20, weights='distance')
knn_uni.fit(train_x, train_y)
knn_dis.fit(train_x, train_y)
````

````python
uni_pred=knn_uni.predict(test_x)
dis_pred=knn_dis.predict(test_x)
from sklearn.metrics import mean_squared_error, mean_absolute_error, 
mean_squared_error
import pandas as pd
import numpy as np
preds = [uni_pred, dis_pred]
weights = ['uniform', 'distance']
evls = ['mse', 'rmse', 'mae']
results=pd.DataFrame(index=weights,columns=evls)
for pred, nm in zip(preds, weights):
 mse = mean_squared_error(test_y, pred)
 mae = mean_absolute_error(test_y, pred)
 rmse = np.sqrt(mse)
 
 results.loc[nm]['mse']=round(mse,2)
 results.loc[nm]['rmse']=round(rmse,2)
 results.loc[nm]['mae']=round(mae,2)
results
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/knn/knn4.png?raw=true" width="300" height="100"></p>

````python
import matplotlib.pyplot as plt
plt.figure(figsize=(8,5))
for i, weights in enumerate(["uniform", "distance"]):
 knn=KNeighborsRegressor(n_neighbors=20, weights=weights)
 
 y_ = knn.fit(X, y).predict(T)
 
 plt.subplot(2, 1, i + 1)
 plt.scatter(X, y, color="darkorange", label="data")
 plt.plot(T, y_, color="navy", label="prediction")
 plt.axis("tight")
 plt.legend()
 plt.title("KNeighborsRegressor (k = %i, weights = '%s')" % (20, weights))
plt.tight_layout()
plt.show()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/knn/knn5.png?raw=true" width="800" height="400"></p>
