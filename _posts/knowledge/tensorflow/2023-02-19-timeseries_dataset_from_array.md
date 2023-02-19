---
layout: single
title:  'timeseries_dataset_from_array'
toc: true
categories: [TensorFlow]
tags: [tensorflow, timeseries]
---

본 게시물은 tensorflow의 [포스트](https://www.tensorflow.org/api_docs/python/tf/keras/utils/timeseries_dataset_from_array)를 보고 정리하는 글이다.
{: .notice}

```
tf.keras.preprocessing.timeseries_dataset_from_array
```

```python
tf.keras.utils.timeseries_dataset_from_array(
    data,
    targets,
    sequence_length,
    sequence_stride=1,
    sampling_rate=1,
    batch_size=128,
    shuffle=False,
    seed=None,
    start_index=None,
    end_index=None
)
```

이 함수는 동일한 간격으로 수집된 연속된 데이터 포인트를 parameter에 따라 time series의 input 및 output의 batch를 생성한다.

### 📌 Args

- data: 연속된 데이터 포인트들(time step)을 포함하는 Numpy array 또는 eager tensor이다. 0번째 축은 시간 차원.
- targets: 데이터의 timestep에 해당하는 target. target은 첫번째 Input에 대응되는 index부터 시작되어야 한다. None일 경우 Input에 대한 데이터셋만 반환한다. (example 참조)
- sequence_length: output sequence의 길이 (= timestep의 숫자)
- sequence_stride: Input sequence 간의 떨어진 정도. stride 1의 경우 data[0:timestep], data[1:timestep+1], ... 로 구성된다.
- sampling_rate: sequence 내의 timestep의 떨어진 정도. rate 2의 경우 [0, 2, 4, ...] [1, 3, 5 ...] ... 로 구성된다.
- batch_size: batch size
- shuffle: shuffle 여부
- seed: random seed
- start_index: (optional) 유효성 검사를 위해 데이터 일부를 보존함.
- end_index: (optional) 유효성 검사를 위해 데이터 일부를 보존함.

### 📌 Returns

target이 있는 경우 (batch_of_sequences, batch_of_targets)를, 없는 경우 batch_of_sequences를 생성한다.

### 📌 Example

데이터가 scalar 값을 가지는 (steps, ) 형태의 배열일때, 과거 10 timestep을 가지고 다음을 예측하는 예시

```python
data_t = np.array(range(0,100))
input_data = data_t[:-10]
targets = data_t[10:]
dataset = tf.keras.utils.timeseries_dataset_from_array(
    input_data, targets, sequence_length=10)
for batch in dataset:
  inputs, targets = batch
  assert np.array_equal(inputs[0], data_t[:10])  # First sequence: steps [0-9]
  # Corresponding target: step 10
  assert np.array_equal(targets[0], data_t[10])
  break
print(inputs[-1])
print(targets[-1])  
```

```
tf.Tensor([80 81 82 83 84 85 86 87 88 89], shape=(10,), dtype=int64)
tf.Tensor(90, shape=(), dtype=int64)
```
