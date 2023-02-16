

wnadb 사용법: https://minimin2.tistory.com/186

early stopping: https://velog.io/@jg31109/Early-stopping

reducelronplateau: https://bo-10000.tistory.com/95

그래디언트 클리핑: https://kh-kim.gitbook.io/natural-language-processing-with-pytorch/00-cover-6/05-gradient-clipping

wandb lstm 예시: https://wandb.ai/wandb_fc/korean/reports/PyTorch-LSTM---VmlldzoyNDc4NjY4#%EC%83%98%ED%94%8C-%EB%AA%A8%EB%8D%B8-%EC%BD%94%EB%93%9C

lstm 코드 구현: https://ok-lab.tistory.com/209

lstm 코드 구현: https://notebook.community/jhjungCode/pytorch-tutorial/16_MNIST-RNN(LSTM)

initialization PyTorch: https://gist.github.com/SauravMaheshkar/5704edf87c33ab09033dc9c0a10adaa1

gradient histogram: https://stackoverflow.com/questions/42315202/understanding-tensorboard-weight-histograms

gradient: https://sdolnote.tistory.com/entry/Gradient

many to one: https://discuss.pytorch.org/t/many-to-one-lstm-input-shape/142468

one to many: https://discuss.pytorch.org/t/how-to-create-a-lstm-with-one-to-many/108659/4

keras: https://stackoverflow.com/questions/52138290/how-can-we-define-one-to-one-one-to-many-many-to-one-and-many-to-many-lstm-ne/52139618#52139618

return_sequence: https://stackoverflow.com/questions/62204109/return-sequences-false-equivalent-in-pytorch-lstm

keras -ml : https://machinelearningmastery.com/timedistributed-layer-for-long-short-term-memory-networks-in-python/

TimeDistributed: https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=chunjein&logNo=221589624838

LSTM AE : https://data-newbie.tistory.com/136

https://data-newbie.tistory.com/567

LSTM-KERAS (KR): https://yjjo.tistory.com/32





timedistributed:

https://stackoverflow.com/questions/47305618/what-is-the-role-of-timedistributed-layer-in-keras

https://medium.com/smileinnovation/how-to-work-with-time-distributed-data-in-a-neural-network-b8b39aa4ce00

https://study-grow.tistory.com/entry/pytorch-pytorch-cross-entropy-%EC%82%AC%EC%9A%A9%EC%8B%9C-%EC%A3%BC%EC%9D%98%ED%95%A0-%EC%A0%90-tf-sparse-categorical-cross-entropy-in-pytorch



autograd: https://velog.io/@olxtar/PyTorch-Autograd

https://gist.github.com/jonlachmann/5cd68c9667a99e4f89edc0c307f94ddb

https://stackoverflow.com/questions/70968393/pytorch-many-to-many-time-series-lstm-always-predicts-the-mean



I have a questions about implementation of many-to-many lstm.
Currently, I'm converting codes implemented in Keras into pytorch, but understanding of output dimension are holding me back.
Below are the questions about it.

[enter image description here](https://i.stack.imgur.com/9jZFC.png)

**What is the difference between timedistributed and linear?**

Below are TimeDistributed Reference as described in Keras documents and other publications

“This wrapper allows to apply a layer to every temporal slice of an input.”
“TimeDistributedDense applies a same Dense (fully-connected) operation to every timestep of a 3D tensor.” 

So, I understand it conceptually means calculating cost for each time step and backpropagating the error to early steps to update weight.

This is an example of the difference between TimeDistributed and Dense(Linear).

- [Keras] many-to-many lstm using TimeDistributed layer

```
 from keras.models import Model
 from keras.layers import Input, Dense, LSTM, TimeDistributed
 import numpy as np


 x = np.array([[[1.], [2.], [3.], [4.], [5.]]])
 y = np.array([[[2.], [3.], [4.], [5.], [6.]]])
 xInput = Input(batch_shape=(None, 5, 1))
 xLstm = LSTM(3, return_sequences=True)(xInput)
 xOutput = TimeDistributed(Dense(1))(xLstm)
 model = Model(xInput, xOutput)
 model.compile(loss='mean_squared_error', optimizer='adam')
 print(model.summary)
```

[enter image description here](https://i.stack.imgur.com/YvQrJ.png)

- [Keras] many-to-many lstm using Dense layer

```
 xInput = Input(batch_shape=(None, 5, 1))
 xLstm = LSTM(3, return_sequences=True)(xInput)
 xOutput = Dense(1)(xLstm)
 model = Model(xInput, xOutput)
 model.compile(loss='mean_squared_error', optimizer='adam')
 print(model.summary())
```

[enter image description here](https://i.stack.imgur.com/BA2S9.png)

Now it's my turn to implement this as Pytorch.
Pytorch does not provide a module for timedistributed, so it refers to the code created by a great developer.

```
class TimeDistributed(nn.Module):
    def __init__(self, module, batch_first=False):
        super(TimeDistributed, self).__init__()
        self.module = module
        self.batch_first = batch_first

    def forward(self, x):
        if len(x.size()) <= 2:
            return self.module(x)
        # Squash samples and timesteps into a single axis
        x_reshape = x.contiguous().view(-1, x.size(-1))  # (samples * timesteps, hidden_size)
        y = self.module(x_reshape)
        # We have to reshape Y
        if self.batch_first:
            y = y.contiguous().view(x.size(0), -1, y.size(-1))  # (samples, timesteps, output_size)
        else:
            y = y.view(-1, x.size(1), y.size(-1))  # (timesteps, samples, output_size)
        return y

```

In this code, I have a question.

If nn.Linear(hidden_size, output_size) layer is connected next to LSTM layer, not TimeDistributed layer, It seems to be no difference in calculation as well as results.

[Linear layer]
calculate: (samples, timesteps, hidden_size) * (hidden_size, output_size)
output: (samples, timesteps, output_size)

[TimeDistributed]
calculate: (samples * timesteps, hidden_size) * (hidden_size, output_size)
output: (samples, timesteps, output_size)

Therefore, I'm very curious about how TimeDistributed's error propagation process at each time steps.
(...And if there is no difference with linear layer, is it okay to just use it?)



please answer the questions!🥲




I ask about some parts of the implementation of many-to-manilstm that I can't understand.



**2. Forecast for subsequent time steps**

[enter image description here](https://i.stack.imgur.com/pbrGT.png)

Which input sequence should I configure in this case of many-to-many type?

Should I repeat the last input of the sequence using repeat vector like one-to-many?

In addition, in the case of output, do I need to derive the result using slice like [:,n:-1,:?]?
