---
layout: single
title:  'LSTM의 모든것 (4) Timeseries forecasting - Make Dataset'
toc: true
categories: [Deep Learning]
tags: [timeseries, lstm]
---

본 게시물은 LSTM을 사용한 [시계열 예측 예제](https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/structured_data/time_series.ipynb#scrollTo=6GmSTHXw6lI1) 내용 중 데이터 셋을 만드는 부분을 정리하는 글이다.
{: .notice}

<div class="notice">
<li><a href="https://sigirace.github.io/deep%20learning/LSTM_method///">LSTM의 모든것 (1) LSTM 및 내부 Gate에 대한 이해</a></li>
<li><a href="https://sigirace.github.io/deep%20learning/LSTM_components//">LSTM의 모든것 (2) PyTorch 공식 문서로 보는 구성요소</a></li>
</div>

## 1. Introduce

튜토리얼은 time series forecasting에 대한 것으로, weather time series dataset을 사용하여 air temperature를 예측을 수행한다. 튜토리얼에서는 이를위해 CNN 및 RNN 등 몇가지 다른 스타일의 모델링을 수행한다. 튜토리얼은 두가지 부분으로 나누어 구성되어 있다.

1. Single step에 대한 예측
2. Multi step에 대한 예측

###  📌 import

```python
import os
import datetime

import IPython
import IPython.display
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf
from sklearn.preprocessing import StandardScaler

mpl.rcParams['figure.figsize'] = (8, 6)
mpl.rcParams['axes.grid'] = False
```

## 2. Dataset

### 📌 weather dataset

Dataset은 온도, 기압, 습도 등 14개의 다른 feature들로 구성되어 있다. 데이터는 2003년부터 10분 간격으로 기록되어 있으며, 튜토리얼에서는 2009년부터 2016년 까지의 데이터를 사용한다. 이때 예측의 목표가 되는 Target은 **T (degC)** 이다.

```python
zip_path = tf.keras.utils.get_file(
    origin='https://storage.googleapis.com/tensorflow/tf-keras-datasets/jena_climate_2009_2016.csv.zip',
    fname='jena_climate_2009_2016.csv.zip',
    extract=True)
csv_path, _ = os.path.splitext(zip_path)
```

데이터 셋의 컬럼별 설명은 아래와 같다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm_tuto_keras/lstm-t-k_3.png?raw=true" width="500" height="600"></p>

튜토리얼에서는 시간별 예측을 진행할 것이기 때문에 10분 간격을 1시간 간격으로 sub-sampling 한다.

```python
df = pd.read_csv(csv_path)
# Slice [start:stop:step], starting from index 5 take every 6th record.
df = df[5::6]

date_time = pd.to_datetime(df.pop('Date Time'), format='%d.%m.%Y %H:%M:%S')
df.head()
```

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm_tuto_keras/lstm-t-k_1.png?raw=true" width="900" height="250"></p>

구성된 데이터를 그래프로 확인해본다. 위는 전체 데이터에 대한 [T, p, rho]의 시간별 그래프이고, 아래는 20(480시간)일의 시간별 그래프이다.

```python
plot_cols = ['T (degC)', 'p (mbar)', 'rho (g/m**3)']
plot_features = df[plot_cols]
plot_features.index = date_time
_ = plot_features.plot(title="Total Plot",subplots=True)

plot_features = df[plot_cols][:480]
plot_features.index = date_time[:480]
_ = plot_features.plot(title="Subsample Plot", subplots=True)
```

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm_tuto_keras/lstm-t-k_2.png?raw=true" width="600" height="450"></p>

### 📌 Inspect and cleanup

데이터 셋에 대한 통계를 통해 이상치를 제거한다. 현재 데이터 중 [wv, max. wv]에서 최소값이 -9999.0으로 이상함을 확인하였다.

```python
df.describe().transpose()
```

데이터 셋은 풍향 [wd]가 포함되어 있기 때문에, 모든 값은 0 이상으로 수정한다.

```python
df['wv (m/s)']=df['wv (m/s)'].apply(lambda x: 0 if x < 0 else x)
df['max. wv (m/s)'] = df['max. wv (m/s)'].apply(lambda x: 0 if x < 0 else x)

# The above inplace edits are reflected in the DataFrame.
df['wv (m/s)'].min()
```

## 3. Feature Engineering

모델에 데이터를 적절한 형식에 맞추어 넘겨주고 있는지 확인해본다.

### 📌 Wind

[wd]는 풍향을 각도의 단위로 나타낸다. 각도는 0부터 360까지 이루어져 있지만 이는 모델이 학습하기 쉬운 표현이 아니다. 현실에서 0도와 360도는 서로 가깝게 보아야하기 때문이다. 현재 풍향 및 풍속[wv, wd]에 대한 분포는 아래와 같이 나타난다.

```python
plt.hist2d(df['wd (deg)'], df['wv (m/s)'], bins=(50, 50), vmax=400)
plt.colorbar()
plt.xlabel('Wind Direction [deg]')
plt.ylabel('Wind Velocity [m/s]')
```

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm_tuto_keras/lstm-t-k_4.png?raw=true" width="500" height="300"></p>

분포를 보았을때 의미를 확인하기 쉽지 않다. 따라서 풍향 및 풍속[wv, wv]을 합쳐 바람에 대한 벡터로 만들면 모델이 이해하기 쉬울 것이다.

```python
wv = df.pop('wv (m/s)')
max_wv = df.pop('max. wv (m/s)')

# Convert to radians.
wd_rad = df.pop('wd (deg)')*np.pi / 180

# Calculate the wind x and y components.
df['Wx'] = wv*np.cos(wd_rad)
df['Wy'] = wv*np.sin(wd_rad)

# Calculate the max wind x and y components.
df['max Wx'] = max_wv*np.cos(wd_rad)
df['max Wy'] = max_wv*np.sin(wd_rad)
```

변환된 분포는 모델이 이해하기 훨씬 쉬워 보인다.

```python
plt.hist2d(df['Wx'], df['Wy'], bins=(50, 50), vmax=400)
plt.colorbar()
plt.xlabel('Wind X [m/s]')
plt.ylabel('Wind Y [m/s]')
ax = plt.gca()
ax.axis('tight')
```

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm_tuto_keras/lstm-t-k_5.png?raw=true" width="500" height="300"></p>

### 📌 Time

시간 [Date Time]은 중요한 정보를 가지고 있을 수 있으나 str 형태가 아니기에, 먼저 시간을 초단위로 변환한다.

```python
timestamp_s = date_time.map(pd.Timestamp.timestamp)
```

시간 데이터 또한 방향과 마찬가지로 모델이 해석하기 적합하지 않다. 현재 다루고 있는 데이터가 날씨 데이터이기에 명확한 주기성을 가지고 있을 것이나, 현재 상태로는 모델이 이를 이해하기 쉽지 않다. 이러한 주기성을 담을 수 있는 대표적 방법은  sin 및 cos 변환을 수행하는 것이다. 이는 연속적인 시계열에 대하여 'day' 및 'year'에 대한 정보를 제외한 주기성만을 남길 수 있다.

```python
day = 24*60*60
year = (365.2425)*day

df['Day sin'] = np.sin(timestamp_s * (2 * np.pi / day))
df['Day cos'] = np.cos(timestamp_s * (2 * np.pi / day))
df['Year sin'] = np.sin(timestamp_s * (2 * np.pi / year))
df['Year cos'] = np.cos(timestamp_s * (2 * np.pi / year))

plt.plot(np.array(df['Day sin'])[:25])
plt.plot(np.array(df['Day cos'])[:25])
plt.xlabel('Time [h]')
plt.title('Time of day signal')
```

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm_tuto_keras/lstm-t-k_6.png?raw=true" width="500" height="300"></p>

## 4. Additional data processing

### 📌 Split the data

Train, Valid, Test를 전체 데이터의 (70%, 20%, 10%)로 분할한다. 이때 데이터를 랜덤하게 섞지 않도록 한다. 이는 시계열 데이터의 연속성을 유지하여 valid, test dataset 검증시에 실제 상황과 유사하게 하기 위함이다.

```python
# column과 index를 매핑시킴
column_indices = {name: i for i, name in enumerate(df.columns)}

n = len(df)
train_df = df[0:int(n*0.7)]
val_df = df[int(n*0.7):int(n*0.9)]
test_df = df[int(n*0.9):]

num_features = df.shape[1]
```

### 📌 Normalize the data

정규화 진행시 주의해야 할 점은, valid 및 test 데이터를 모른다고 가정하는 것이다. 따라서 train set으로 생성한 scaler를 valid 및 test에 적용한다. 이떄, scaler는 skit-learn이 제공하는 min-max scaler를 사용한다.

```python
# scaling

def train_scaling(df, target):

    X_scaler = StandardScaler()
    Y_scaler = StandardScaler()
    col_list = df.columns.to_list()
    col_list.remove(target)
    X = X_scaler.fit_transform(df[col_list])
    y = Y_scaler.fit_transform(df[[target]])

    scaler_list = {'X_scaler': X_scaler,
                   'Y_scaler': Y_scaler}

    df_scaled = pd.concat([pd.DataFrame(y, columns=[target]), pd.DataFrame(X, columns=col_list)], axis=1)

    return df_scaled, scaler_list

def test_scaling(df, target,  scaler_list):
    
    col_list = df.columns.to_list()
    col_list.remove(target)

    X_scaler = scaler_list['X_scaler']
    Y_scaler = scaler_list['Y_scaler']
    
    df_scaled = pd.concat([pd.DataFrame(Y_scaler.transform(df[[target]]), columns=[target]),\
                           pd.DataFrame(X_scaler.transform(df[col_list]), columns=col_list)],\
                           axis=1)
    
    return df_scaled
  
target = 'T (degC)'
train_df, scaler_list = train_scaling(train_df, target)
val_df = test_scaling(val_df, target, scaler_list)
test_df = test_scaling(test_df, target, scaler_list)
```

구성된 데이터 셋을 통해 violin plot을 그려보면 이상치 데이터는 제거되었고, 일정 범위 안에 데이터가 존재함을 확인 할 수 있다.

```python
plt.figure(figsize=(12, 6))
ax = sns.violinplot(data=train_df)
_ = ax.set_xticklabels(df.keys(), rotation=90)
```

## 5. Data windowing

튜토리얼에서 구현할 모델은 연속적인 샘플의 window를 기반으로 예측을 수행한다. 연속적인 window를 만들기 위한 함수는 아래의 파라미터들이 필요하다. 더하여 해당 함수는 single-output/ multi-output/ single-time-step/ multi-time-step 모델에서 모두 사용할 수 있도록 범용성을 갖추도록 설계한다.

- number of time steps: window size를 결정함
- offset: 몇 step 뒤를 예측할지 결정함
- label: 어떤 column을 target으로 할지 결정함

📍 **예시**

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm_tuto_keras/lstm-t-k_7.png?raw=true" width="600" height="250"></p>

> 24시간의 과거 데이터가 주어졌을 때, 24시간 후를 예측하는 데이터 window 구성

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm_tuto_keras/lstm-t-k_8.png?raw=true" width="400" height="250"></p>

> 6시간의 과거 데이터가 주어졌을 때, 1시간 후를 예측하는 데이터 window 구성

### 📌 Indexes and offsets

먼저 WindowGenerator class를 만든다. class를 초기화 시킬 때 입력되는 parameter는 아래와 같다.

- input_width: 예측을 위해 주어질 window의 길이
- label_width: 예측할 window의 길이
- shift: 향후 몇 step 뒤를 예측할 것인지

```python
class WindowGenerator():
  def __init__(self, input_width, label_width, shift,
               train_df=train_df, val_df=val_df, test_df=test_df,
               label_columns=None):
    # 원본 데이터를 저장함
    self.train_df = train_df
    self.val_df = val_df
    self.test_df = test_df

    # label, column 인덱싱
    self.label_columns = label_columns
    if label_columns is not None:
      # {label_name0:0, label_name1:1, ...}
      self.label_columns_indices = {name: i for i, name in
                                    enumerate(label_columns)}
    # {column_name0:0, column_name1:1, ...}        
    self.column_indices = {name: i for i, name in
                           enumerate(train_df.columns)}

    # window parameter 저장
    # input_width: input time step / label_width: output size
    # shift: input time 후 몇 시점 뒤를 label의 시점으로 할 것인지
    self.input_width = input_width
    self.label_width = label_width
    self.shift = shift

    # 하나의 window의 총 size
    self.total_window_size = input_width + shift
		
    # input, output 인덱싱
    self.input_slice = slice(0, input_width)
    self.input_indices = np.arange(self.total_window_size)[self.input_slice]

    self.label_start = self.total_window_size - self.label_width
    self.labels_slice = slice(self.label_start, None)
    self.label_indices = np.arange(self.total_window_size)[self.labels_slice]

  def __repr__(self):
    return '\n'.join([
        f'Total window size: {self.total_window_size}',
        f'Input indices: {self.input_indices}',
        f'Label indices: {self.label_indices}',
        f'Label column name(s): {self.label_columns}'])
```

앞선 예시를 위 클래스에 적용해 보면 다음과 같다.

```python
w1 = WindowGenerator(input_width=24, label_width=1, shift=24,
                     label_columns=['T (degC)'])
w1
```

```
Total window size: 48
Input indices: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
Label indices: [47]
Label column name(s): ['T (degC)']
```

```python
w2 = WindowGenerator(input_width=6, label_width=1, shift=1,
                     label_columns=['T (degC)'])
w2
```

````
Total window size: 7
Input indices: [0 1 2 3 4 5]
Label indices: [6]
Label column name(s): ['T (degC)']
````

### 📌 Split

앞서 WindowGenerator는 Input과 Output의 index 정의를 하였지만, 실제로 이를 잘라서 구성하지는 않았다. 따라서 split_window 함수를 통해 이를 실제 윈도우 단위로 잘라서 리턴해주는 작업을 수행한다.

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm_tuto_keras/lstm-t-k_9.png?raw=true" width="400" height="250"></p>

이는 앞서 구성한 w2 객체에 대한 split_window 예시이다.

```python
def split_window(self, features):
  inputs = features[:, self.input_slice, :]
  labels = features[:, self.labels_slice, :]
  if self.label_columns is not None:
    labels = tf.stack(
        [labels[:, :, self.column_indices[name]] for name in self.label_columns],
        axis=-1)

  # Slicing doesn't preserve static shape information, so set the shapes
  # manually. This way the `tf.data.Datasets` are easier to inspect.
  inputs.set_shape([None, self.input_width, None])
  labels.set_shape([None, self.label_width, None])

  return inputs, labels

WindowGenerator.split_window = split_window
```

```python
# Stack three slices, the length of the total window.
example_window = tf.stack([np.array(train_df[:w2.total_window_size]),
                           np.array(train_df[100:100+w2.total_window_size]),
                           np.array(train_df[200:200+w2.total_window_size])])

example_inputs, example_labels = w2.split_window(example_window)

print('All shapes are: (batch, time, features)')
print(f'Window shape: {example_window.shape}')
print(f'Inputs shape: {example_inputs.shape}')
print(f'Labels shape: {example_labels.shape}')
```

```
All shapes are: (batch, time, features)
Window shape: (3, 7, 19)
Inputs shape: (3, 6, 19)
Labels shape: (3, 1, 1)
```

일반적으로 Tensorflow의 데이터는 [batch, time step, feature]로 구성된다. 위 예제에서는 3개의 배치를 가진 7 time step 및 19 features의 window를 구성하였다. 이때, 앞의 6 step은 Input이며 마지막 1 step은 label을 구성한다. feature의 경우 초기화시 1개의 label을 입력하였기에 label은 1개의 차원을 가지게 된다.

### 📌 Plot

구성된 window에 대한 시각화를 수행한다.

```python
w2.example = example_inputs, example_labels
```

```python
def plot(self, model=None, plot_col='T (degC)', max_subplots=3):
  inputs, labels = self.example
  plt.figure(figsize=(12, 8))
  plot_col_index = self.column_indices[plot_col]
  max_n = min(max_subplots, len(inputs))
  for n in range(max_n):
    plt.subplot(max_n, 1, n+1) 
    plt.ylabel(f'{plot_col} [normed]')
    plt.plot(self.input_indices, inputs[n, :, plot_col_index],
             label='Inputs', marker='.', zorder=-10)

    if self.label_columns:
      label_col_index = self.label_columns_indices.get(plot_col, None)
    else:
      label_col_index = plot_col_index

    if label_col_index is None:
      continue

    plt.scatter(self.label_indices, labels[n, :, label_col_index],
                edgecolors='k', label='Labels', c='#2ca02c', s=64)
    if model is not None:
      predictions = model(inputs)
      plt.scatter(self.label_indices, predictions[n, :, label_col_index],
                  marker='X', edgecolors='k', label='Predictions',
                  c='#ff7f0e', s=64)

    if n == 0:
      plt.legend()

  plt.xlabel('Time [h]')

WindowGenerator.plot = plot

w2.plot()
```

<p align="center"><img src="https://github.com/sigirace/page-images/blob/main/pytorch/lstm_tuto_keras/lstm-t-k_10.png?raw=true" width="600" height="300"></p>

### 📌 Create tf.data.Dataset

make_dataset 함수를 통해 time series DataFrame을 tf.keras.utils.timeseries_dataset_from_array를 사용해 (input_window, label_window)쌍의 tf.data.Dataset로 변환한다.

```python
def make_dataset(self, data):
  data = np.array(data, dtype=np.float32)
  ds = tf.keras.utils.timeseries_dataset_from_array(
      data=data,
      targets=None,
      sequence_length=self.total_window_size,
      sequence_stride=1,
      shuffle=True,
      batch_size=32,)

  ds = ds.map(self.split_window)

  return ds

WindowGenerator.make_dataset = make_dataset
```

앞서 생성한 WindowGenerator의 객체에는 train, valid, test data가 포함되어있다. 이들에 대한 접근 및 변형(make_dataset 함수등)을 위해 @property를 추가해준다. 또한 배치의 예시를 쉽게 확인하기 위하여 example 함수를 생성한다.

```python
@property
def train(self):
  return self.make_dataset(self.train_df)

@property
def val(self):
  return self.make_dataset(self.val_df)

@property
def test(self):
  return self.make_dataset(self.test_df)

@property
def example(self):
  """Get and cache an example batch of `inputs, labels` for plotting."""
  result = getattr(self, '_example', None)
  if result is None:
    # No example batch was found, so get one from the `.train` dataset
    result = next(iter(self.train))
    # And cache it for next time
    self._example = result
  return result

WindowGenerator.train = train
WindowGenerator.val = val
WindowGenerator.test = test
WindowGenerator.example = example
```

이로 인하여 WindowGenerator 객체는 tf.data.Dataset 개체에 대한 접근이 가능하기 때문에, 데이터를 쉽게 반복할 수있다. element_spec은 데이터셋의 구조, 유형 등을 알려준다.

```python
# Each element is an (inputs, label) pair.
w2.train.element_spec
```

```
(TensorSpec(shape=(None, 6, 19), dtype=tf.float32, name=None),
 TensorSpec(shape=(None, 1, 1), dtype=tf.float32, name=None))
```

이후 데이터 셋을 반복하여 배치를 생성한다.

```python
for example_inputs, example_labels in w2.train.take(1):
  print(f'Inputs shape (batch, time, features): {example_inputs.shape}')
  print(f'Labels shape (batch, time, features): {example_labels.shape}')
```

```
Inputs shape (batch, time, features): (32, 6, 19)
Labels shape (batch, time, features): (32, 1, 1)
```

















