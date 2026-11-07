from ._内部存储 import 获取内部数据

all=[
    'Symbol',
    'Undefined',
    '无数据',
    '非数字',
    '正无穷',
    '负无穷',
    '负0',
    'JavaScript对象',
    'window',
    'new',
    '符号',
    ]

#### js中的特殊值 ####
class Symbol:
    'JavaScript 的 symbol。为真，每次新建都不同，不能转成字符串，不能调用，不能写属性'
    def __init__(自身,描述=None):
        object.__setattr__(自身,'描述',描述)

    def __bool__(自身):
        return True

    def __repr__(自身):
        描述=object.__getattribute__(自身,'描述')
        if 描述 is None:
            return 'Symbol()'
        return 'Symbol('+repr(描述)+')'

    def __str__(自身):
        raise TypeError('Cannot convert a Symbol value to a string')

    def __eq__(自身,其他):
        return 其他 is 自身

    def __hash__(自身):
        return hash(id(自身))

    def __call__(自身,*位置参数,**关键词参数):
        raise TypeError('symbol is not a function')

    def __getattr__(自身,名称):
        if 名称=='description':
            描述=object.__getattribute__(自身,'描述')
            if 描述 is None:
                return undefined
            return 描述
        raise TypeError("Cannot read properties of symbol (reading '"+str(名称)+"')")

    def __setattr__(自身,名称,值):
        raise TypeError("Cannot create property '"+str(名称)+"' on symbol '"+repr(自身)+"'")

    def __getitem__(自身,键):
        raise TypeError("Cannot read properties of symbol (reading '"+str(键)+"')")

    def __setitem__(自身,键,值):
        raise TypeError("Cannot create property '"+str(键)+"' on symbol '"+repr(自身)+"'")

    def __iter__(自身):
        raise TypeError(repr(自身)+' is not iterable')

class Undefined:
    'JavaScript 的 undefined。为假，不能调用，不能读写属性'
    def __bool__(自身):
        return False

    def __repr__(自身):
        return 'undefined'

    def __str__(自身):
        return 'undefined'

    def __eq__(自身,其他):
        return 其他 is 自身 or 其他 is None

    def __hash__(自身):
        return hash(None)

    def __call__(自身,*位置参数,**关键词参数):
        raise TypeError('undefined is not a function')

    def __getattr__(自身,名称):
        raise TypeError("Cannot read properties of undefined (reading '"+str(名称)+"')")

    def __setattr__(自身,名称,值):
        raise TypeError("Cannot set properties of undefined (setting '"+str(名称)+"')")

    def __getitem__(自身,键):
        raise TypeError("Cannot read properties of undefined (reading '"+str(键)+"')")

    def __setitem__(自身,键,值):
        raise TypeError("Cannot set properties of undefined (setting '"+str(键)+"')")

    def __iter__(自身):
        raise TypeError('undefined is not iterable')

符号=symbol=Symbol()
无数据=undefined=Undefined()
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
    def __call__(自身,*位置参数):
        连接=获取内部数据(自身,'所属连接',None)
        return 连接.调用(自身,位置参数)

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

    #def __delitem__(自身,键:str):
        #连接=获取内部数据(自身,'所属连接',None)
        #return 连接.解除引用(自身)

def new(构造函数,*位置参数):
    '用 new 创建实例。构造函数是页面上的函数'
    连接=获取内部数据(构造函数,'所属连接')
    return 连接.创建对象(构造函数,list(位置参数))