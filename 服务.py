from __future__ import annotations
from contextvars import ContextVar as 上下文变量
from pathlib import Path as 路径
from threading import (
    Event as 线程事件,
    Lock as 锁,
    Thread as 线程,
)
from queue import Queue as 队列
from uuid import UUID,uuid4
from time import monotonic as 单调时钟,sleep as 休眠
import builtins
import traceback
from flask import Flask
from flask import request as 请求
from flask_sock import Sock as flaskws
from .js import JavaScript对象,undefined
from dataclasses import dataclass as 数据类,field as 字段
from typing import Any
from .异常 import (
    js错误,
    连接断开,
    非法报文,
    )
from ._内部存储 import 获取内部数据,设置内部数据
from .元素.基础元素 import 元素
from .工具 import python对象服务
import json

################################  ws  ################################

桥接脚本路径=路径(__file__).with_name('桥接脚本.js')

全0UUID=UUID('0'*32)
全1UUID=UUID('1'*32)

def 读取桥接脚本():
    '每次发页面时读磁盘上的脚本。改文件后下一张页面用新内容'
    return 桥接脚本路径.read_text(encoding='utf-8')

def 桥接网页(uuid:str|UUID)->str:
    return f'''\
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>pywebbridge</title>
        <script id="pywebbridge" defer>
        'use strict'

        const 握手密钥='{UUID(uuid).hex}'
        {读取桥接脚本()}
        </script>
    </head>
    <body>
        <div id="pywebbridge-boot">连接中</div>
    </body>
</html>'''

################################  报文封装  ################################

@数据类
class 调用信封:
    操作ID:UUID
    目标:UUID
    操作:str
    参数:dict|list
所有键_调用字典={'操作ID','目标','操作','参数'}

@数据类
class 结果信封:
    操作ID:UUID
    执行成功:bool
    类型:str #数据类型或错误类型
    值:Any #成功时是返回数据,失败时是报错数据(str消息或dict分析数据)
所有键_结果字典={'操作ID','执行成功','类型','值'}

可用类型={
    'undefined',
    'null',
    'string',
    'boolean',
    'symbol',
    'object',
    'bigint',
    'function',
    'json',
    'number',
    #number的↓
    'float',
    'nan',
    'infinity',
    '-infinity',
    '-0',
    }

可进行的操作={
    '读取属性',
    '写入属性',
    '解除引用',
    '创建对象',
    '调用',
}

class 报文处理器:
    def __init__(自身,连接对象:flaskws):
        自身.连接对象=连接对象

    def 接收报文(自身)->调用信封|结果信封:
        '读套接字，解析调用帧或结果帧'
        报文:str|None=自身.连接对象.receive()
        if 报文 is None:
            raise 连接断开('页面连接已断开')
        try:
            帧=json.loads(报文)
        except json.JSONDecodeError:
            raise 非法报文('报文格式错误',报文)
        if not isinstance(帧,dict):
            raise 非法报文('报文格式错误',报文)
        if set(帧.keys())==所有键_结果字典:
            return 解析结果报文(帧)
        if set(帧.keys())==所有键_调用字典:
            return 解析调用报文(帧)
        raise 非法报文('报文格式错误',报文)

    def 发送报文(自身,报文:调用信封|结果信封):
        '把信封编成字典发到套接字'
        match 报文:
            case 调用信封():
                字典={
                    '操作ID':报文.操作ID.hex,
                    '操作目标':报文.目标.hex,
                    '操作':报文.操作,
                    '参数':报文.参数,
                }
            case 结果信封():
                字典={
                    '操作ID':报文.操作ID.hex,
                    '执行成功':报文.执行成功,
                    '类型':报文.类型,
                    '值':报文.值,
                }
            case _:
                raise TypeError(f'报文类型无效: {type(报文).__name__}')
        自身.连接对象.send(json.dumps(字典,ensure_ascii=False))

