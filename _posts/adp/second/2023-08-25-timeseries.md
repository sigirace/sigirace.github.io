---
layout: single
title:  'ADP 실기 16장 Time Series'
toc: true
categories: [ADP]
tags: [ADP 실기]

---

본 게시물은 시계열 분석에 대한 내용을 소개한다.
{: .notice}

## 1. 시계열 분해

### 1.1 Concept

> 자료를 추세, 계절성, 잔차로 분해하는 기법

- 시간요인: 추세, 계절성
- 외부요인: 잔차(불규칙요인)

### 1.2 모형 판단

- 시계열 데이터를 보고 주기적 반복/ 계절성이 있는지에 따라 additive 모형과 multiplcative 모형 중 어떤 것이 더 적합할지 판단
- Additive: 추세와 계절성이 별개로 존재
- Multiplicative: 추세에 따라 계절성 존재

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/ts/ts1.png?raw=true" width="700" height="300"></p>

### 1.3 Implementation

````python
import pandas as pd
import warnings
data = pd.read_csv('https://raw.githubusercontent.com/ADPclass/ADP_book_ver01/main/data/arima_data.csv', 
                   names = ['day', 'price'])
data.head()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/ts/ts2.png?raw=true" width="200" height="150"></p>

````python
data.info()
````

````
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   day     60 non-null     object
 1   price   60 non-null     int64 
dtypes: int64(1), object(1)
````

- 시계열 분석을 위해 day를 datetime으로 변환

````python
data['day'] = pd.to_datetime(data['day'],format='%Y-%m-%d')
data.set_index('day', inplace=True)
data.head(3)
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/ts/ts3.png?raw=true" width="200" height="150"></p>

- 변환된 day를 index 지정

````python
import matplotlib.pyplot as plt
plt.plot(data.index,data['price'])
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/ts/ts4.png?raw=true" width="650" height="400"></p>

- 데이터를 시각화해서 보면, 추세에 따라 계절성이 존재
- 시간이 지날수록 변도이 커지므로 Multiplicative를 적용하여 시계열 분해

````python
from statsmodels.tsa.seasonal import seasonal_decompose
ts = data
result = seasonal_decompose(ts, model='multiplicative')
plt.rcParams['figure.figsize'] = [12, 8]
result.plot()
plt.show()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/ts/ts5.png?raw=true" width="650" height="550"></p>

- 시계열 분해 결과 Trend와 Seasonal이 존재
- 불규칙 요인이 없음

## 2. 정상성 변환

### 2.1 Concept

> 정상성은 평균, 분산이 시간에 따라 일정한 성질을 가지고 있는것으로, 시계열 데이터의 특성이 시간의 흐름에 따라 변하지 않는 상태를 의미

- 추세나 계절성이 있는 시계열은 정상 시계열이 아님

- 비정상 시계열인 경우 ARIMA 모델을 적용시킬 수 없음

  ☞ 정상 시계열로의 변환이 필요

### 2.2 로그 변환

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/ts/ts6.png?raw=true" width="650" height="300"></p>

- 로그 변환은 분산이 일정하지 않은 경우 사용
  - 위의 예시에서는 분산이 점차 커짐

### 2.3 차분

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/ts/ts7.png?raw=true" width="650" height="300"></p>

- 로그변환 후 추세, 계절성이 존재하는 경우 차분을 적용

### 2.4 Parameters

- 정상성 검정을 위해 Augmented Dickey-Fuller Test 수행
  - H0: 데이터가 정상성을 갖지 않는다.
  - H1: 데이터가 정상성을 갖는다.

````python
adfuller(x, maxlag, regression, autolag) 
````

- x: 2개의 관측값으로 이루어진 binary data를 배열 형식으로 받음, 관측은 정수형
- regression: 테스트 버전
  - 추세 없음: "nc"
  - 트렌드가 없는 경우: "c" (상수항만 있는 모델)
  - 선형 트렌드가 있는 경우: "ct" (상수항과 선형 트렌드 모델)
  - 2차 차분까지 포함된 트렌드가 있는 경우: "ctt" (상수항, 선형 트렌드, 2차 차분을 포함한 모델)
