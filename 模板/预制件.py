from ..元素.基础元素 import 元素
from abc import ABC,abstractmethod

class 预制件(ABC):
    @abstractmethod
    def json(自身)->dict:
        ...

def 构建():
    ...