def 解析调用报文(报文:dict)->调用信封:
    if 报文['操作'] not in 可进行的操作:
        raise 非法报文('操作无效',报文)
    return 调用信封(
        操作ID=UUID(报文['操作ID']),
        目标=UUID(报文['目标']),
        操作=报文['操作'],
        参数=报文['参数']
        )

def 解析结果报文(报文:dict)->结果信封:
    '仅解析数据,不处理内容含义'
    值=报文['值']
    类型=报文['类型']
    match 类型:
        #特殊值
        case 'undefined':
            值=undefined
        case 'null':
            值=None
        case 'nan':
            值=float('nan')
        case 'infinity':
            值=float('inf')
        case '-infinity':
            值=float('-inf')
        case '-0':
            值=float('-0')
        case 'bigint':
            值=int(值)
        #普通值
        case 'object'|'symbol':
            值=UUID(值)
        case 'string':
            值=str(值)
        case 'boolean':
            值=bool(值)
        case 'number':
            值=float(值)
        case 'dict'|'array':
            raise TypeError(f'拒绝类型: {类型}')
        case 'json':
            pass
        case _:
            raise TypeError(f'未知类型: {类型}')
    return 结果信封(
        操作ID=UUID(报文['操作ID']),执行成功=报文['执行成功'],
        类型=类型,值=值 )

def 解析结果语义(结果:结果信封,对象回调)->Any:
    if not 结果.执行成功:
        raise Exception(str(结果.值))
    match 结果.类型:
        case 'undefined':
            return undefined
        case 'null':
            return None
        case 'nan':
            return float('nan')
        case 'infinity':
            return float('inf')
        case '-infinity':
            return float('-inf')
        case '-0':
            return float('-0')
        case 'bigint':
            return int(结果.值)
        case 'object'|'symbol':
            return 对象回调(结果.值)
        case 'string':
            return str(结果.值)
        case 'boolean':
            return bool(结果.值)
        case 'number':
            return float(结果.值)
        case 'dict'|'array':
            raise TypeError(f'拒绝类型: {结果.类型}')
        case 'json':
            return json.loads(结果.值)
        case _:
            raise TypeError(f'未知类型: {结果.类型}')

################################  ?  ################################

安全整数=9007199254740991
当前窗口=上下文变量('当前窗口',default=None)#这条调用所属的页面对象

class 窗口代理:
    '写 window 就用当前线程这份页面对象'
    def __bool__(自身):
        return 当前窗口.get() is not None

    def __getattr__(自身,名称):
        页面=当前窗口.get()
        if 页面 is None:
            raise RuntimeError('没有窗口')
        return getattr(页面,名称)

    def __setattr__(自身,名称,值):
        页面=当前窗口.get()
        if 页面 is None:
            raise RuntimeError('没有窗口')
        setattr(页面,名称,值)

builtins.window=窗口代理()

def 获取请求信息(window):
    '接口无处安放请求信息,又因为对象操作模型(flask的是线程操作)所以只能通过内部数据传递'
    return 获取内部数据(window,'请求信息')