- return
  - t-statistic
  - p-value

### 2.5 Implementation

````python
from statsmodels.tsa.stattools import adfuller
#Train, Test 데이터 구분
training = data[:'2016-12-01']
test = data.drop(training.index)
adf = adfuller(training, regression='ct')
print('ADF Statistic: {}'.format(adf[0]))
print('p-value : {}'.format(adf[1]))
````

````
ADF Statistic: -1.9997199341328342
p-value : 0.6015863303793882
````

- train data가 가지고 있는 정상성 검정
  - p-value > 0.05 ☞ 정상성을 갖지 않음 ☞ 1차 차분 혹은 로그변환 필요

````python
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
diff_data = training.diff(1)
diff_data = diff_data.dropna()
diff_data.plot()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/ts/ts8.png?raw=true" width="650" height="400"></p>

- 1차 차분후 그래프

````python
adf = adfuller(diff_data)
print('ADF Statistic: {}'.format(adf[0]))
print('p-value : {}'.format(adf[1]))
````

````
ADF Statistic: -12.094547576926415
p-value : 2.0851606399611424e-22
````

- 1차 차분 후 그래프에 트렌드가 보이지 않기에 c를 적용하여 검정
  - p-value < 0.05 ☞ 정상성을 보임

## 3. AR

### 3.1 Concept

> 자기회귀 과정은 현 시점의 데이터를 이전 데이터들의 상관성으로 나타내는 모형

- 과거의 값이 현재의 값에 얼마나 영향을 미쳤는지 파악
  - 과거의 값이 현재의 값에 영향을 미치지 않았다면 성능은 낮아짐
- 최적의 성능을 만들어내는 과거의 값을 p라고 하며 AR(p) 모델이 됨

### 3.2 PACF

- 편자기상관 함수
- 시차가 다른 두 시계열 데이터 간의 순수한 상호 연관성
- PACF 값이 0에 수렴할 때의 p 값을 AR 모델의 p로 설정

### 3.3 Implementation

````python
plot_pacf(diff_data) # AR(p)의 값 확인 가능
plt.show()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/ts/ts9.png?raw=true" width="650" height="400"></p>

- PACF 그래프에서 y값이 처음으로 양에서 음으로 바뀌는 시차(p)는 현재 시점과 p 시점 전의 관측치 간의 상관 관계가 유의미하게 떨어진 시차를 나타내기에 AR(p) 모델의 차수로 선택

## 4. MA

### 4.1 Concept

> 과거 예측 오차들의 가중이동평균으로 현재 시점의 데이터를 표현하는 모델

- 과거의 예측 오차를 이용하여 미래를 예측하는 모델
- MA 모델이 최적이 되게 하는 변수 값을 q라고 하며 MA(q) 모델이라고 함

### 4.2 ACF

- 자기상관 함수로 시차에 다른 자기상관성을 의미
- 비정상 시계열일 경우 ACF 값은 느리게 0에 접근하며 양수의 값을 가질 수 있음
  - 추세나 계절성을 갖고 있기 때문에 가장 최근의 상관성이 높을 것이고, 과거의 값은 상대적으로 낮음 ☞ 느리게 0에 수렴
- 정상 시계열일 경우 ACF 값이 빠르게 0으로 수렴하며 이때를 q로 설정

### 4.3 Implementation

````python
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
plot_acf(diff_data) #MA(q)의 값 확인 가능
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/ts/ts10.png?raw=true" width="650" height="400"></p>

- 시차 2 이후에 0에 수렴하므로 q값은 2로 설정

## 5. ARIMA

### 5.1 Concept

> 비정상적 시계열 자료에 대해 분석하는 모형

- 차분을 사용하여 정상 시계열로 만듦
- AR, MA 모형을 결합하여 과거 시점의 데이터로 현재 혹은 미래 시점의 데이터 예측

### 5.2 Parameters

````python
from statsmodels.tsa.arima.model import ARIMA 
````

- endog or exog: 인덱스를 가지고 1개의 관측값으로 이루어진 데이터 입력
- order: p, d, q를 사용하며 d는 정상성을 가지게 될 때 까지 사용되는 차분의 횟수
- trend: 정상성 검정시 사용한 regression 과 동일

