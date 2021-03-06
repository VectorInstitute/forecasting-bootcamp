import torch
import torch.nn as nn


class MultiInputSequential(nn.Sequential):
    def forward(self, *inputs):
        for module in self._modules.values():
            if isinstance(inputs, tuple):
                inputs = module(*inputs)
            else:
                inputs = module(inputs)
        return inputs

def boolean_string(s: str) -> bool:
    if s not in {"True", "False"}:
        raise ValueError("Not a proper boolean string")
    else:
        return s == "True"
