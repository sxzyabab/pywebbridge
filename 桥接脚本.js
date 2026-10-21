const 对方引用=new Map()
const 内部数据=new WeakMap()
const 全0标识='00000000000000000000000000000000'
const 全1标识='ffffffffffffffffffffffffffffffff'
const 待执行=[]
let 正在执行=false
let 套接字=null

function 规范标识(标识){
    '收成32位小写十六进制。全0和全1留给内部，不能当对象'
    if(typeof 标识!=='string') throw new TypeError('uuid必须是字符串')
    const 十六进制=标识.replaceAll('-','').toLowerCase()
    if(!/^[0-9a-f]{32}$/.test(十六进制)) throw new TypeError('uuid格式不对')
    if(十六进制===全0标识||十六进制===全1标识) throw new TypeError('目标ID保留')
    return 十六进制
}

function 新标识(){
    '分配对象uuid。撞上保留值就重来'
    let 标识=crypto.randomUUID().replaceAll('-','')
    while(标识===全0标识||标识===全1标识){
        标识=crypto.randomUUID().replaceAll('-','')
    }
    return 标识
}

function 登记(对象){
    '对方会拿着这个对象，强引用留到解除引用。同一个对象始终同一个uuid'
    let 数据=内部数据.get(对象)
    if(数据===undefined){
        数据={uuid:新标识()}
        内部数据.set(对象,数据)
    }
    对方引用.set(数据.uuid,对象)
    return 数据.uuid
}

function 取对象(标识){
    '按uuid取对方还引用着的对象'
    const 规范=规范标识(标识)
    if(!对方引用.has(规范)) throw new ReferenceError('没有这个对象')
    return 对方引用.get(规范)
}

function 编码(值){
    '编成类型和值。函数并进object。数组、普通对象、symbol留在页面上，只交uuid'
    if(值===undefined) return {类型:'undefined'}
    if(值===null) return {类型:'null',值:null}
    const 种类=typeof 值
    if(种类==='boolean') return {类型:'boolean',值:值}
    if(种类==='string') return {类型:'string',值:值}
    if(种类==='number'){
        if(Number.isNaN(值)) return {类型:'nan'}
        if(值===Infinity) return {类型:'infinity'}
        if(值===-Infinity) return {类型:'-infinity'}
        if(Object.is(值,-0)) return {类型:'-0'}
        return {类型:'number',值:值}
    }
    if(种类==='bigint') return {类型:'bigint',值:值.toString()}
    if(种类==='symbol') return {类型:'symbol',值:登记(值)}
    if(种类==='object'||种类==='function') return {类型:'object',值:登记(值)}
    throw new TypeError('该值不能进入帧')
}

function 解码(帧){
    '还原一个值。JSON标量原样用，其余看类型'
    if(帧===null) return null
    const 种类=typeof 帧
    if(种类==='boolean'||种类==='string'||种类==='number') return 帧
    if(种类!=='object'||Array.isArray(帧)) throw new TypeError('值格式不对')
    if(typeof 帧.类型!=='string') throw new TypeError('值缺少类型')
    switch(帧.类型){
        case 'string':
        case 'boolean':
        case 'number':
            return 帧.值
        case 'null':
            return null
        case 'undefined':
            return undefined
        case 'nan':
            return NaN
        case 'infinity':
            return Infinity
        case '-infinity':
            return -Infinity
        case '-0':
            return -0
        case 'bigint':
            return BigInt(帧.值)
        case 'object':
        case 'symbol':
            return 取对象(帧.值)
        default:
            throw new TypeError('未知类型:'+帧.类型)
    }
}

function 回复成功(操作ID,结果){
    '成功回复。类型和值在帧顶层，特殊数字不带值'
    const 编码结果=编码(结果)
    const 帧={操作ID:操作ID,执行成功:true,类型:编码结果.类型}
    if(Object.prototype.hasOwnProperty.call(编码结果,'值')) 帧.值=编码结果.值
    套接字.send(JSON.stringify(帧))
}

function 回复失败(操作ID,错误){
    '失败时类型是错误名，值是消息'
    const 类型名=错误&&typeof 错误.name==='string'&&错误.name?错误.name:'Error'
    const 消息文本=错误&&typeof 错误.message==='string'?错误.message:String(错误)
    套接字.send(JSON.stringify({
        操作ID:操作ID,
        执行成功:false,
        类型:类型名,
        值:消息文本,
    }))
}

