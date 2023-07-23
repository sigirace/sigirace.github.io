---
layout: single
title:  'ADP 실기 3장 데이터 전처리'
toc: true
categories: [ADP]
tags: [ADP 실기]

---

본 게시물은 데이터 전처리 종류와 방식에 대한 내용을 소개한다.
{: .notice}

## 1. 데이터 전처리 종류

- 데이터 클리닝: **결측치** 처리, **이상치** 확인 및 정제
- 데이터 변환: **스케일링**, 요약
- 데이터 축소: **차원축소**, **라벨링**
- 불균형 처리: **언더,오버 샘플링**
- 데이터 분할: **train, test split**

## 2. 이상치 확인 및 정제

> 결측치와 값이 크게 차이가 나는 데이터로 측정의 변동성이나 실험의 오류, 장비의 이상 등의 이류로 발생

### 2.1 이상치 종류

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/preproc/out1.png?raw=true" width="650" height="250"></p>

### 2.2 이상치 제거: IQR 방식

> Box plot의 이상치 결정 방법을 이용하며, 데이터를 4분위로 나눈 뒤 IQR(Q3-Q1)을 설정하고 Q1, Q3 부터 alpha * IQR 만큼 떨어진 것을 이상치로 간주

😗 **데이터 가져오기**

````python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
wine_load = load_wine()
wine = pd.DataFrame(wine_load.data, columns=wine_load.feature_names)
wine['Class'] = wine_load.target
wine['Class'] = wine['Class'].map({0:'class_0', 1:'class_1', 2:'class_2'})
````

📍 **Box plot 그리기**

````python
plt.boxplot(wine['color_intensity'], whis=1.5)
plt.title('color_intensity')
plt.show()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/preproc/out2.png?raw=true" width="500" height="300"></p>

📍 **이상치의 위치와 값 확인**

````python
import numpy as np
def outliers_iqr(dt, col):
 quartile_1, quartile_3 = np.percentile(dt[col], [25, 75])
 iqr = quartile_3 - quartile_1
 lower_whis = quartile_1 - (iqr * 1.5)
 upper_whis = quartile_3 + (iqr * 1.5)
 outliers = dt[(dt[col] > upper_whis) | (dt[col] < lower_whis)]
 return outliers[[col]]
outliers = outliers_iqr(wine,‘color_intensity’)
outliers
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/preproc/out3.png?raw=true" width="150" height="150"></p>

### 2.3 이상치 정제

📍 **이상치 제거**

````python
drop_outliers = wine.drop(index=outliers.index)
# 이상치를 삭제하기 전
print('Original :', wine.shape)
# 이상치 삭제 후
print('Drop outliers :', drop_outliers.shape)
````

````
Original : (178, 14)
Drop outliers : (174, 14)
````

📍**이상치 대체**

````python
# 이상치를 NaN으로 변경
wine.loc[outliers.index, 'color_intensity'] = np.nan
wine['color_intensity'].fillna(wine['color_intensity'].mean())
wine.loc[outliers.index, 'color_intensity']
````

````
151   NaN
158   NaN
159   NaN
166   NaN
````

````python
wine['color_intensity'] = wine['color_intensity'].fillna(wine['color_intensity'].mean())
wine.loc[outliers.index, 'color_intensity']
````

````
151    4.908678
158    4.908678
159    4.908678
166    4.908678
````

## 3. 범주형 변수 처리

> 부류, 범위 그리고 서열 등으로 구분되는 변수로 질적변수라고도 하며, object나 category 형으로 저장되고 수학적 의미가 없음

### 3.1 Label encoding

> 알파벳 순서로 숫자를 할당해 주기에 랭크된 숫자 정보가 의미를 잘못 내포하는지 확인 필요

📍**Label encoder 예시**

````python
from sklearn.preprocessing import LabelEncoder

item_label = ['b','a','c','d','a','b']
encoder = LabelEncoder()
encoder.fit(item_label)
test_label = ['a','a','b','d','c']
digit_label = encoder.transform(test_label)

print(encoder.classes_)
print(digit_label)
print(encoder.inverse_transform(digit_label))
````

````
['a' 'b' 'c' 'd']
[0 0 1 3 2]
['a' 'a' 'b' 'd' 'c']
````

### 3.2 One-hot encoding

> 더미 변수를 통해 category 변수를 이진화 시킴

😗 **데이터 불러오기**

````python
import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
iris = pd.DataFrame(iris.data, columns=iris.feature_names)
iris['Class'] = load_iris().target
iris['Class'] = iris['Class'].map({0:'Setosa', 1:'Versicolour', 2:'Virginica'})
````

