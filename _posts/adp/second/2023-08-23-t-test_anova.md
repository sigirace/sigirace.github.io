---
layout: single
title:  'ADP 실기 12장 T-test & ANOVA'
toc: true
categories: [ADP]
tags: [ADP 실기]

---

본 게시물은 T-test & ANOVA 에 대해 소개한다.
{: .notice}

## 1. T-검정

### 1.1 Concept

> 특정 집단의 평균 값을 추정하거나 차이를 검정할 때 사용

- 검정 통계량이 귀무가설 하에서 t-distribution을 따름
- 종속변수는 연속형 변수(평균값)
- 독립변수는 범주형 변수
- t-통계량: 분산을 사용하여 차이를 통계적으로 표현한 것

### 1.2 t-통계량

- 표본이 1개일 때

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/t/t1.png?raw=true" width="200" height="100"></p>

- 표본이 2개일 때

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/t/t2.png?raw=true" width="400" height="100"></p>

## 2. 일표본 T-검정

### 2.1 Concept

> 단일 모집단에서 관심이 있는 연속형 변수의 평균값을 특정 기준값과 비교

- 모집단의 구성요소들이 정규분포를 이뤄야함
- 종속변수는 연속형
- 검증하고자 하는 기준값이 있어야 함

### 2.2 Hypothesis

- 귀무가설: 모평균의 값은 x이다.
- 대립가설: 모평균의 값은 x가 아니다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/t/t3.png?raw=true" width="900" height="500"></p>

### 2.2 Implementation

😗 **cat의 몸무게가 2.6kg인지 아닌지 검정**

````python
import pandas as pd
cats=pd.read_csv("https://raw.githubusercontent.com/ADPclass/ADP_book_ver01/main/data/cats.csv")
cats
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/t/t4.png?raw=true" width="200" height="400"></p>

````
cats.info()
````

````
RangeIndex: 144 entries, 0 to 143
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   Sex     144 non-null    object 
 1   Bwt     144 non-null    float64
 2   Hwt     144 non-null    float64
dtypes: float64(2), object(1)
````

- Bwt는 몸무게

````
import scipy.stats as stats
from scipy.stats import shapiro
mu =2.6
shapiro(cats['Bwt'])
````

````
ShapiroResult(statistic=0.9518786668777466, pvalue=6.730228778906167e-05)
````

- mu에 2.6을 할당 후 정규성 검정 ☞ H0: 데이터가 정규분포를 따름
  - 검정통계치: 0.95187
  - p-value: < 0.05
- 귀무가설 기각하여 정규분포를 따르지 않음을 확인

````
stats.wilcoxon(cats.Bwt - mu , alternative='two-sided')
````

````
WilcoxonResult(statistic=3573.0, pvalue=0.02524520294814093)
````

- 데이터가 정규분포를 따르지 않으므로 wilcoxon test로 t-test 수행
  - p-value < 0.05
- 귀무가설(몸무게가 2.6)을 기각
- 정규분포를 따른다면 stats.ttest_1samp(cats.Bwt, popmean=mu)

````
import matplotlib.pyplot as plt
cats_Bwt_cnt = pd.value_counts(cats['Bwt'].values, sort=False)
width =0.4
plt.bar(cats_Bwt_cnt.index, cats_Bwt_cnt.values,width)
plt.title('Bwt')
plt.ylabel('Count')
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/t/t5.png?raw=true" width="900" height="500"></p>

- 시각화 결과 또한 정규분포를 띄지 않음

## 3. 대응표본 T-검정 (Paired Sample t-test)

### 3.1 Concept

> 단일 모집단에 대해 어떤 실험 후 전후 평균의 차이를 비교

- 표본 내 개체들에 대해 두번의 측정 ☞ 같은 집단이므로 등분산성 만족
- 모집단의 관측값이 정규성을 만족해야함

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/t/t6.png?raw=true" width="900" height="500"></p>

### 3.2 Hypothesis

- 귀무가설: 두 모평균 사이의 차이는 없다.
- 대립가설: 두 모평균 사이의 차이는 있다.

### 3.3 Implementation

😗 **수면제 복용의 효과 검증**

````
import pandas as pd 
data = {'before':[7,3,4,5,2,1,6,6,5,4], 
				'after':[8,4,5,6,2,3,6,8,6,5]}
