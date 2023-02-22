---
layout: single
title:  'LSTM의 모든것 (5) Timeseries forecasting - Modeling'
toc: true
categories: [Deep Learning]
tags: [timeseries, lstm]
---

본 게시물은 Tensorflow의 LSTM을 사용한 [시계열 예측 예제](https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/structured_data/time_series.ipynb#scrollTo=6GmSTHXw6lI1) 내용 모델링을 적용하는 부분을 정리하는 글이다.
{: .notice}

<div class="notice">
<li><a href="https://sigirace.github.io/deep%20learning/LSTM_method///">LSTM의 모든것 (1) LSTM 및 내부 Gate에 대한 이해</a></li>
<li><a href="https://sigirace.github.io/deep%20learning/LSTM_components//">LSTM의 모든것 (2) PyTorch 공식 문서로 보는 구성요소</a></li>
<li><a href="https://sigirace.github.io/deep%20learning/LSTM-time-tutorial//">LSTM의 모든것 (4) Timeseries forecasting - Make Dataset</a></li>  
</div>
## 1. Import dataset

이전 포스트에서 데이터에 대해 전처리와 더불어 학습을 위한 데이터를 반환하는 클래스를 만들었다. 이를 하나의 py 파일로 생성하여 업로드하였으니 만약 새롭게 튜토리얼을 진행하길 원하면 [여기](https://github.com/sigirace/sigirace.github.io/blob/master/_posts/pytorch/LSTM/dataset.py)에서 다운받아 임포트 시킨다.

```python
import dataset as ds
```

## 2. Single step model

가장 간단한 모델은 현재 조건만을 사용하여 1 time step(본 튜토리얼에서는 1시간) 후의 값을 예측하는 것이다. 따라서 1 time step 후의 T (degC)를 예측하는 모델을 구축한다.

🤪[image11]

먼저 위와 같은 single time step의 (input, label) 쌍을 생성하도록 객체를 구성한다.

```python
target = 'T (degC)'
single_step_window = ds.WindowGenerator(
    input_width=1, label_width=1, shift=1, batch_size = 32, target=target,
    label_columns=[target])
single_step_window
```

```
Total window size: 2
Input indices: [0]
Label indices: [1]
Label column name(s): ['T (degC)']
```

생성한 객체는 train, validation, test 데이터 세트로부터 tf.data.Datasets를 생성하므로 쉽게 배치를 얻을 수 있으며 반복 또한 가능하다. 데이터 셋의 예시는 (batch size, time step, features)의 형태를 띄고 있다.

```python
for example_inputs, example_labels in single_step_window.train.take(1):
  print(f'Inputs shape (batch, time, features): {example_inputs.shape}')
  print(f'Labels shape (batch, time, features): {example_labels.shape}')
```

````
Inputs shape (batch, time, features): (32, 1, 19)
Labels shape (batch, time, features): (32, 1, 1)
````

### 2.1 Linear model

하나의 Linear layer를 통해 가장 간단한 모델을 구축한다. 이때 unit의 수는 예측할 time step이다. 현재는 single step에 대한 예측을 하고 있기 때문에 1로 설정한다.

```python
linear = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1)
])

# 샘플 데이터 예시
print('Input shape:', single_step_window.example[0].shape)
print('Output shape:', linear(single_step_window.example[0]).shape)
```

훈련은 모델 및 step size만 바꾸어 여러 조건으로 진행할 것이기 때문에 훈련 절차를 하나의 함수 패키지로 만들어준다.

````python
MAX_EPOCHS = 20
val_performance = {}
performance = {}

def compile_and_fit(model, window, patience=2):
  early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss',
                                                    patience=patience,
                                                    mode='min')

  model.compile(loss=tf.keras.losses.MeanSquaredError(),
                optimizer=tf.keras.optimizers.Adam(),
                metrics=[tf.keras.metrics.MeanAbsoluteError()])

  history = model.fit(window.train, epochs=MAX_EPOCHS,
                      validation_data=window.val,
                      callbacks=[early_stopping])
  return history
````

구축한 모델을 사용하여 훈련을 진행한다.

```python
history = compile_and_fit(linear, single_step_window)

val_performance['Linear'] = linear.evaluate(single_step_window.val)
performance['Linear'] = linear.evaluate(single_step_window.test, verbose=0)
```

```
Epoch 1/20
1534/1534 [==============================] - 8s 5ms/step - loss: 0.0096 - mean_absolute_error: 0.0721 - val_loss: 82249.0547 - val_mean_absolute_error: 286.7191
Epoch 2/20
1534/1534 [==============================] - 6s 4ms/step - loss: 0.0093 - mean_absolute_error: 0.0707 - val_loss: 85541.4922 - val_mean_absolute_error: 292.3961
Epoch 3/20
1534/1534 [==============================] - 7s 4ms/step - loss: 0.0092 - mean_absolute_error: 0.0702 - val_loss: 88454.2031 - val_mean_absolute_error: 297.3310
439/439 [==============================] - 2s 4ms/step - loss: 88454.1797 - mean_absolute_error: 297.3310
```

결과가 썩 좋지 못하나 예측한 내용을 샘플을 확인해본다.

```python
single_step_window.plot(linear)
```

🤪[image12]

Input 데이터 포인트와 output 데이터 포인트 그리고 예측한 데이터 포인트를 확인할 수 있다. 학습 결과와 마찬가지로 좋지 못한 모습이다.

이번엔 step size를 조정하여 24시간의 Input 데이터가 들어갔을 때 24시간 후를 예측하는 데이터 셋을 구성 및 linear model에 대한 학습을 수행한다.

```python
wide_window = WindowGenerator(
    input_width=24, label_width=24, shift=1, batch_size = 32, target=target,
    label_columns=['T (degC)'])

wide_window
```

```
Total window size: 25
Input indices: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
Label indices: [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24]
Label column name(s): ['T (degC)']
```