📍 **dummy 변수를 통한 one-hot encoder 예시**

````python
iris_dummy = pd.get_dummies(iris, columns = ['Class'])
iris_dummy
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/preproc/oh1.png?raw=true" width="600" height="350"></p>

📍**sklearn을 활용한 one-hot encoder**

````python
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

data_dic = {'label':['Apple', 'Banana', 'Pear', 'Apple', 'Mango']}
df = pd.DataFrame(data_dic)

oh = OneHotEncoder(sparse_output=False)
oh.fit(df)
sk_oh_encoded = oh.transform(df)
pd.DataFrame(sk_oh_encoded.astype('int'), columns=oh.get_feature_names_out())
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/preproc/oh2.png?raw=true" width="350" height="200"></p>

````python
oh.inverse_transform(pd.DataFrame([1, 0, 0, 0]).T)
````

````
array([['Apple']], dtype=object)
````

👀 **Dummy variable trap**

> One-hot encoding을 통해 생성된 변수가 다른 변수들간의 상관성이 있는 것 ☞ **multicollinearity**<br>이를 극복하기 위해서는 dummy variables 중 하나를 버려야 함 by using VIF

### 3.3 Label vs One-hot 선택 기준

- Label: 순서의 의미가 있을 때, 고유값의 개수가 많아 one-hot 시 메모리 이슈가 있을 때
- One-hot: 순서가 없을 때, 고유값의 개수가 많지 않을 때

## 4. 데이터 분할

😗 **데이터 불러오기**

````python
import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
iris = pd.DataFrame(iris.data, columns=iris.feature_names)
iris['Class'] = load_iris().target
iris['Class'] = iris['Class'].map({0:'Setosa', 1:'Versicolour', 2:'Virginica'})
````

📍**train test split**

````python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris.drop(columns='Class'), iris['Class'], test_size = 0.2, random_state=1004)
print('X_train :', X_train.shape, ' X_test :', X_test.shape)
print('y_train :', y_train.shape, ' y_test :', y_test.shape)
````

````
X_train : (120, 4)  X_test : (30, 4)
y_train : (120,)  y_test : (30,)
````

👀 **Parameter**

- random state: 같은 수를 지정하면 같은 결과가 도출됨
- stratify: 지정하지 않을 시, class 비율이 원본과 차이가 나게 됨 ☞ 지정하면 층화추출법으로 모든 클래스가 동일하게 split

📍**층화 추출법**

````python
X_train, X_test, y_train, y_test = train_test_split(iris.drop(columns='Class'), iris['Class'], test_size = 0.2, stratify =iris['Class'])
print('X_train :', X_train.shape, '\tX_test :', X_test.shape)
print('y_train :', y_train.shape, '\ty_test :', y_test.shape)
````

````
X_train : (120, 4) 	X_test : (30, 4)
y_train : (120,) 	y_test : (30,)
````

````python
y_train.value_counts()
````

````
Class
Versicolour    40
Setosa         40
Virginica      40
Name: count, dtype: int64
````

## 5. 데이터 스케일링

### 5.1 Standard scaler

- 평균이 0 분산이 1인 정규 분포로 스케일링
- 최소값의 크기를 제한하지 않아 **이상치에 민감** ☞ 이상치 처리 필수
-  **분류분석에서 유용**

📍**standard scaler 예시**

````python
from sklearn.preprocessing import StandardScaler
StdScaler = StandardScaler()
# Train 데이터의 fitting과 스케일링
StdScaler.fit(X_train)
X_train_sc = StdScaler.transform(X_train)
# Test 데이터의 스케일링
X_test_sc = StdScaler.transform(X_test)
# 결과 확인
print('\t\t(min, max) (mean, std)')
print ('Train_scaled (%.2f, %.2f) (%.2f, %.2f)'%(X_train_sc.min(), X_train_sc.max(), X_train_sc.mean(), X_train_sc.std()))
print ('Test_scaled (%.2f, %.2f) (%.2f, %.2f)'%(X_test_sc.min(), X_test_sc.max(), X_test_sc.mean(), X_test_sc.std()))
````

````
		(min, max) (mean, std)
Train_scaled (-2.00, 3.13) (0.00, 1.00)
Test_scaled (-2.46, 2.34) (0.03, 1.06)
````

### 5.2 Min-max sclaer

- 0과 1 사이의 값으로 스케일링
- **이상치에 민감** ☞ 이상치 처리 필수
- **회귀분석에 유용**

📍**min-max scaler 예시**

