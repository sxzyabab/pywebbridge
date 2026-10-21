from __future__ import annotations
from pathlib import Path as 路径
from threading import (
    Event as 线程事件,
    Lock as 锁,
    Thread as 线程,
)
from time import sleep as 等待
from queue import Queue as 队列
from uuid import UUID,uuid4
from concurrent.futures import ThreadPoolExecutor as 线程池
from flask import Flask
from flask import request as 请求
from flask_sock import Sock as 网页套接字
from .数据 import JavaScript对象,undefined
from dataclasses import dataclass as 数据类,field as 字段
from typing import Any
from .异常 import (
    js错误,
    连接断开,
    )
from ._内部存储 import 获取内部数据,设置内部数据

import json
#RecursionError: maximum recursion depth exceeded
################################  ws  ################################

桥接脚本路径=路径(__file__).with_name('桥接脚本.js')

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
        <script id="pywebbridge">
        'use strict'

        const 握手密钥='{UUID(uuid).hex}'
        {读取桥接脚本()}
        </script>
    </head>
    <body>
        <div id="pywebbridge-boot">连接中</div>
    </body>
</html>'''


@数据类
class 调用信封:
    操作:str
    目标:UUID
    参数:dict
    操作ID:UUID=字段(default_factory=uuid4)
@数据类
class 结果信封:
    类型:str #数据类型或错误类型
    值:Any #成功时是返回数据,失败时是报错数据(str消息或dict分析数据)
    操作ID:UUID=字段(default_factory=uuid4)
    执行成功:bool=True
    
可用类型=(
    'undefined',
    'null',
    'string',
    'boolean',
    'symbol',
    'object',
    'bigint',
    'function',
    'number',
    #number的↓
    'float',
    'nan',
    'infinity',
    '-infinity',
    '-0',
    )

class 报文处理器:
    def __init__(自身,连接对象):
        自身.连接对象=连接对象

def 解析报文(数据:dict)->dict:
    ...
def 解析消息(连接,消息:dict)->结果信封:
    '仅解析数据,不处理内容含义'
    值=消息['值']
    类型=消息['类型']
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
        case _:
            raise TypeError(f'未知类型: {类型}')
    return 结果信封(类型=类型,值=值,操作ID=消息['操作ID'],执行成功=消息['执行成功'])

################################  ?  ################################

安全整数=9007199254740991


def 获取请求信息(window):
    '接口无处安放请求信息,又因为对象操作模型(flask的是线程操作)所以只能通过内部数据传递'
    return 获取内部数据(window,'请求信息')

class 桥接连接:
    '一条网页套接字。调用在这里等回复，接收循环不在事件里等待下一次调用'
    def __init__(自身,服务,套接字):
        自身.等待表={}#AI
        自身.等待锁=锁()#AI
        自身.发送锁=锁()#AI
        自身.已断开=False#AI
        自身.断开原因='页面连接已断开'#AI
        自身.收尾事件=线程事件()#AI
        自身.套接字=套接字
        自身.js调用池=线程池(1024)
        自身.js调用池
        自身.读取线程=线程(target=自身.读取循环)
        自身.读取线程.daemon=True#AI
        自身.读取线程.start()

    def 标记断开(自身,原因='页面连接已断开'):#AI
        '让还在等回复的调用全部醒来'#AI
        with 自身.等待锁:#AI
            if 自身.已断开:#AI
                自身.收尾事件.set()#AI
                return#AI
            自身.已断开=True#AI
            自身.断开原因=原因#AI
            等待项=list(自身.等待表.values())#AI
        for 等待 in 等待项:#AI
            等待['断开']=True#AI
            等待['事件'].set()#AI
        自身.收尾事件.set()#AI

    def 编码值(自身,值):#AI
        '编成页面解码认得的类型和值。对象只交uuid'#AI
        if 值 is undefined:#AI
            return {'类型':'undefined'}#AI
        if 值 is None:#AI
            return {'类型':'null','值':None}#AI
        if isinstance(值,bool):#AI
            return {'类型':'boolean','值':值}#AI
        if isinstance(值,str):#AI
            return {'类型':'string','值':值}#AI
        if isinstance(值,int):#AI
            if -安全整数<=值<=安全整数:#AI
                return {'类型':'number','值':值}#AI
            return {'类型':'bigint','值':str(值)}#AI
        if isinstance(值,float):#AI
            if 值!=值:#AI
                return {'类型':'nan'}#AI
            if 值==float('inf'):#AI
                return {'类型':'infinity'}#AI
            if 值==float('-inf'):#AI
                return {'类型':'-infinity'}#AI
            if 值==0 and str(值).startswith('-'):#AI
                return {'类型':'-0'}#AI
            return {'类型':'number','值':值}#AI
        if isinstance(值,JavaScript对象):#AI
            return {'类型':'object','值':UUID(获取内部数据(值,'uuid')).hex}#AI
        raise TypeError(f'该值不能进入帧: {type(值).__name__}')#AI

    def 改写参数(自身,操作,参数):#AI
        '现有几个方法都把操作写成调用。按参数里的键改回页面要的操作'#AI
        if 操作=='调用' and isinstance(参数,dict):#AI
            键集=set(参数)#AI
            if 键集=={'键'} and isinstance(参数.get('键'),str):#AI
                操作='读取属性'#AI
            elif 键集=={'键','值'} and isinstance(参数.get('键'),str):#AI
                操作='写入属性'#AI
            elif 键集=={'uuid'}:#AI
                操作='解除引用'#AI
        if 操作=='读取属性':#AI
            if not isinstance(参数,dict):#AI
                raise TypeError('读取属性需要key')#AI
            键名=参数['key'] if 'key' in 参数 else 参数['键']#AI
            if not isinstance(键名,str):#AI
                raise TypeError('读取属性需要key')#AI
            return '读取属性',{'key':键名}#AI
        if 操作=='写入属性':#AI
            if not isinstance(参数,dict):#AI
                raise TypeError('写入属性需要key')#AI
            键名=参数['key'] if 'key' in 参数 else 参数['键']#AI
            if not isinstance(键名,str):#AI
                raise TypeError('写入属性需要key')#AI
            内容=参数['value'] if 'value' in 参数 else 参数['值']#AI
            return '写入属性',{'key':键名,'value':自身.编码值(内容)}#AI
        if 操作=='解除引用':#AI
            if not isinstance(参数,dict) or 'uuid' not in 参数:#AI
                raise TypeError('解除引用需要uuid')#AI
            return '解除引用',{'uuid':UUID(参数['uuid']).hex}#AI
        if isinstance(参数,list):#AI
            参数={str(序号):项 for 序号,项 in enumerate(参数)}#AI
        if not isinstance(参数,dict):#AI
            raise TypeError('参数必须是对象')#AI
        return '调用',{键:自身.编码值(项) for 键,项 in 参数.items()}#AI

    def 新建句柄(自身,标识):#AI
        '页面交回来的对象。uuid和所属连接写在内部数据里'#AI
        对象=JavaScript对象()#AI
        if isinstance(标识,UUID):#AI
            文本=标识.hex#AI
        else:#AI
            文本=UUID(标识).hex#AI
        设置内部数据(对象,'uuid',文本)#AI
        设置内部数据(对象,'所属连接',自身)#AI
        return 对象#AI

    def 读取循环(自身):
        while not 自身.已断开:#AI
            try:#AI
                if hasattr(自身.套接字,'receive'):#AI
                    原文=自身.套接字.receive()#AI
                else:#AI
                    原文=自身.套接字.recv()#AI
            except Exception as 接收错误:#AI
                自身.标记断开(f'页面连接已断开: {接收错误}')#AI
                if type(接收错误).__name__!='ConnectionClosed':#AI
                    raise#AI
                return#AI
            if 原文 is None:#AI
                自身.标记断开()#AI
                return#AI
            if isinstance(原文,bytes):#AI
                原文=原文.decode('utf-8')#AI
            try:#AI
                帧=json.loads(原文)#AI
            except json.JSONDecodeError as 报文错误:#AI
                continue#AI
            if not isinstance(帧,dict) or '执行成功' not in 帧:#AI
                continue#AI
            操作ID=帧.get('操作ID')#AI
            if not isinstance(操作ID,str):#AI
                continue#AI
            with 自身.等待锁:#AI
                等待=自身.等待表.get(操作ID)#AI
            if 等待 is None:#AI
                continue#AI
            等待['帧']=帧#AI
            等待['事件'].set()#AI

    def 发送调用(自身,操作目标:UUID,操作:str,参数:list|dict):
        目标=UUID(操作目标)
        if 操作 not in {'调用','写入属性','读取属性','解除引用'}:
            raise ValueError(f'无效操作: {操作}')
        if 自身.已断开:#AI
            raise 连接断开(自身.断开原因)#AI
        实际操作,实际参数=自身.改写参数(操作,参数)#AI
        操作ID=uuid4().hex#AI
        帧={#AI
            '操作ID':操作ID,#AI
            '操作目标':目标.hex,#AI
            '操作':实际操作,#AI
            '参数':实际参数,#AI
        }#AI
        等待={'事件':线程事件(),'帧':None,'断开':False}#AI
        with 自身.等待锁:#AI
            自身.等待表[操作ID]=等待#AI
        try:#AI
            报文=json.dumps(帧,ensure_ascii=False)#AI
            try:#AI
                with 自身.发送锁:#AI
                    自身.套接字.send(报文)#AI
            except Exception as 发送错误:#AI
                自身.标记断开(f'页面连接已断开: {发送错误}')#AI
                raise 连接断开(自身.断开原因) from 发送错误#AI
            等待['事件'].wait()#AI
            if 等待['帧'] is None:#AI
                raise 连接断开(自身.断开原因)#AI
            回复=等待['帧']#AI
            if not 回复.get('执行成功',False):#AI
                类型名=回复.get('类型') or 'Error'#AI
                消息=回复.get('值')#AI
                if not isinstance(消息,str):#AI
                    消息='' if 消息 is None else str(消息)#AI
                raise js错误(消息)#AI
            if '值' not in 回复:#AI
                回复={**回复,'值':None}#AI
            结果=解析消息(自身,回复)#AI
            if 结果.类型 in ('object','symbol','function'):#AI
                return 自身.新建句柄(结果.值)#AI
            return 结果.值#AI
        finally:#AI
            with 自身.等待锁:#AI
                自身.等待表.pop(操作ID,None)#AI
            
    def 调用(自身,目标:JavaScript对象,参数:list):
        '调用页面上的对象。参数是报文处理器解析后的参数'
        目标UUID=获取内部数据(目标,'uuid')
        return 自身.发送调用(#会自动生成调用uuid并阻塞等待结果返回
            操作目标=目标UUID,
            操作="调用",
            参数=参数
        )
    def 写入属性(自身,目标:JavaScript对象,键:str,值:Any):
        '写入页面上的属性'
        目标UUID=获取内部数据(目标,'uuid')
        return 自身.发送调用(#会自动生成调用uuid并阻塞等待结果返回
            操作目标=目标UUID,
            操作="调用",
            参数={'键':键,'值':值}
        )
    def 读取属性(自身,目标:JavaScript对象,键:str):
        '读取页面上的属性'
        目标UUID=获取内部数据(目标,'uuid')
        return 自身.发送调用(#会自动生成调用uuid并阻塞等待结果返回
            操作目标=目标UUID,
            操作="调用",
            参数={'键':键}
        )
    def 解除引用(自身,目标:JavaScript对象):
        '解除引用(为GC预留)'
        目标UUID=获取内部数据(目标,'uuid')
        return 自身.发送调用(#会自动生成调用uuid并阻塞等待结果返回
            操作目标=目标UUID,
            操作="调用",
            参数={'uuid':目标UUID}
        )

class 服务器(Flask):
    '网页服务。路由函数在页面握手之后收到窗口'
    def __init__(自身,导入名=None):
        super().__init__(导入名 or __name__)
        自身.套接字=网页套接字(自身)

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
            def 套接字入口(页面套接字,*位置参数,**关键字参数):#AI
                '这条路由只接升级请求。处理函数返回后保持连接,直到浏览器断开'#AI
                密钥文本=请求.args.get('握手密钥')#AI
                if not 密钥文本:#AI
                    raise RuntimeError('握手密钥缺失')#AI
                密钥=UUID(密钥文本).hex#AI
                连接=桥接连接(自身,页面套接字)#AI
                原始请求=请求._get_current_object()#AI
                原始请求.get_data()#AI
                已缓存=请求数据缓存.get(密钥)#AI
                if 已缓存 is not None:#AI
                    原始请求=已缓存#AI
                with 握手锁:#AI
                    页面=页面表.get(密钥)#AI
                    if 页面 is None:#AI
                        页面=JavaScript对象()#AI
                        设置内部数据(页面,'uuid',密钥)#AI
                        页面表[密钥]=页面#AI
                    设置内部数据(页面,'请求信息',原始请求)#AI
                    设置内部数据(页面,'所属连接',连接)#AI
                try:#AI
                    真处理函数(页面,*位置参数,**关键字参数)#AI
                    连接.收尾事件.wait()#AI
                except 连接断开 as 断开错误:#AI
                    断开错误=断开错误#AI
                finally:#AI
                    连接.标记断开()#AI
            套接字路由选项={键:值 for 键,值 in 选项.items() if 键!='endpoint'}#AI
            自身.套接字.route(规则,**套接字路由选项)(套接字入口)#AI
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
