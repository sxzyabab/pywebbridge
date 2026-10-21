from threading import Thread as 线程
from queue import Queue as 队列
from threading import Lock as 锁

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