````python
from sklearn.preprocessing import MinMaxScaler
MmScaler = MinMaxScaler()
# Train 데이터의 fitting과 스케일링
MmScaler.fit(X_train)
X_train_sc = MmScaler.transform(X_train)
# Test 데이터의 스케일링
X_test_sc = MmScaler.transform(X_test)
print('\t\t(min, max) (mean, std)')
print ('Train_scaled (%.2f, %.2f) (%.2f, %.2f)'%(X_train_sc.min(), X_train_sc.max(), X_train_sc.mean(), X_train_sc.std()))
print ('Test_scaled (%.2f, %.2f) (%.2f, %.2f)'%(X_test_sc.min(), X_test_sc.max(), X_test_sc.mean(), X_test_sc.std()))
````

````
		(min, max) (mean, std)
Train_scaled (0.00, 1.00) (0.43, 0.26)
Test_scaled (-0.09, 1.00) (0.44, 0.28)
````

### 5.3 Max abs scaler

- 모든 값이 -1과 1 사이에 표현 ☞ 데이터가 양수인 경우 min-max와 동일
- **이상치에 민감** ☞ 이상치 처리 필수
- **회귀분석에 유용**

📍**max abs scaler 예시**

````python
from sklearn.preprocessing import MaxAbsScaler
MaScaler = MaxAbsScaler()
# Train 데이터의 fitting과 스케일링
MaScaler.fit(X_train)
X_train_sc = MaScaler.transform(X_train)
# Test 데이터의 스케일링
X_test_sc = MaScaler.transform(X_test)
print('\t\t(min, max) (mean, std)')
print ('Train_scaled (%.2f, %.2f) (%.2f, %.2f)'%(X_train_sc.min(), X_train_sc.max(), X_train_sc.mean(), X_train_sc.std()))
print ('Test_scaled (%.2f, %.2f) (%.2f, %.2f)'%(X_test_sc.min(), X_test_sc.max(), X_test_sc.mean(), X_test_sc.std()))
````

````
		(min, max) (mean, std)
Train_scaled (0.04, 1.00) (0.61, 0.24)
Test_scaled (0.08, 1.00) (0.62, 0.24)
````

### 5.4 Robust scaler

- 평균과 분산 대신 중앙값과 사분위를 활용
- IQR을 사용하여 이상치 영향을 최소화

📍**robust scaler 예시**

````python
from sklearn.preprocessing import RobustScaler
RuScaler = RobustScaler()
# Train 데이터의 fitting과 스케일링
RuScaler.fit(X_train)
X_train_sc = RuScaler.transform(X_train)
# Test 데이터의 스케일링
X_test_sc = RuScaler.transform(X_test)
print('\t\t(min, max) (mean, std)')
print ('Train_scaled (%.2f, %.2f) (%.2f, %.2f)'%(X_train_sc.min(), X_train_sc.max(), X_train_sc.mean(), X_train_sc.std()))
print ('Test_scaled (%.2f, %.2f) (%.2f, %.2f)'%(X_test_sc.min(), X_test_sc.max(), X_test_sc.mean(), X_test_sc.std()))
````

````
		(min, max) (mean, std)
Train_scaled (-1.60, 2.80) (-0.02, 0.64)
Test_scaled (-2.00, 1.60) (-0.01, 0.68)
````

## 6. 차원 축소

👀 **차원의 저주**

> 데이터의 차원이 증가(=설명변수가 늘어남)에 따라 데이터 간의 거리가 멀어지고, 전체 영역에서 설명할 수 있는 데이터의 비율이 줄어듦 <br>☞ But, 차원이 늘어나는게 무조건 나쁜건 아님

### 6.1 설명변수 선택

- EDA에서 상관관계가 높았던 설명변수만을 사용
- 고차원적인 상관관계는 고려하기 어려움

### 6.2 주성분 분석

- 기존 컬럼을 저차원의 초평면에 투영
- 분산이 가장 높은 축(=설명을 가장 잘 하는 축)을 찾아 새로운 주성분으로 결정
- 수치형 데이터에 대해서만 진행
- 스케일 차이가 주성분 선정에 영향을 주는것을 방지하기 위해 이상치 제거 및 스케일링

😗 **데이터 불러오기**

````python
import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
iris = pd.DataFrame(iris.data, columns=iris.feature_names)
iris['Class'] = load_iris().target
iris['Class'] = iris['Class'].map({0:'Setosa', 1:'Versicolour', 2:'Virginica'})
````

📍**PCA 예시**

