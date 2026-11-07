class 桥接服务异常(Exception):
    ...

class 连接断开(桥接服务异常):
    ...

class 非法报文(桥接服务异常):
    def __init__(自身,消息,报文):
        自身.消息=消息
        自身.报文=报文

    def __str__(自身):
        return 自身.消息

class js错误(Exception):
    js错误标识='Error'

class 求值错误(js错误):
    js错误标识='EvalError'

class 范围错误(js错误):#待定
    js错误标识='RangeError'

class 引用错误(js错误,NameError):
    js错误标识='ReferenceError'

class 语法错误(js错误,SyntaxError):
    js错误标识='SyntaxError'

class 类型错误(js错误,TypeError):
    js错误标识='TypeError'

class URI错误(js错误):
    js错误标识='URIError'

class 聚合错误(js错误,ExceptionGroup):
    js错误标识='AggregateError'

class 抑制错误(js错误):
    js错误标识='SuppressedError'

class DOM异常(js错误):
    js错误标识='DOMException'

class GPU管线错误(DOM异常):
    js错误标识='GPUPipelineError'

class 身份凭证错误(DOM异常):
    js错误标识='IdentityCredentialError'

class 过约束错误(DOM异常):
    js错误标识='OverconstrainedError'

class 配额超出错误(DOM异常):
    js错误标识='QuotaExceededError'

class 实时通信错误(DOM异常):
    js错误标识='RTCError'

class WebSocket错误(DOM异常):
    js错误标识='WebSocketError'

class WebTransport错误(DOM异常):
    js错误标识='WebTransportError'

class WebAssembly编译错误(js错误):
    js错误标识='WebAssembly.CompileError'

class WebAssembly链接错误(js错误):
    js错误标识='WebAssembly.LinkError'

class WebAssembly运行错误(js错误):
    js错误标识='WebAssembly.RuntimeError'

class WebAssembly挂起错误(js错误):
    js错误标识='WebAssembly.SuspendError'
