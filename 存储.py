from .数据 import JavaScript对象

class 网页存储(JavaScript对象):
    存储类型:str='Storage'
    @property
    def length(自身)->int:
        return len(自身)

    def key(自身,index:int)->str|None:
        '越界返回None'
        ...

    def getItem(自身,key:str)->str|None:
        '按键读取，没有是 None'
        return 自身[key]

    def setItem(自身,key: str,value: str)->None:
        '按键写入'
        自身[key]=value

    def removeItem(自身,key: str)->None:
        '按键删除,不存在不报错'
        del 自身[key]

    def clear(自身)->None:
        '全部删除'
        ...

    def __getitem__(自身,key:str)->str:
        ...

    def __setitem__(自身,key:str,value:str)->None:
        ...

    def __delitem__(自身,key:str)->None:
        ...

    def __len__(自身)->int:
        ...

    def __iter__(自身)->iter:
        ...

    def __contains__(自身,key:str)->bool:
        ...

class localStorage(网页存储):
    '长期本地存储'
    存储类型='localStorage'

class sessionStorage(网页存储):
    '这个标签页关掉就没的存储'
    存储类型='sessionStorage'
