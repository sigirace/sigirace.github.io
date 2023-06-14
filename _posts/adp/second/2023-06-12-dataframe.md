---
layout: single
title:  '1. 데이터 프레임'
toc: true
categories: [ADP]
tags: [ADP 실기]
---

## Dataframe

### 1. iloc

````python
DataFrame.iloc[row, column]
````

- 정수로 된 위치 기반 인덱스로 행과 열을 선택

### 2. loc

````python
DataFrame.loc[row, column]
````

- 레이블로 행과 열을 선택

### 3. 결측값

````python
isna(), isnull()
notna(), notnull()
````

### 4. 결측값 제거

````python
DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
````

- axis: 0또는 index면 결측값이 포함된 행 삭제, 1 또는 column이면 결측값이 포함된 열 삭제
- how: 'any'이면 결측값이 존재하는 모든 행/열 삭제, 'all'이면 모든 값이 결측값일 때 삭제
- thresh: 정수값을 지정하면 결측값이 아닌 값이 그보다 많을 때 행 또는 열을 유지
- subset: 어떤 레이블에 결측값이 존재하면 삭제할지 정의

### 5. 결측값 대체

````python
DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None)
````

- value: 단일 값 혹은 dict/Series/DataFrame 형식으로 대체할 값을 직접 입력
- method: 'pad', 'fill' 이전 값, 'backfill','bfill' 다음에 오는 값으로 채움
- axis: 0 또는 index이면 행 방향, 1 또는 columns면 열 방향으로 채움
- limit: method 인자를 지정한 경우 limit로 지정한 개수만큼만 대체할 수 있음

### 6. 중복행 삭제

````python
DataFrame.drop_duplicates()
````

### 7. 데이터 정렬

````python
DataFrame.sort_index(axis=0, ascending=True, inplace=False)
````

- axis: 0이면 행 인덱스 기준, 1이면 컬럼명 기준 정렬
- ascending: True이면 오름차순, False이면 내림차순으로 정렬

````python
DataFrame.sort_values(by, axis=0, ascending=True, inplace=False)
````

- by: 정렬 기준으로 사용할 컬럼 혹은 컬럼명 리스트
- axis: 0이면 행 인덱스 기준, 1이면 컬럼명 기준 정렬
- ascending: True이면 오름차순, False이면 내림차순으로 정렬

### 8. 그룹화와 집계

````python
DataFrame.groupby(by=None, axis=0, level=None, as_index=True, sort=False, dropna=True).FUNC()
````

- by: subset
- axis: 0은 행기준 1은 열 기준 (default=0)
- level: 축이 계층 구조일 때 특정 수준을 기준으로 그룹화
- as_index: 그룹 레이블이 인덱스로 출력될지 여부(default=True)
- sort: 집계 행으로 정렬 여부
- dropna: True이면 결측값이 행/열과 함께 삭제, False이면 결측값도 그룹의 키로 처리

### 9. 도수분포표

````python
pd.Series(DataFrame['column_name']).value_counts()
````

- 수치형일 경우 모든 값에 대한 개수를 카운트하기에 범주형으로 변환해야 함

````python
pd.qcut(DataFrame['column_name'], q, labels)
````

- q: 나눌 그룹 수
- labels: 그룹수에 따른 label name

````python
pd.crosstab(index, columns, dropna=True, normalize=False)
````

- 두 개의 기준에 따른 데이터의 분포를 확인할 때 사용
- index: 열 위치에서 집계될 범주형 변수(컬럼1)
- columns: 행 위치에서 집계될 범주형 변수(컬럼2)
- dropna: 항목이 모두 NaN인 열을 제외할지 여부

### 10. Pivot

````python
DataFrame.pivot_table(index=None, columns=None, values=None, aggfunc='mean')
````

- index: 피벗 테이블에서 인덱스가 될 컬럼의 이름(두 개 이상이면 리스트로 입력)
- columns: 피벗 테이블에서 컬럼으로 분리할 컬럼의 이름(범주형 변수 사용)
- values: 피벗 테이블에서 columns의 값이 될 컬럼의 이름
- aggfunc: 집계함수를 사용할 경우 지정

### 11. Melt

````python
DataFrame.melt(id_vars=None, var_name=None, value_name=None)
````

- id_vars: 피벗 테이블에서 인덱스가 될 컬럼의 이름
- var_name: variable 변수의 이름으로 지정할 문자열(선택)
- value_name: value 변수의 이름으로 지정할 문자열(선택)

### 12. 날짜 데이터

````python
datetime.strptime('날짜 문자열', '포맷')
datetime.strftime('포맷')
````