data = pd.DataFrame(data)
````

````
stats.ttest_rel(data['after'],data['before'],alternative='greater')
````

````
TtestResult(statistic=4.743416490252569, pvalue=0.0005269356285082764, df=9)
````

- 표본이 정규성을 만족한다는 가정 (데이터가 임의의 데이터이므로)

````
data.mean()
````

````
before    4.3
after     5.3
````

## 4. 독립표본 t-test(Independent Sample t-test)

### 4.1 Concept

> 두 개의 독립된 모집단의 평균(=모평균)을 비교

- 두 모집단은 정규성을 만족해야 함
- 두 모집단의 분산이 서로 같아야 함 ☞ 등분산성

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/t/t7.png?raw=true" width="900" height="500"></p>

### 4.2 Hypothesis

- H0: 두 모평균 사이의 차이는 없다.
- H1: 두 모평균 사이의 차이는 있다.

### 4.3 Implementaion

😗 **수컷 고양이와 암컷 고양이의 몸무게 차이 비교**

````python
import pandas as pd
cats=pd.read_csv("https://raw.githubusercontent.com/ADPclass/ADP_book_ver01/main/data/cats.csv")
female = cats.loc[cats.Sex =='F', 'Bwt']
male = cats.loc[cats.Sex =='M', 'Bwt']
stats.levene(female, male)
````

````
LeveneResult(statistic=19.43101190877999, pvalue=2.0435285255189404e-05)
````

- 정규성을 만족한다고 가정
- 등분산성 검정 ☞ H0: 데이터가 등분산성을 만족
  - p-value < 0.05
- 등분산성을 만족하지 못하기에 equal_var=False로 독립 t-test를 수행

````python
stats.ttest_ind(female, male, equal_var=False)
````

````
Ttest_indResult(statistic=-8.70948849909559, pvalue=8.831034455859356e-15)
````

````python
print(female.mean())
print(male.mean())
````

````
2.359574468085107
2.8999999999999995
````

````python
female_Bwt_cnt = pd.value_counts(female.values, sort=False)
male_Bwt_cnt = pd.value_counts(male.values, sort=False)
fig, axs = plt.subplots(1, 2,figsize=(20,5))
fig.suptitle('Bar plot')
width =0.4
axs[0].bar(female_Bwt_cnt.index, female_Bwt_cnt.values)
axs[0].set_title('female_Bwt')
axs[0].set_ylabel('Count')
axs[1].bar(male_Bwt_cnt.index, male_Bwt_cnt.values)
axs[1].set_title('male_Bwt')
axs[1].set_ylabel('Count')
plt.show()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/t/t8.png?raw=true" width="900" height="400"></p>



## 5. ANOVA

### 5.1 Concept

> 두 개 이상의 다수 집단 간 평균을 비교하는 것으로, 집단 내 분산(=차이)보다 다른 집단과의 분산(=차이)이 더 크면 유의하다고 할 수 있음

- 종속변수는 연속형
- 독립변수는 범주형
- 개수에 따라 일원, 이원, 다원 배치로 나뉨

### 5.2 분산분석 분류표

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/t/a1.png?raw=true" width="700" height="300"></p>

## 6. 일원배치 분산분석 (One-way ANOVA)

### 6.1 Concept

>  반응값에 대한 하나의 범주형 변수의 영향을 알아보기 위해 사용되는 검증 방법

- 모집단의 수에는 제한이 없으며, 각 표본의 수는 같지 않아도 됨
- F 검정 통계량 이용

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/t/a2.png?raw=true" width="700" height="300"></p>

- F 검정 통계량은 분산의 비율값으로, 집단 내 분산보다 집단 간 분산이 크다면 F값은 커지고 귀무가설을 기각할 확률이 높아짐
- 집단의 측정치는 서로 독립이며 정규분포를 따름
- 집단 측정치의 분산은 같음 (=등분산)

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/t/a3.png?raw=true" width="900" height="500"></p>

### 6.2 Hypothesis

- H0: k개의 집단 간 모평균에는 차이가 없다. (=같다.)
- H1: k개의 집단 간 모평균이 모두 같다고 할 수 없다.

📍 **사후검정**

