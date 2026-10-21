from .数据 import JavaScript对象

class console(JavaScript对象):
    def assert_(自身,condition: bool,message: str|None=None)->None:
        '断言'
        ...

    def clear(自身)->None:
        '清空控制台'
        ...

    def count(自身,label: str|None=None)->None:
        '给这个标签计数并打印'
        ...

    def countReset(自身,label: str|None=None)->None:
        '计数清零'
        ...

    def debug(自身,*data: object)->None:
        '打印调试'
        ...

    def dir(自身,item: object|None=None,options: dict|None=None)->None:
        '打印对象结构。options 可用 depth'
        ...

    def dirxml(自身,*data: object)->None:
        '按 XML 结构打印'
        ...

    def error(自身,*data: object)->None:
        '打印错误'
        ...

    def group(自身,*data: object)->None:
        '开始一组日志'
        ...

    def groupCollapsed(自身,*data: object)->None:
        '开始一组默认折叠的日志'
        ...

    def groupEnd(自身)->None:
        '结束当前组'
        ...

    def info(自身,*data: object)->None:
        '打印信息'
        ...

    def log(自身,*data: object)->None:
        '打印'
        ...

    def table(自身,tabularData: object|None=None,properties: list|None=None)->None:
        '按表格打印'
        ...

    def time(自身,label: str|None=None)->None:
        '开始计时'
        ...

    def timeEnd(自身,label: str|None=None)->None:
        '结束计时并打印'
        ...

    def timeLog(自身,label: str|None=None,*data: object)->None:
        '打印当前计时'
        ...

    def timeStamp(自身,label: str|None=None)->None:
        '在性能时间线打一个点'
        ...

    def trace(自身,*data: object)->None:
        '打印调用栈'
        ...

    def warn(自身,*data: object)->None:
        '打印警告'
        ...