class 桥接连接:
    '一条网页套接字。调用在这里等回复，接收循环不在事件里等待下一次调用'
    def __init__(自身,服务,套接字,窗口=None):
        自身.窗口=窗口#这条套接字对应的页面对象，读取循环启动前就定下
        自身.等待表={}
        自身.等待锁=锁()
        自身.发送锁=锁()
        自身.已断开=False
        自身.断开原因='页面连接已断开'
        自身.收尾事件=线程事件()
        自身.套接字=套接字
        自身.python对象=python对象服务()
        自身.句柄表={}#uuid到包装，强引用
        自身.句柄锁=锁()
        自身.报文=报文处理器(套接字)
        自身.读取线程=线程(target=自身.读取循环)
        自身.读取线程.daemon=True
        自身.读取线程.start()

    def 标记断开(自身,原因='页面连接已断开'):
        '让还在等回复的调用全部醒来'
        with 自身.等待锁:
            if 自身.已断开:
                自身.收尾事件.set()
                return
            自身.已断开=True
            自身.断开原因=原因
            等待项=list(自身.等待表.items())
            自身.等待表.clear()
        for 操作ID,结果队列 in 等待项:
            结果队列.put(结果信封(
                类型='连接断开',
                值=原因,
                操作ID=UUID(操作ID),
                执行成功=False,
            ))
        自身.python对象.池.shutdown(wait=False,cancel_futures=True)
        自身.收尾事件.set()

    def 解码参数(自身,参数):
        '按序号还原页面传来的参数'
        序=[]
        for 键 in 参数:
            if not isinstance(键,str) or not 键.isdigit():
                raise TypeError('回调参数键必须是序号')
            序.append(int(键))
        序.sort()
        结果=[]
        for 序号 in 序:
            结果.append(自身.解码帧(参数[str(序号)]))
        return 结果

    def 解码帧(自身,帧):
        '还原页面编码的一个值。对象变成句柄'
        if not isinstance(帧,dict) or not isinstance(帧.get('类型'),str):
            raise TypeError('值格式不对')
        结果=解析结果报文({
            '类型':帧['类型'],
            '值':帧.get('值'),
            '操作ID':'00000000000000000000000000000000',
            '执行成功':True,
        })
        if 结果.类型 in ('object','symbol','function'):
            return 自身.新建句柄(结果.值)
        return 结果.值

    def 编码值(自身,值):
        '编成页面解码认得的类型和值。页面对象只交uuid，字典和列表按值展开'
        if 值 is undefined:
            return {'类型':'undefined'}
        if 值 is None:
            return {'类型':'null','值':None}
        if isinstance(值,bool):
            return {'类型':'boolean','值':值}
        if isinstance(值,str):
            return {'类型':'string','值':值}
        if isinstance(值,int):
            if -安全整数<=值<=安全整数:
                return {'类型':'number','值':值}
            return {'类型':'bigint','值':str(值)}
        if isinstance(值,float):
            if 值!=值:
                return {'类型':'nan'}
            if 值==float('inf'):
                return {'类型':'infinity'}
            if 值==float('-inf'):
                return {'类型':'-infinity'}
            if 值==0 and str(值).startswith('-'):
                return {'类型':'-0'}
            return {'类型':'number','值':值}
        if isinstance(值,JavaScript对象):
            return {'类型':'object','值':UUID(获取内部数据(值,'uuid')).hex}
        if callable(值):
            return {'类型':'function','值':自身.python对象.注册对象(值)}
        if isinstance(值,元素):
            return 自身.编码值(值.json())
        if isinstance(值,dict):
            内容={}
            for 键,项 in 值.items():
                if not isinstance(键,str):
                    raise TypeError('字典键必须是字符串')
                内容[键]=自身.编码值(项)
            return {'类型':'json','值':内容}
        if isinstance(值,list) or isinstance(值,tuple):
            return {'类型':'json','值':[自身.编码值(项) for 项 in 值]}
        raise TypeError(f'该值不能进入帧: {type(值).__name__}')

    def 新建句柄(自身,标识):
        '同一个uuid始终交回同一个包装'
        if isinstance(标识,UUID):
            文本=标识.hex
        else:
            文本=UUID(标识).hex
        with 自身.句柄锁:
            已有=自身.句柄表.get(文本)
            if 已有 is not None:
                return 已有
            对象=JavaScript对象()
            设置内部数据(对象,'uuid',文本)
            设置内部数据(对象,'所属连接',自身)
            自身.句柄表[文本]=对象
            return 对象

    def 读取循环(自身):
        while True:
            try:
                try:
                    结果=自身.报文.接收报文()
                except Exception as 接收错误:
                    if type(接收错误).__name__!='ConnectionClosed':
                        自身.标记断开(f'页面连接已断开: {接收错误}')
                        raise
                    raise 连接断开('页面连接已断开') from 接收错误
                if type(结果) is 调用信封:
                    操作ID=结果.操作ID
                    def 发回这次结果(执行成功,返回值,操作ID=操作ID):
                        '闭包这次调用的uuid。被调用时把结果信封交给报文处理器'
                        if 执行成功:
                            编码=自身.编码值(返回值)
                            类型=编码['类型']
                            值=编码.get('值')
                        else:
                            类型=type(返回值).__name__
                            值=str(返回值)
                        with 自身.发送锁:
                            自身.报文.发送报文(结果信封(
                                操作ID=操作ID,
                                执行成功=执行成功,
                                类型=类型,
                                值=值,
                            ))
                    令牌=None
                    if 自身.窗口 is not None:
                        令牌=当前窗口.set(自身.窗口)#提交前写入，线程池拷走这份上下文
                    try:
                        try:
                            自身.python对象.调用(
                                *自身.解码参数(结果.参数),
                                目标=结果.目标,
                                结果回调=发回这次结果,
                            )
                        except 连接断开:
                            pass
                        except Exception:
                            traceback.print_exc()
                    finally:
                        if 令牌 is not None:
                            当前窗口.reset(令牌)
                    continue
                if type(结果) is 结果信封:
                    with 自身.等待锁:
                        结果队列=自身.等待表.pop(结果.操作ID.hex,None)
                    if 结果队列 is None:
                        continue
                    结果队列.put(结果)
                    continue
            except 连接断开:
                旧处理器=自身.报文
                旧连接=旧处理器.连接对象
                截止=单调时钟()+5
                已重连=False
                while 单调时钟()<截止:
                    if 自身.报文 is not 旧处理器 or 自身.报文.连接对象 is not 旧连接:
                        已重连=True
                        break
                    休眠(0.05)
                if not 已重连:
                    自身.标记断开()
                    return

    def 发送调用(自身,调用:调用信封)->队列:
        '按信封发给页面，马上返回这个调用的队列。get 阻塞到结果信封'
        if 调用.操作 not in {'调用','写入属性','读取属性','解除引用','创建对象'}:
            raise ValueError(f'无效操作: {调用.操作}')
        if 自身.已断开:
            raise 连接断开(自身.断开原因)
        操作ID=调用.操作ID.hex
        结果队列=队列()
        with 自身.等待锁:
            自身.等待表[操作ID]=结果队列
        try:
            with 自身.发送锁:
                自身.报文.发送报文(调用)
        except Exception as 发送错误:
            with 自身.等待锁:
                自身.等待表.pop(操作ID,None)
            自身.标记断开(f'页面连接已断开: {发送错误}')
            raise 连接断开(自身.断开原因) from 发送错误
        return 结果队列

    def 创建对象(自身,目标:JavaScript对象,参数:list):
        '用 new 创建实例。参数与调用相同'
        目标UUID=获取内部数据(目标,'uuid')
        结果=自身.发送调用(调用信封(
            操作ID=uuid4(),
            操作='创建对象',
            目标=UUID(目标UUID),
            参数=[自身.编码值(项) for 项 in 参数],
        )).get()
        return 解析结果语义(结果,自身.新建句柄)
    def 调用(自身,目标:JavaScript对象,参数:list):
        '调用页面上的对象。参数按位置交给页面'
        目标UUID=获取内部数据(目标,'uuid')
        结果=自身.发送调用(调用信封(
            操作ID=uuid4(),
            操作='调用',
            目标=UUID(目标UUID),
            参数=[自身.编码值(项) for 项 in 参数],
        )).get()
        return 解析结果语义(结果,自身.新建句柄)
    def 写入属性(自身,目标:JavaScript对象,键:str,值:Any):
        '写入页面上的属性'
        目标UUID=获取内部数据(目标,'uuid')
        结果=自身.发送调用(调用信封(
            操作ID=uuid4(),
            操作='写入属性',
            目标=UUID(目标UUID),
            参数={'key':键,'value':自身.编码值(值)},
        )).get()
    def 读取属性(自身,目标:JavaScript对象,键:str):
        '读取页面上的属性'
        目标UUID=获取内部数据(目标,'uuid')
        结果=自身.发送调用(调用信封(
            操作ID=uuid4(),
            操作='读取属性',
            目标=UUID(目标UUID),
            参数={'key':键},
        )).get()
        return 解析结果语义(结果,自身.新建句柄)
    def 解除引用(自身,目标:JavaScript对象):
        '解除引用(为GC预留)'
        return
        目标UUID=获取内部数据(目标,'uuid')
        return 自身.发送调用(调用信封(
            操作ID=uuid4(),
            操作='解除引用',
            目标=UUID(目标UUID),
            参数={'uuid':UUID(目标UUID).hex},
        )).get()