- 집단에서 평균의 차이가 있을 경우 어떤 집단들에 대해 평균의 차이가 존재하는지 알아보는 방법
  - H0: 집단들 사이의 평균은 같다.
  - H1: 집단들 사이의 평균은 같지 않다.
- 던칸의 MRT, 피셔의 LSD, 튜키의 HSD

### 6.3 Implementation

````python
import scipy.stats as stats 
import pandas as pd
Iris_data = pd.read_csv("https://raw.githubusercontent.com/ADPclass/ADP_book_ver01/main/data/iris.csv")
Iris_data.head(100)
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/t/a4.png?raw=true" width="700" height="300"></p>

````python
Iris_data["target"].unique()
````

````
array(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], dtype=object)
````

````python
Iris_data.target.value_counts()
````

````
target
Iris-setosa        50
Iris-versicolor    50
Iris-virginica     50
Name: count, dtype: int64
````

````python
target_list = Iris_data["target"].unique()
setosa = Iris_data[Iris_data["target"]==target_list[0]]["sepal width"]
versicolor = Iris_data[Iris_data["target"]==target_list[1]]["sepal width"]
virginica = Iris_data[Iris_data["target"]==target_list[2]]["sepal width"]
print(target_list)
````

````
['Iris-setosa' 'Iris-versicolor' 'Iris-virginica']
````

````python
import seaborn as sns
import matplotlib.pyplot as plt
# Scatter plot by Groups
sns.scatterplot(x='target', 
                y='sepal width', 
                hue='target', # different colors by group
                style='target', # different shapes by group
                s=100, # marker size
                data=Iris_data)
plt.show()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/t/a5.png?raw=true" width="700" height="400"></p>

````python
print(stats.shapiro(setosa))
print(stats.shapiro(versicolor))
print(stats.shapiro(virginica))
````

````
ShapiroResult(statistic=0.9686915278434753, pvalue=0.20464898645877838)
ShapiroResult(statistic=0.9741329550743103, pvalue=0.3379843533039093)
ShapiroResult(statistic=0.9673907160758972, pvalue=0.18089871108531952)
````

- 정규성 검정 (☞ 데이터가 정규성을 띄는지)
  - p-value > 0.05 이므로 정규성 만족
  - 하나라도 만족하지 않으면 kruskal 고려

````python
stats.levene(setosa,versicolor,virginica)
````

````
LeveneResult(statistic=0.6475222363405327, pvalue=0.5248269975064537)
````

- 등분산성 검정
  - p-value > 0.05 이므로 세 집단간 분산이 동일

````python
stats.f_oneway(setosa,versicolor,virginica)
````

````
F_onewayResult(statistic=47.36446140299382, pvalue=1.3279165184572242e-16)
````

- ANOVA 수행
  - p-value < 0.05 이므로 귀무가설 기각 ☞ 집단간 차이 존재

````python
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison
mc = MultiComparison(data= Iris_data["sepal width"], groups=Iris_data["target"] )
tuekeyhsd = mc.tukeyhsd(alpha=0.05)
fig = tuekeyhsd.plot_simultaneous()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/t/a6.png?raw=true" width="700" height="400"></p>

````python
tuekeyhsd.summary()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/t/a7.png?raw=true" width="400" height="150"></p>

- 어떤 집단간 차이가 있는지 확인하기 위해 사후 검정 수행
  - 모든 p-value < 0.05이므로 귀무가설 기각

````python
stats.kruskal(setosa,versicolor,virginica)
````

````
KruskalResult(statistic=62.49463010053111, pvalue=2.6882119006774528e-14)
````

- 정규성을 만족하지 못하였을 경우

````python
import pingouin as pg
pg.welch_anova(data = Iris_data, dv ='sepal width', between='target')
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/t/a8.png?raw=true" width="400" height="90"></p>

- 등분산성을 만족하지 못하였을 경우

## 7. 이원배치 분산분석 (Two-way ANOVA)

### 7.1 Concept

> 하나의 종속변수(연속형)에 대한 두 개의 독립변수(범주형) A, B의 영향을 알아보기 위해 사용되는 검증 방법

- 두 독립변수 A,B 사이에 상관관계가 있는지를 살펴보는 교호작용을 수해야 함

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/t/a9.png?raw=true" width="700" height="500"></p>

