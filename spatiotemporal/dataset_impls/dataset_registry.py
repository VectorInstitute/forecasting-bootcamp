from functools import partial

from .registry import register_with_dictionary
from .custom_mnist import CustomMNIST
from .custom_cifar10 import CustomCIFAR10 
from .moving_mnist import MovingMnist
from .weatherbench import WeatherBench

DATASET_IMPLEMENTATION_REGISTRY = {}
register = partial(register_with_dictionary, DATASET_IMPLEMENTATION_REGISTRY)


register(CustomMNIST)
register(CustomCIFAR10)
register(MovingMnist)
register(WeatherBench)

def get_dataset_implementation(name):
    return DATASET_IMPLEMENTATION_REGISTRY[name]
