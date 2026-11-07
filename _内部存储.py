################################  内部存储  ################################
from weakref import WeakKeyDictionary as 弱引用键字典
from threading import RLock as 锁

未传参=object()#没传默认值

def 生成内部存储():
    '这是为了拦截对内部数据的恶意不规范读写'
    _对象内部数据表=弱引用键字典()
    存储锁=锁()
    def 获取内部数据存储(对象)->dict:
        with 存储锁:
            return _对象内部数据表.setdefault(对象,{})

    def 获取内部数据(对象,键,默认值=未传参):
        '传默认值为dict.get,不然就是dict[]'
        存储=获取内部数据存储(对象)
        if 默认值 is 未传参:
            return 存储[键]
        else:
            return 存储.get(键,默认值)

    def 设置内部数据(对象,键,值):
        'dict[k]=v'
        with 存储锁:
            获取内部数据存储(对象)[键]=值
    def 设置内部数据默认值(对象,键,默认值):
        'dict.setdefault'
        存储=获取内部数据存储(对象)
        with 存储锁:
            return 存储.setdefault(键,默认值)

    def 存在内部键(对象,键)->bool:
        'k in dict'
        return 键 in 获取内部数据存储(对象)
        
    return 获取内部数据,设置内部数据,设置内部数据默认值,存在内部键

获取内部数据,设置内部数据,设置内部数据默认值,存在内部键=生成内部存储()
del 生成内部存储