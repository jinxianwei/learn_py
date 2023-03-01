from dataclasses import dataclass
from typing import List
import time


@dataclass
class Product:
    name: str
    qty: int
    price: float

print('product模块准备中')
time.sleep(5)
print('product模块完成初始化.')

def get_products() -> List[Product]:
    return [
        Product('Apple', 18, 5.8),
        Product('Origin', 8, 23.5)
    ]