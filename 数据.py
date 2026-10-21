from ._内部存储 import 获取内部数据

#### js中的特殊值 ####
class Symbol:...

无数据=undefined=object()
非数字=NaN=float('nan')
正无穷=Infinity=float('inf')
负无穷=_Infinity=float('-inf')
负0=float('-0')

数据类型映射={#js:python
    'undefined':None,#?
    'null':None,
    'string':str,
    'boolean':bool,
    'symbol':Symbol,
    'Object':object,
    'bigint':int,
    'function':type(获取内部数据),
    'number':{#float
        'float':float,
        'NaN':float('nan'),
        'Infinity':float('inf'),#正无穷
        '-Infinity':float('-inf'),#负无穷
        '-0':float('-0'),#负0,仅带个符号
    },
}

class JavaScript对象:
    getOwnPropertySymbols:...
    def __call__(自身,*位置参数,**关键词参数):#AI
        连接=获取内部数据(自身,'所属连接',None)
        参数={str(序号):值 for 序号,值 in enumerate(位置参数)}
        参数.update(关键词参数)
        return 连接.调用(自身,参数)

    def __getitem__(自身,键):
        名称=键 if isinstance(键,str) else str(键)
        连接=获取内部数据(自身,'所属连接',None)
        return 连接.读取属性(自身,名称)

    def __getattribute__(自身,键:str):
        名称=键 if isinstance(键,str) else str(键)
        连接=获取内部数据(自身,'所属连接',None)
        return 连接.读取属性(自身,名称)

    def __setitem__(自身,键,值):
        名称=键 if isinstance(键,str) else str(键)
        连接=获取内部数据(自身,'所属连接')
        连接.写入属性(自身,名称,值)

    def __setattr__(自身,键,值):
        名称=键 if isinstance(键,str) else str(键)
        连接=获取内部数据(自身,'所属连接')
        连接.写入属性(自身,名称,值)

    def __delitem__(自身,键:str):
        连接=获取内部数据(自身,'所属连接',None)
        return 连接.解除引用(自身)