function 执行调用(帧事件){
    '按收到的顺序执行，一条回复送出之后才执行下一条'
    const 消息=JSON.parse(帧事件.data)
    if(!消息.操作) return
    待执行.push(消息)
    if(正在执行) return
    正在执行=true
    try{
        while(待执行.length>0){
            const 命令=待执行.shift()
            if(typeof 命令.操作ID!=='string'){
                console.error('桥接收到的调用没有操作ID',命令)
                continue
            }
            try{
                回复成功(命令.操作ID,执行一条(命令))
            }catch(错误){
                回复失败(命令.操作ID,错误)
            }
        }
    }finally{
        正在执行=false
    }
    function 执行一条(命令){
        '执行一条服务端调用，返回浏览器里的原始结果'
        const 参数=命令.参数
        if(参数===null||typeof 参数!=='object'||Array.isArray(参数)) throw new TypeError('参数必须是对象')
        if(命令.操作==='解除引用'){
            if(typeof 参数.uuid!=='string') throw new TypeError('解除引用需要uuid')
            对方引用.delete(规范标识(参数.uuid))
            return undefined
        }
        const 目标=取对象(命令.操作目标)
        if(命令.操作==='读取属性'){
            if(typeof 参数.key!=='string') throw new TypeError('读取属性需要key')
            return 读取属性(目标,参数.key)
        }
        if(命令.操作==='写入属性'){
            if(typeof 参数.key!=='string') throw new TypeError('写入属性需要key')
            if(!Object.prototype.hasOwnProperty.call(参数,'value')) throw new TypeError('写入属性需要value')
            目标[参数.key]=解码(参数.value)
            const 数据=内部数据.get(目标)
            if(数据!==undefined&&数据.绑定函数!==undefined) 数据.绑定函数.delete(参数.key)
            return undefined
        }
        if(命令.操作==='调用'){
            if(typeof 目标!=='function') throw new TypeError('调用目标必须是函数')
            const 实参=[]
            for(const 键 of Object.keys(参数)) 实参.push(解码(参数[键]))
            return 目标.apply(undefined,实参)
        }
        throw new TypeError('未知操作:'+命令.操作)
    }
}

function 读取属性(目标,键){
    '函数绑在原对象上再交出去，之后调用时this还是这个对象'
    const 值=目标[键]
    if(typeof 值!=='function') return 值
    const 数据=内部数据.get(目标)
    if(数据.绑定函数===undefined) 数据.绑定函数=new Map()
    if(!数据.绑定函数.has(键)) 数据.绑定函数.set(键,值.bind(目标))
    return 数据.绑定函数.get(键)
}

function 显示启动失败(消息){
    '启动块还在时写入错误。脚本在头部执行，页面没解析完就等到解析完'
    const 写入=function(){
        const 启动块=document.getElementById('pywebbridge-boot')
        if(启动块) 启动块.textContent=消息
    }
    if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',写入)
    else 写入()
}

function 启动桥接(){
    '带着握手密钥连接当前页面的同一路径。window用这个uuid'
    let 已连上=false
    try{
        const 标识=规范标识(握手密钥)
        内部数据.set(window,{uuid:标识})
        对方引用.set(标识,window)
        const 协议=location.protocol==='https:'?'wss://':'ws://'
        const 查询=new URLSearchParams(location.search)
        查询.set('握手密钥',标识)
        套接字=new WebSocket(协议+location.host+location.pathname+'?'+查询.toString())
        套接字.addEventListener('message',执行调用)
        套接字.addEventListener('open',function(){
            已连上=true
            const 启动块=document.getElementById('pywebbridge-boot')
            if(启动块) 启动块.remove()
        })
        套接字.addEventListener('error',function(错误事件){
            console.error('桥接连接失败',错误事件)
            if(!已连上) 显示启动失败('连接失败')
        })
        套接字.addEventListener('close',function(关闭事件){
            if(已连上) return
            const 原因文本=typeof 关闭事件.reason==='string'&&关闭事件.reason?关闭事件.reason:''
            const 消息=原因文本?`连接失败（${关闭事件.code}）${原因文本}`:`连接失败（${关闭事件.code}）`
            显示启动失败(消息)
            console.error('桥接连接关闭',关闭事件.code,原因文本)
        })
    }catch(错误){
        const 消息文本=错误&&typeof 错误.message==='string'?错误.message:String(错误)
        显示启动失败('连接失败：'+消息文本)
        console.error('桥接启动失败',错误)
    }
}

启动桥接()