````python
# 수치형 데이터만 추출
features = ['수치형 변수1', '수치형 변수2']
x = iris.drop(columns = 'Class')
# 수치형 변수 정규화
from sklearn.preprocessing import StandardScaler
x = StandardScaler().fit_transform(x)
pd.DataFrame(x).head()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/preproc/pca1.png?raw=true" width="300" height="150"></p>

````python
from sklearn.decomposition import PCA
pca = PCA( n_components = 4) 
pca_fit = pca.fit(x)
print('고유 값 : ', pca.singular_values_)
print('분산 설명력: ', pca.explained_variance_ratio_)
````

````
고유 값 :  [20.92306556 11.7091661   4.69185798  1.76273239]
분산 설명력:  [0.72962445 0.22850762 0.03668922 0.00517871]
````

👀 **고유값**

> 데이터에서 해당하는 주성분 개수로 설명할 수 있는 분산의 비율

👀 **분산 설명력**

> 전체 데이터에서 각 주성분이 설명할 수 있는 분산의 비율

☀️ **고유값과 분산 설명력을 통해 주성분의 개수를 구할 수 있음**

📍 **Scree plot으로 주성분 개수 구하기**

👀 **scree plot**

> 주성분으로 설명할 수 있는 분산의 정도를 점으로 표시하고 각 점들을 이은 선 ☞ **기울기가 급격히 감소하는 지점 직전까지를 주성분 선택**

````python
import matplotlib.pyplot as plt

plt.title('Scree Plot')
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance')
plt.plot(pca.explained_variance_ratio_ , 'o-')
plt.show()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/preproc/pca2.png?raw=true" width="500" height="300"></p>

````python
# PCA 객체 생성 (주성분 개수 2개 생성)
pca = PCA(n_components = 2)
# 2개의 주성분을 가진 데이터로 변환
principalComponents = pca.fit_transform(x)
principal_iris = pd.DataFrame (data = principalComponents, columns =['pc1', 'pc2']) 
principal_iris.head()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/preproc/pca3.png?raw=true" width="200" height="150"></p>

````python
import matplotlib.pyplot as plt
import seaborn as sns
plt.title('2 component PCA' )
sns.scatterplot (x = 'pc1', y = 'pc2', hue = iris.Class, data = principal_iris)
plt.show()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/preproc/pca4.png?raw=true" width="500" height="300"></p>

- 산포도를 확인하면 원본 데이터프레임으로 그린 산포도보다 종속변수를 더 잘 설명하는 산포도 확인 가능

## 7. 데이터 불균형 문제 처리

### 7.1 언더 샘플링

> 작은 클래스에 맞추어 전체 데이터를 감소하는 기법으로 불균형은 해결할 수 있으나 학습 성능을 떨어뜨릴 수 있음

😗 **데이터 불러오기**

````python
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from collections import Counter
from imblearn.under_sampling import RandomUnderSampler
x, y = make_classification(n_samples=2000, n_features=6, weights=[0.95], flip_y=0)
print(Counter(y))
````

````
Counter({0: 1900, 1: 100})
````

📍 **Random under sampling**

````python
undersample = RandomUnderSampler(sampling_strategy='majority')
x_under, y_under = undersample.fit_resample(x, y)
print(Counter(y_under))
````

````
Counter({0: 100, 1: 100})
````

````python
undersample = RandomUnderSampler(sampling_strategy=0.5) 
x_under2, y_under2 = undersample.fit_resample(x, y)
print(Counter(y_under2))
````

````
Counter({0: 200, 1: 100})
````

### 7.2 오버 샘플링

> 다수 레이블에 맞춰 소수 레이블의 데이터를 증식시키는 방법으로 언더 샘플링보다 보통 유용함

😗 **데이터 불러오기**

````python
from imblearn.over_sampling import RandomOverSampler
oversample = RandomOverSampler(sampling_strategy=0.5) 
x_over, y_over = oversample.fit_resample(x, y)
print(Counter(y_over))
````

````
Counter({0: 1900, 1: 950})
````

📍 **Random over sampling**

````python
oversample = RandomOverSampler(sampling_strategy='minority')
x_over, y_over = oversample.fit_resample(x, y)
print(Counter(y_over))
````

````
Counter({0: 1900, 1: 1900})
````

📍 **SMOTE**

> 소수 레이블을 지닌 데이터 세트의 관측 값에 대한 KNN을 찾고, 관측 값과 이웃으로 선택된 값 사이에 새로운 데이터를 생성하여 데이터 증식

````python
from imblearn.over_sampling import SMOTE
smote_sample = SMOTE(sampling_strategy='minority') 
x_sm, y_sm = smote_sample.fit_resample(x, y)
print(Counter(y_sm))
````

````
Counter({0: 1900, 1: 1900})
````







