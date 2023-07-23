---
layout: single
title:  'ADP 실기 4장 머신러닝 프로세스'
toc: true
categories: [ADP]
tags: [ADP 실기]

---

본 게시물은 평가함수와 머신러닝 기초 예제에 대해 소개한다.
{: .notice}

## 1. 평가 함수

### 1.1 회귀 분석

📍 **MAE**

- 절대값 차이
- 에러의 크기를 그대로 반영 ☞ 이상치에 영향을 받음

````python
from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y_test, y_pred)
````

📍 **MSE**

- 제곱합 평균 ☞ 실측과 예측 차이의 면적과 동일
- 특이값이 존재하면 수치 증가

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/ml/ml1.png?raw=true" width="650" height="350"></p>

````python
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, y_pred)
````

📍 **RMSE**

- MSE에 루트 적용
- 제곱합으로 인해 커지는 손실을 scale down 함

````python
from sklearn.metrics import mean_squared_error
import numpy as np
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse) 
````

📍 **MSLE**

- MSE에 로그 적용
- 차이가 작을수록 큰 값을 가지기에 예측값이 작을때 유용

```` python
from sklearn.metrics import mean_squared_log_error
msle = mean_squared_log_error(y_test, y_pred) 
````

📍 **MAPE**

- MAE를 퍼센트로 변환
- 오차가 예측값에서 차지하는 퍼센트

````python
import numpy as np
def MAPE(y_test, y_pred):
 mape = np.mean(np.abs((y_test - y_pred)/y_test)) * 100
 return mape
mape = MAPE(y_test, y_pred)
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/ml/ml2.png?raw=true" width="650" height="350"></p>

### 1.2 분류 분석

📍 **Accuracy**

````python
from sklearn.metrics import accuracy_score
acc = accuracy_score(y_test, y_pred)
````

📍 **Confusion Matrix**

````python
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
````

📍 **Precision**

````python
from sklearn.metrics import precision_score
precision = precision_score(y_test, y_pred)
````

📍 **Recall**

````python
from sklearn.metrics import recall_score
recall = recall_score(y_test, y_pred)
````

📍 **F1-score**

````python
from sklearn.metrics import f1_score
f1 = f1_score(y_test, y_pred)
````

📍 **ROC curve**

- 분류 기준이 되는 threshold를 기준으로 FFR과 TPR을 구하고 그래프를 그림

````python
from sklearn.metrics import roc_curve
fpr, tpr, thres = roc_curve(y_test, y_pred, pos_label = 1)
import matplotlib.pyplot as plt
plt.plot(fpr, tpr)
````

📍**AUC score**

- ROC curve의 아래 면적으로 랜덤 수준의 AUC score는 0.5

````python
from sklearn.metrics import roc_curve, auc
fpr, tpr, thres = roc_curve(y_test, y_pred, pos_label = 1)
auc = auc(fpr, tpr)
````

## 2. 회귀분석

😗 **데이터 가져오기**

````python
from sklearn import datasets
import pandas as pd
df, price = datasets.fetch_openml('boston', return_X_y=True)
df['PRICE'] = price
````

### 2.1 데이터 확인하기

````python
# 대략적 형태 확인
df.head()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/ml/ml3.png?raw=true" width="600" height="200"></p>

````python
# 행, 열 확인
df.shape
````

````
(506, 14)
````

````python
# 타입 확인
df.info()
````

````
 #   Column   Non-Null Count  Dtype   
---  ------   --------------  -----   
 0   CRIM     506 non-null    float64 
 1   ZN       506 non-null    float64 
 2   INDUS    506 non-null    float64 
 3   CHAS     506 non-null    category
 4   NOX      506 non-null    float64 
 5   RM       506 non-null    float64 
 6   AGE      506 non-null    float64 
 7   DIS      506 non-null    float64 
 8   RAD      506 non-null    category
 9   TAX      506 non-null    float64 
 10  PTRATIO  506 non-null    float64 
 11  B        506 non-null    float64 
 12  LSTAT    506 non-null    float64 
 13  PRICE    506 non-null    float64 
dtypes: category(2), float64(12)
````

- CHAS를 제외하고는 모두 float형이어야 하지만, RAD가 1.0, 2.0 .. 과 같은 형태라 category로 인식됨 ☞ 형변환 필요

````python
df['RAD'] = df['RAD'].astype('float')
df.info()
````

````
 #   Column   Non-Null Count  Dtype   
---  ------   --------------  -----   
 0   CRIM     506 non-null    float64 
 1   ZN       506 non-null    float64 
 2   INDUS    506 non-null    float64 
 3   CHAS     506 non-null    category
 4   NOX      506 non-null    float64 
 5   RM       506 non-null    float64 
 6   AGE      506 non-null    float64 
 7   DIS      506 non-null    float64 
 8   RAD      506 non-null    float64 
 9   TAX      506 non-null    float64 
 10  PTRATIO  506 non-null    float64 
 11  B        506 non-null    float64 
 12  LSTAT    506 non-null    float64 
 13  PRICE    506 non-null    float64 
dtypes: category(1), float64(13)
````

````python
# null 확인
df.isna().sum()
````

````
CRIM       0
ZN         0
INDUS      0
CHAS       0
NOX        0
RM         0
AGE        0
DIS        0
RAD        0
TAX        0
PTRATIO    0
B          0
LSTAT      0
PRICE      0
dtype: int64
````

### 2.2 데이터 시각화

