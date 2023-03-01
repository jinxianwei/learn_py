import importlib
from types import ModuleType
from typing import List

__all__ = ['product']

print('加载rpc包')

def __getattr__(attr: str) -> ModuleType:
    if attr in __all__:
        return importlib.import_module(f'rpc.{attr}')
    
    raise ModuleNotFoundError(f'没有找到{attr}的模块！')


def __dir__(self) -> List:
    return __all__