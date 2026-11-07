from contextvars import copy_context as 复制上下文
from queue import Queue as 队列
from threading import Lock as 锁,Semaphore as 信号量,Thread as 线程
import inspect
from uuid import UUID,uuid4
from concurrent.futures import ThreadPoolExecutor
from ._内部存储 import 设置内部数据默认值

class 工人线程(线程):
    '跑完一次调用就回到池里等下一次'
    def __init__(自身,池):
        super().__init__(daemon=True)
        自身.所属线程池:无上限线程池=池
        自身.待执行=队列()

    def run(自身):
        while True:
            函数,位置参数=自身.待执行.get()
            try:
                函数(*位置参数)
            except Exception:
                import traceback
                traceback.print_exc()
            with 自身.所属线程池.调度锁:
                自身.所属线程池.空闲线程.append(自身)

class 无上限线程池:
    '没有空闲线程就新建。线程数停在同时卡住的最高数量'
    def __init__(自身):
        自身.空闲线程=[]
        自身.调度锁=锁()

    def 提交(自身,函数,*位置参数):
        with 自身.调度锁:
            if 自身.空闲线程:
                工人=自身.空闲线程.pop()
            else:
                工人=工人线程(自身)
                工人.start()
        工人.待执行.put((函数,位置参数))

def 存在仅关键字参数(函数)->bool:
    '函数参数存在仅关键字参数'
    if not inspect.isfunction(函数):
        raise ValueError('非函数')
    函数签名=inspect.signature(函数)
    return any(参数.kind==inspect.Parameter.KEYWORD_ONLY for 参数 in 函数签名.parameters.values())

class 线程池(ThreadPoolExecutor):
    @property
    def 空闲线程数(自身)->int:
        信号=getattr(自身,"_idle_semaphore",None)
        if not isinstance(信号,信号量):
            raise NotImplementedError(
                "当前 Python 实现的 ThreadPoolExecutor 没有 _idle_semaphore"
            )
        return max(0,信号._value)

    @property
    def 工作中线程数(自身)->int:
        return max(0,自身.已创建线程数-自身.空闲线程数)

    @property
    def 已创建线程数(自身)->int:
        return sum(1
        for t in tuple(自身._threads)
        if t.is_alive())

    @property
    def 剩余可创建线程数(自身)->int:
        return max(0,自身._max_workers-自身.已创建线程数)

    @property
    def 队列中任务计数(自身)->int:
        try:
            return 自身._work_queue.qsize()
        except (AttributeError, NotImplementedError):
            return -1

    def 状态(自身)->dict:
        return {
            "最大线程数":自身._max_workers,
            "已创建线程数":自身.已创建线程数,
            "剩余可创建线程数":自身.剩余可创建线程数,
            "空闲线程": 自身.空闲线程数,
            "忙碌线程": 自身.工作中线程数,
            "队列中任务计数":自身.队列中任务计数,
        }

################################  js调用py  ################################

回调接口='def 执行结果回调(执行成功:bool,结果:any)->None:'#没成功时结果为错误

class python对象服务:
    '页面调用已登记的Python函数。同时没结束的调用不超过1024'
    def __init__(自身):
        自身.池=线程池(1024)
        自身.注册表={}
        自身.函数锁=锁()

    def 注册对象(自身,对象)->UUID:
        with 自身.函数锁:
            ID=设置内部数据默认值(对象,'uuid',uuid4().hex)
            自身.注册表[ID]=对象
            return ID

    def 查询对象(自身,对象id:UUID|str)->any:
        ID=UUID(对象id).hex
        with 自身.函数锁:
            return 自身.注册表[ID]

    def 调用(自身,*位置参数,目标:UUID|str,结果回调):
        '提交到线程池。已有1024个调用还没结束时抛出递归上限。结果回调收到是否成功和结果，没成功时结果是错误'
        if 自身.池.空闲线程数+自身.池.剩余可创建线程数<=0:
            raise RecursionError('递归达上限')
        ID=UUID(目标).hex if isinstance(目标,str) else 目标.hex
        上下文=复制上下文()#带上读取循环刚写入的当前窗口
        任务=自身.池.submit(上下文.run,自身.注册表[ID],*位置参数)
        def 完成回调(任务):
            try:
                结果回调(True,任务.result())
            except Exception as e:
                import traceback
                traceback.print_exc()
                结果回调(False,e)
        任务.add_done_callback(完成回调)



from collections import deque as 队列

class 可监听变量:
    ...
    def 订阅变化通知()->订阅:
        ...

class 可监听数值(可监听变量):
    ...

class 可监听列表(可监听变量):
    ...

class 可监听字典(可监听变量):
    ...



class 订阅(队列):
    def 获取消息():
        ...
    def 注册消息处理器():
        ...



#uuid类
def 非保留uuid():
    while True:
        ID=uuid4().hex
        if ID!='0'*32 and ID!='1'*32:
            return ID
def 对象引用uuid():
    return '0bec'+非保留uuid()[4:]

def 调用uuid():
    return 'ca11'+非保留uuid()[4:]

def 整体缩进(文本:str,缩进:int,缩进类型=' ')->str:
    '将文本按行缩进'
    return '\n'.join(f'{缩进类型*缩进}{line}' for line in 文本.splitlines())