class 桥接服务器(Flask):
    '网页服务。路由函数在页面握手之后收到窗口'
    def __init__(自身,导入名=None):
        super().__init__(导入名 or __name__)
        自身.套接字=flaskws(自身)

    def 桥接页面路由(自身,规则,**选项):
        '桥接的各种存储按路由级存放'
        真添加路由=自身.route(规则,**选项)
        页面表={}#uuid:window
        请求数据缓存={}#uuid:请求
        握手锁=锁()
        def 装饰器(真处理函数):
            def 代理处理函数(*args,**kargs):
                真请求=请求._get_current_object()
                真请求.get_data()#获取之后请求体会缓存
                握手密钥=请求.args.get('握手密钥')
                #原始请求
                if 握手密钥 is None:
                    密钥=uuid4().hex
                    请求数据缓存[密钥]=真请求
                    return 桥接网页(密钥)
                #携带了密钥
                握手密钥=UUID(握手密钥).hex
                with 握手锁:
                    if 握手密钥 in 页面表:#断线重连
                        return 页面表[握手密钥]#?
                    else:#新ws连接
                        页面=JavaScript对象()
                        设置内部数据(页面,'请求信息',真请求)
                        设置内部数据(页面,'uuid',握手密钥)
                        设置内部数据(页面,'所属连接',桥接连接(自身,自身.套接字))
                        页面表[握手密钥]=页面
                return 真处理函数(页面,*args,**kargs)
            真添加路由(代理处理函数)
            def 套接字入口(页面套接字,*位置参数,**关键字参数):
                '这条路由只接升级请求。处理函数返回后保持连接,直到浏览器断开'
                密钥文本=请求.args.get('握手密钥')
                if not 密钥文本:
                    raise RuntimeError('握手密钥缺失')
                密钥=UUID(密钥文本).hex
                已缓存=请求数据缓存.get(密钥)
                if 已缓存 is not None:
                    原始请求=已缓存
                else:
                    原始请求=请求._get_current_object()
                with 握手锁:
                    页面=页面表.get(密钥)
                    if 页面 is None:
                        页面=JavaScript对象()
                        设置内部数据(页面,'uuid',密钥)
                        页面表[密钥]=页面
                连接=桥接连接(自身,页面套接字,窗口=页面)
                设置内部数据(页面,'请求信息',原始请求)
                设置内部数据(页面,'所属连接',连接)
                连接.句柄表[密钥]=页面
                令牌=当前窗口.set(页面)#这条线程上的入口也能读到窗口
                try:
                    真处理函数(页面,*位置参数,**关键字参数)
                    连接.收尾事件.wait()
                except 连接断开 as 断开错误:
                    断开错误=断开错误
                finally:
                    当前窗口.reset(令牌)
                    连接.标记断开()
            套接字路由选项={键:值 for 键,值 in 选项.items() if 键!='endpoint'}
            自身.套接字.route(规则,**套接字路由选项)(套接字入口)
            return 真处理函数
        return 装饰器

    def 启动(自身,主机:str,端口:int,调试=False):
        '阻塞运行服务。调试时按修改时间重载。watchdog 在 Windows 上会把导入报成文件改动'
        自身.run(
            host=主机,
            port=端口,
            threaded=True,
            debug=调试,
            reloader_type='stat',
            )