- 집단의 측정치는 서로 독립이며, 정규분포를 따름
- 집단 측정치의 분산은 같음 (=등분산)

### 7.2 Hypothesis

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/t/a10.png?raw=true" width="650" height="400"></p>

📍 **사후검정**

- 귀무가설이 기각되었을 경우(=적어도 한 집단에서 평균의 차이가 있음), 어떤 집단들에 대해 평균의 차이가 존재하는지 알아봄
- 던칸의 MRT, 피셔의 LSD, 튜키의 HSD 방법

### 7.3 Implementation

😗 **실린더 개수 및 변속기 종류가 주행거리에 영향을 주는지 검정**

````python
import pandas as pd
mtcars = pd.read_csv("https://raw.githubusercontent.com/ADPclass/ADP_book_ver01/main/data/mtcars.csv")
mtcars.head()
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/t/a11.png?raw=true" width="500" height="250"></p>

````python
mtcars = mtcars[["mpg","am","cyl"]]
mtcars.info()
````

````
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   mpg     32 non-null     float64
 1   am      32 non-null     int64  
 2   cyl     32 non-null     int64  
dtypes: float64(1), int64(2)
````

- target인 mpg는 연속형
- am과 cyl은 수치형이지만 의미상 범주형 변수임을 확인

📍**가설**

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/t/a14.png?raw=true" width="500" height="300"></p>

````python
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
formula = 'mpg ~ C(cyl) + C(am) + C(cyl):C(am)'
model = ols(formula, mtcars).fit()
aov_table = anova_lm(model, typ=2)
aov_table
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/t/a12.png?raw=true" width="400" height="200"></p>

- cyl 변수와 am 변수 간의 상호작용 효과 검정
  - p-value > 0.2 ☞ 교호작용 존재하지 않음 ☞ 주효과 검정이 의미있음
- cly 변수에 대한 주효과 검정
  - p-vlaue < 0.05 ☞ 귀무가설 기각 ☞ 차이 존재
- am 변수에 대한 주효과 검정
  - p-value > 0.05 ☞ 귀무가설 채택 ☞ 차이 없음

````python
from statsmodels.graphics.factorplots import interaction_plot
import matplotlib.pyplot as plt
## 독립변수 cyl,am와 종속변수 mpg을 Series로 변경 
cyl = mtcars["cyl"]
am = mtcars["am"]
mpg = mtcars["mpg"]
fig, ax = plt.subplots(figsize=(6, 6))
fig = interaction_plot(cyl,am, mpg,
 colors=['red', 'blue'], markers=['D', '^'], 
ms=10, ax=ax)
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/t/a13.png?raw=true" width="700" height="500"></p>

- 상호작용 그래프에서 두 선이 서로 교차시에 상호작용 존재함
- interaction_plot의 parameter는 x1, x2, y 순으로 작성

## 8. 교차분석(카이제곱 검정)

### 8.1 Concept

> 각 범주에 따른 결과변수의 분포를 설명하거나, 범주형 변수가 두 개 이상인 경우 상관이 있는지를 검정

- 교차표를 통해 각 셀의 관찰빈도와 기대빈도 간의 차이를 검정
  - 관찰빈도: 자료로부터 얻은 빈도 분포
  - 기대빈도: 두 변소가 독립일 때, 이론적으로 기대할 수 있는 빈도분포 (각 범주의 기대빈도는 5 이상)
- 적합성 검정, 독립성 검정, 동질성 검정

📍 **Example**

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/t/ch1.png?raw=true" width="600" height="230"></p>

- 환자군이면서 과체중인 사람의 관찰 빈도는 25, 기대빈도는 전체의 40%인 14
- 관찰빈도와 기대빈도의 차이가 유의한 차이가 있는지를 카이제곱 통계량을 이용하여 검정

### 8.2 적합성 검정

### 8.2.1 Concept

> 각 범주에 따른 데이터의 빈도분포가 이론적으로 기대하는 분포를 따르는지를 검정

- ex) 주사위를 굴렸을 때, 각 주사위의 값(범주)이 1/6의 확률(빈도분포)이 맞는지 검정

### 8.2.2 parameters

````
scipy.stats.chisquare( f_obs , f_exp =None , ddof =0 , axis =0 )
````

