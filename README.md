PyTorchViz
==========

**This is a fork of the original package `torchviz`, which is no longer maintained.**

A small package to create visualizations of PyTorch execution graphs and traces.

## Installation

Install graphviz, e.g.:

```
brew install graphviz
```

Install the package itself:

```
pip install torchviz2
```


## Usage
Example usage of `make_dot`:
```
import torch
from torch import nn
from torchviz import make_dot

model = nn.Sequential()
model.add_module('W0', nn.Linear(8, 16))
model.add_module('tanh', nn.Tanh())
model.add_module('W1', nn.Linear(16, 1))

x = torch.randn(1, 8)
y = model(x)

make_dot(y.mean(), params=dict(model.named_parameters()))
```
![image](https://user-images.githubusercontent.com/13428986/110844921-ff3f7500-8277-11eb-912e-3ba03623fdf5.png)

Set `show_attrs=True` and `show_saved=True` to see what autograd saves for the backward pass. (Note that this is only available for pytorch >= 1.9.)
```
model = nn.Sequential()
model.add_module('W0', nn.Linear(8, 16))
model.add_module('tanh', nn.Tanh())
model.add_module('W1', nn.Linear(16, 1))

x = torch.randn(1, 8)
y = model(x)

make_dot(y.mean(), params=dict(model.named_parameters()), show_attrs=True, show_saved=True)
```
![image](https://user-images.githubusercontent.com/13428986/110845186-4ded0f00-8278-11eb-88d2-cc33413bb261.png)