````python
import matplotlib.pyplot as plt
import seaborn as sns
# 3개의 행과 4개의 열을 가진 subplot 그리기
fig, axs = plt.subplots(figsize=(16,10), ncols=4, nrows=3, constrained_layout=True)
features = df.columns.difference(['PRICE', 'CHAS'])

for i, feature in zip(range(12), features):
    row = int(i/4) # 행번호 설정
    col = i%4 # 열번호 설정
    # seaborn의 regplot을 이용해 산점도와 선형 회귀직선을 함께 시각화함
    sns.regplot(x=feature, y=df['PRICE'], data=df, ax=axs[row][col])
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/ml/ml4.png?raw=true" width="900" height="700"></p>

### 2.3 데이터 분할

````python
from sklearn.model_selection import train_test_split
x = df[['CRIM', 'ZN', 'INDUS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']].values
y = df['PRICE'].values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print('학습데이터세트 PRICE 평균: ', y_train.mean())
print('평가데이터세트 PRICE 평균: ', y_test.mean())
````

````
학습데이터세트 PRICE 평균:  22.796534653465343
평가데이터세트 PRICE 평균:  21.488235294117644
````

### 2.4 전처리

````python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
x_train_scaled = scaler.fit_transform(x_train) 
````

### 2.5 모델 학습

````python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.metrics import r2_score
import numpy as np

# 모델 핛브
linear = LinearRegression()
linear.fit(x_train_scaled, y_train)

# 학습데이터로 평가
pred_train = linear.predict(x_train_scaled)
mae = mean_absolute_error(y_train, pred_train)
mse = mean_squared_error(y_train, pred_train)
rmse = np.sqrt(mse)
r2 = r2_score(y_train, pred_train)
print('MAE: {0: .5f}'.format(mae))
print('MSE: {0: .5f}'.format(mse))
print('RMSE: {0: .5f}'.format(rmse))

# 모델의 설명력
print('R2: {0: .5f}'.format(r2))
````

````
MAE:  3.32616
MSE:  22.11246
RMSE:  4.70239
R2:  0.74546
````

- R2는 모델의 설명력을 의미함

### 2.6 평가

````python
x_test_scaled = scaler.transform(x_test)
pred = linear.predict(x_test_scaled)

mae = mean_absolute_error(y_test, pred)
mse = mean_squared_error(y_test, pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, pred)
print('MAE: {0: .5f}'.format(mae))
print('MSE: {0: .5f}'.format(mse))
print('RMSE: {0: .5f}'.format(rmse))
print('R2: {0: .5f}'.format(r2))
````

````python
MAE:  3.23724
MSE:  24.63539
RMSE:  4.96341
R2:  0.66406
````

## 3. 분류분석

😗 **데이터 가져오기**

````python
from sklearn.datasets import load_iris
import pandas as pd
iris = load_iris()
iris_dt = iris.data
iris_label = iris.target
df = pd.DataFrame(data=iris_dt, columns=iris.feature_names)
df['label'] = iris_label
````

### 3.1 데이터 확인

````
df.head()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/ml/ml5.png?raw=true" width="650" height="250"></p>

````python
df.label.unique()
````

````
array([0, 1, 2])
````

````
df.shape
````

````
(150, 5)
````

````python
df.isna().sum()
````

````
sepal length (cm) 0
sepal width (cm) 0
petal length (cm) 0
petal width (cm) 0
Species 0
dtype: int64 
````

### 3.2 데이터 분할

````python
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(iris_dt, iris_label, test_size=0.2, random_state=0, stratify=iris_label)
````

### 3.3 모델 학습

````python
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
import numpy as np

dtree_clf_5 = DecisionTreeClassifier(max_depth=5, random_state=100)
dtree_clf_3 = DecisionTreeClassifier(max_depth=3, random_state=100)
dtree_clf_1 = DecisionTreeClassifier(max_depth=1, random_state=100) 

scores = cross_val_score(dtree_clf_5, x_train, y_train, scoring='accuracy', cv=10)
print("max depth 5")
print('교차검증 정확도: ', np.round(scores, 3))
print('평균 검증 정확도: ', np.round(np.mean(scores), 4))

scores = cross_val_score(dtree_clf_3, x_train, y_train, scoring='accuracy', cv=10)
print("max depth 3")
print('교차검증 정확도: ', np.round(scores, 3))
print('평균 검증 정확도: ', np.round(np.mean(scores), 4))


scores = cross_val_score(dtree_clf_1, x_train, y_train, scoring='accuracy', cv=10)
print("max depth 1")
print('교차검증 정확도: ', np.round(scores, 3))
print('평균 검증 정확도: ', np.round(np.mean(scores), 4))
````

````
max depth 5
교차검증 정확도:  [0.917 1.    0.917 1.    1.    0.833 1.    0.917 1.    0.833]
평균 검증 정확도:  0.9417
max depth 3
교차검증 정확도:  [0.917 1.    0.917 0.917 1.    0.833 1.    0.917 0.917 0.833]
평균 검증 정확도:  0.925
max depth 1
교차검증 정확도:  [0.667 0.667 0.667 0.667 0.667 0.667 0.667 0.667 0.667 0.667]
평균 검증 정확도:  0.6667
````

### 3.4 성능 평가

````python
dtree_clf_5.fit(x_train, y_train)
pred = dtree_clf_5.predict(x_test)
from sklearn.metrics import accuracy_score
print('의사결정나무(교차검증 후) 예측 정확도: {0:.5f}'.format(accuracy_score(y_test, pred)))
````

````
의사결정나무(교차검증 후) 예측 정확도: 0.96667
````



