- f_obs: 관찰 빈도로 pd.value_counts() 결과 값 입력
- f_exp: 각 카테고리의 기대 빈도
- doff: p-value에 대한 자유도를 조정 (k-1-ddof)

### 8.2.3 Implementation

😗 **타이타닉호의 생존자 중 남, 녀의 비율 검정**

- H0: 타이타닉호의 생존자 중 남자의 비율이 50%, 여자의 비율이 50%
- H0: 타이타닉호의 생존자 중 남자의 비율이 50%, 여자의 비율이 50%가 아님

````python
import pandas as pd
# 데이터 불러오기
df = pd.read_csv("https://raw.githubusercontent.com/ADPclass/ADP_book_ver01/main/data/titanic.csv")
# titanic 데이터의 구조 확인
df.info()
````

````
Data columns (total 11 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   survived     891 non-null    int64  
 1   pclass       891 non-null    int64  
 2   sex          891 non-null    object 
 3   age          714 non-null    float64
 4   sibsp        891 non-null    int64  
 5   parch        891 non-null    int64  
 6   fare         891 non-null    float64
 7   embarked     889 non-null    object 
 8   class        891 non-null    object 
 9   adult_male   891 non-null    bool   
 10  embark_town  889 non-null    object 
dtypes: bool(1), float64(2), int64(4), object(4)
````

- target인 sex 변수 확인 결과 결측치가 없으며, 명목형 변수임을 확인

````python
df_t = df[df['survived']==1]
table= df_t[['sex']].value_counts()
table
````

````
sex   
female    233
male      109
````

- 교차분석을 위해 명목형 변수에 대한 도수분포표를 생성 ☞ 관찰빈도를 확인

````python
from scipy.stats import chisquare
chi = chisquare(table, f_exp=[171,171])
print('<적합도 검정>\n',chi)
````

````
<적합도 검정>
 Power_divergenceResult(statistic=44.95906432748538, pvalue=2.0119672574477235e-11)
````

- 적합도 검정 수행
  - p-value < 0.05 ☞ 귀무가설 기각 ☞ 남:녀 != 50:50

### 8.3 독립성 검정

### 8.3.1 Concept

> 모집단이 두 개의 변수 A, B에 의해 범주화 되었을 때, 이 두 변수들 사이의 관계가 독립인지 검정

📍 **Example**

- 환자의 비만유무와 질환 유무가 주어졌을 때, 비만에 따른 질환 비율에 차이가 존재하는지 검정

### 8.3.2 Parameters

````python
scipy.stats.chi2_contingency((observed, correction=True, lambda_=None ))
````

- observed: 관찰빈도로 pd.crosstab 결과를 입력
- expected: 수행 결과로 테이블 합계를 기반으로 한 기대빈도

### 8.3.3 Implementation

😗 **타이타닉 데이터에서 좌석등급과 생존여부가 서로 독립인지 검정**

- H0: 두 변수는 독립
- H1: 두 변수는 독립이 아님

````python
df = pd.read_csv("https://raw.githubusercontent.com/ADPclass/ADP_book_ver01/main/data/titanic.csv")
table = pd.crosstab(df['class'], df['survived'])
table
````

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/adp/t/ch2.png?raw=true" width="200" height="100"></p>

- 독립 검정을 위해 crosstab(교차표) 생성

````python
from scipy.stats import chi2_contingency
chi, p, df, expect = chi2_contingency(table) 
print('Statistic:', chi)
print('p-value:', p)
print('df:', df)
print('expect: \n', expect)
````

````
Statistic: 102.88898875696056
p-value: 4.549251711298793e-23
df: 2
expect: 
 [[133.09090909  82.90909091]
 [113.37373737  70.62626263]
 [302.53535354 188.46464646]]
````

- 독립성 검정 수행
  - p-value < 0.05 ☞ 귀무가설 기각 ☞ 독립이 아님

### 8.4 동질성 검정

> 모집단이 임의의 변수에 따라 R개 속성으로 범주화 되었을 때, R개의 부분 모집단에서 추출한 표본이 C개의 범주화된 집단의 분포가 서로 동일한지 검정

- 독립성 검정과 계산 법 및 방법이 동일
- 가설 설정만 다름
  - H0: class의 분포는 survived에 관계없이 동일
  - H1: class의 분포는 survived에 관계없이 동일하지 않음