### 5.3 Implementation

````python
from statsmodels.tsa.arima.model import ARIMA
model = ARIMA(training, order=(2,1,2))
res = model.fit()
res.summary()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/ts/ts11.png?raw=true" width="400" height="500"></p>

- AIC: AIC가 작을수록 모델의 성능이 좋음
- coef에서 ar, ma가 p-value 0.05 이하라면 AR, MA 모델 사용 가능
  - L은 시차를 의미

````python
plt.plot(res.predict())
plt.plot(training)
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/ts/ts12.png?raw=true" width="650" height="400"></p>

- train data로 확인 결과 그래프 모양이 일치하므로 과소적합은 의심되지 않음

````python
forecast_data = res.forecast(steps=len(test), alpha=0.05) 
# 학습데이터세트로부터 test 데이터 길이만큼 예측
pred_y= forecast_data
pred_y
````

````
2017-01-01    5830.873897
2017-02-01    5508.758958
2017-03-01    5884.150158
2017-04-01    5492.640751
2017-05-01    5888.364253
2017-06-01    5492.238045
2017-07-01    5887.548906
2017-08-01    5493.440411
2017-09-01    5886.225819
2017-10-01    5494.798895
2017-11-01    5884.859269
2017-12-01    5496.164765
````

````python
test_y = test # 실제 데이터
test_y
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/ts/ts18.png?raw=true" width="150" height="300"></p>

````python
plt.plot(pred_y, color='gold', label='Predict') # 모델이 예상한 가격 그래프
plt.plot(test_y, color='green' , label='test') # 실제 가격 그래프
plt.legend()
plt.show()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/ts/ts13.png?raw=true" width="650" height="400"></p>

- 그래프를 확인한 결과 예측이 잘 되지 않음

````python
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
print('r2_score : ', r2_score(test_y, pred_y))
RMSE = mean_squared_error(test_y, pred_y)**0.5
print('RMSE : ' , RMSE)
````

````
r2_score :  -1.6424718909550333
RMSE :  2302.013569686878
````

- R-square가 음수가 나온 것은 정확도가 매우 낮음
- 데이터가 1년 단위로 계절성이 있기 때문
  - 계절성이 있는 경우 SARIMA 모델을 적용하는 것이 적합

## 6. SARIMA

### 6.1 Concept

> 데이터가 지닌 계절성 까지 고려한 ARIMA 모델

### 6.2 Parameters

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/ts/ts14.png?raw=true" width="600" height="500"></p>

### 6.3 Implementation

````Python
from pmdarima import auto_arima
auto_model = auto_arima(training, start_p=0, d=1, start_q=0,
                        max_p=3, max_q=3, 
                        start_P=0, start_Q=0,
                        max_P=3, max_Q=3, m=12,
                        seasonal=True, information_criterion='aic',
                        trace=True)
````

````
Best model:  ARIMA(0,1,1)(0,1,0)[12]
````

- ARIMA 모델과는 다른 값이 나온것을 보아 계절성이 추가되며 다른 학습이 되었다는 의미

````python
auto_model.summary()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/ts/ts15.png?raw=true" width="400" height="500"></p>

````python
# 학습데이터세트로부터 test 데이터 길이만큼 예측
auto_pred_y= pd.DataFrame(auto_model.predict(n_periods=len(test)), index=test.index) 
auto_pred_y.columns = ['predicted_price']
auto_pred_y
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/ts/ts16.png?raw=true" width="200" height="400"></p>

````python
plt.figure(figsize=(10,6))
plt.plot(training, label='Train') # Train 데이터 
plt.plot(auto_pred_y, label='Prediction') # 모델이 예상한 그래프 
plt.plot(test, label='Test') # 실제 가격 그래프 
plt.legend(loc='upper left')
plt.show()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/ts/ts17.png?raw=true" width="650" height="400"></p>

````python
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
print('r2_score : ', r2_score(test_y, auto_pred_y))
RMSE = mean_squared_error(test_y, auto_pred_y)**0.5
print('RMSE : ' , RMSE)
````

````
r2_score :  0.9305467058434135
RMSE :  373.2064283878219
````

