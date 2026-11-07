const 对方引用=new Map()
const 内部数据=new WeakMap()
const 符号数据=new Map()//Symbol不能做WeakMap的键
const 本方函数=new Map()
const 全0标识='00000000000000000000000000000000'
const 全1标识='ffffffffffffffffffffffffffffffff'
const 待执行=[]
let 正在执行=false
let 套接字=null

class 工具{
    static 规范标识(标识){
        '收成32位小写十六进制。全0和全1留给内部，不能当对象'
        if(typeof 标识!=='string') throw new TypeError('uuid必须是字符串')
        const 十六进制=标识.replaceAll('-','').toLowerCase()
        if(!/^[0-9a-f]{32}$/.test(十六进制)) throw new TypeError('uuid格式不对')
        if(十六进制===全0标识||十六进制===全1标识) throw new TypeError('目标ID保留')
        return 十六进制
    }

    static 新标识(){
        '分配对象uuid。撞上保留值就重来'
        let 标识=crypto.randomUUID().replaceAll('-','')
        while(标识===全0标识||标识===全1标识){
            标识=crypto.randomUUID().replaceAll('-','')
        }
        return 标识
    }

    static 登记(对象){
        '同一个对象始终同一个uuid。交出一次加一，解除引用减到零才丢掉'
        const 表=typeof 对象==='symbol'?符号数据:内部数据
        let 数据=表.get(对象)
        if(数据===undefined){
            数据={uuid:工具.新标识(),次数:0}
            表.set(对象,数据)
        }
        if(typeof 数据.次数!=='number') 数据.次数=0
        数据.次数=数据.次数+1
        对方引用.set(数据.uuid,对象)
        return 数据.uuid
    }

    static 取对象(标识){
        '按uuid取对方还引用着的对象'
        const 规范=工具.规范标识(标识)
        if(!对方引用.has(规范)) throw new ReferenceError('没有这个对象')
        return 对方引用.get(规范)
    }

    static 取回调(标识){
        '同一个uuid始终是同一个函数。调用后立刻返回，不在页面上等待'
        const 规范=工具.规范标识(标识)
        let 包装=本方函数.get(规范)
        if(包装===undefined){
            包装=function(...实参){
                const 参数={}
                for(let 序号=0;序号<实参.length;序号++){
                    参数[String(序号)]=工具.编码(实参[序号])
                }
                套接字.send(JSON.stringify({
                    操作ID:工具.新标识(),
                    目标:规范,
                    操作:'调用',
                    参数:参数,
                }))
            }
            本方函数.set(规范,包装)
        }
        return 包装
    }

    static 编码(值){
        '编成类型和值。函数并进object。数组、普通对象、symbol留在页面上，只交uuid'
        if(值===undefined) return {类型:'undefined',值:null}
        if(值===null) return {类型:'null',值:null}
        const 种类=typeof 值
        if(种类==='boolean') return {类型:'boolean',值:值}
        if(种类==='string') return {类型:'string',值:值}
        if(种类==='number'){
            if(Number.isNaN(值)) return {类型:'nan',值:null}
            if(值===Infinity) return {类型:'infinity',值:null}
            if(值===-Infinity) return {类型:'-infinity',值:null}
            if(Object.is(值,-0)) return {类型:'-0',值:null}
            return {类型:'number',值:值}
        }
        if(种类==='bigint') return {类型:'bigint',值:值.toString()}
        if(种类==='symbol') return {类型:'symbol',值:工具.登记(值)}
        if(种类==='object'||种类==='function') return {类型:'object',值:工具.登记(值)}
        throw new TypeError('该值不能进入帧')
    }

    static 解码(帧){
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
                return 工具.取对象(帧.值)
            case 'function':
                return 工具.取回调(帧.值)
            case 'json':{
                if(Array.isArray(帧.值)){
                    const 结果=[]
                    for(let 序号=0;序号<帧.值.length;序号++) 结果.push(工具.解码(帧.值[序号]))
                    return 结果
                }
                if(帧.值===null||typeof 帧.值!=='object') throw new TypeError('json值必须是对象或数组')
                const 结果={}
                for(const 键 of Object.keys(帧.值)) 结果[键]=工具.解码(帧.值[键])
                return 结果
            }
            default:
                throw new TypeError('未知类型:'+帧.类型)
        }
    }

    static 回复成功(操作ID,结果){
        '成功回复。操作ID、执行成功、类型、值四个键都在'
        const 编码结果=工具.编码(结果)
        套接字.send(JSON.stringify({
            操作ID:操作ID,
            执行成功:true,
            类型:编码结果.类型,
            值:Object.prototype.hasOwnProperty.call(编码结果,'值')?编码结果.值:null,
        }))
    }

    static 回复失败(操作ID,错误){
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

    static 显示启动失败(消息){
        '启动块还在时写入错误。脚本在头部执行，页面没解析完就等到解析完'
        const 写入=function(){
            const 启动块=document.getElementById('pywebbridge-boot')
            if(启动块) 启动块.textContent=消息
        }
        if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',写入)
        else 写入()
    }

    static 启动桥接(){
        '带着握手密钥连接当前页面的同一路径。window用这个uuid'
        let 已连上=false
        try{
            const 标识=工具.规范标识(握手密钥)
            内部数据.set(window,{uuid:标识})
            对方引用.set(标识,window)
            const 协议=location.protocol==='https:'?'wss://':'ws://'
            const 查询=new URLSearchParams(location.search)
            查询.set('握手密钥',标识)
            套接字=new WebSocket(协议+location.host+location.pathname+'?'+查询.toString())
            套接字.addEventListener('message',function(帧事件){
                指令集.执行调用(帧事件)
            })
            套接字.addEventListener('open',function(){
                已连上=true
                const 启动块=document.getElementById('pywebbridge-boot')
                if(启动块) 启动块.remove()
            })
            套接字.addEventListener('error',function(错误事件){
                console.error('桥接连接失败',错误事件)
                if(!已连上) 工具.显示启动失败('连接失败')
            })
            套接字.addEventListener('close',function(关闭事件){
                if(已连上) return
                const 原因文本=typeof 关闭事件.reason==='string'&&关闭事件.reason?关闭事件.reason:''
                const 消息=原因文本?`连接失败（${关闭事件.code}）${原因文本}`:`连接失败（${关闭事件.code}）`
                工具.显示启动失败(消息)
                console.error('桥接连接关闭',关闭事件.code,原因文本)
            })
        }catch(错误){
            const 消息文本=错误&&typeof 错误.message==='string'?错误.message:String(错误)
            工具.显示启动失败('连接失败：'+消息文本)
            console.error('桥接启动失败',错误)
        }
    }
}

class 指令集{
    static 读取属性(目标,参数){
        '函数绑在原对象上再交出去，之后调用时this还是这个对象'
        if(typeof 参数.key!=='string') throw new TypeError('读取属性需要key')
        const 键=参数.key
        const 值=目标[键]
        if(typeof 值!=='function') return 值
        if(目标===null||(typeof 目标!=='object'&&typeof 目标!=='function')) return 值
        const 数据=内部数据.get(目标)
        if(数据===undefined) return 值.bind(目标)
        if(数据.绑定函数===undefined) 数据.绑定函数=new Map()
        if(!数据.绑定函数.has(键)) 数据.绑定函数.set(键,值.bind(目标))
        return 数据.绑定函数.get(键)
    }

    static 写入属性(目标,参数){
        '写入属性。这个键上绑过的函数丢掉'
        if(typeof 参数.key!=='string') throw new TypeError('写入属性需要key')
        if(!Object.prototype.hasOwnProperty.call(参数,'value')) throw new TypeError('写入属性需要value')
        目标[参数.key]=工具.解码(参数.value)
        const 数据=内部数据.get(目标)
        if(数据!==undefined&&数据.绑定函数!==undefined) 数据.绑定函数.delete(参数.key)
        return undefined
    }

    static 调用(目标,参数){
        '调用页面上的函数'
        if(typeof 目标!=='function') throw new TypeError('调用目标必须是函数')
        const 实参=[]
        for(const 键 of Object.keys(参数)) 实参.push(工具.解码(参数[键]))
        return 目标.apply(undefined,实参)
    }

    static 创建对象(目标,参数){
        '用 new 创建实例。参数与调用相同'
        if(typeof 目标!=='function') throw new TypeError('创建对象的目标必须是函数')
        const 实参=[]
        for(const 键 of Object.keys(参数)) 实参.push(工具.解码(参数[键]))
        return Reflect.construct(目标,实参)
    }

    static 解除引用(参数){
        '减引用次数。到零才从对照表丢掉'
        if(typeof 参数.uuid!=='string') throw new TypeError('解除引用需要uuid')
        const 规范=工具.规范标识(参数.uuid)
        const 对象=对方引用.get(规范)
        if(对象!==undefined){
            const 表=typeof 对象==='symbol'?符号数据:内部数据
            const 数据=表.get(对象)
            if(数据!==undefined && typeof 数据.次数==='number'){
                数据.次数=数据.次数-1
                if(数据.次数>0) return undefined
                表.delete(对象)
            }
        }
        对方引用.delete(规范)
        return undefined
    }

    static 执行一条(命令){
        '执行一条服务端调用，返回浏览器里的原始结果'
        const 参数=命令.参数
        if(参数===null||typeof 参数!=='object') throw new TypeError('参数必须是对象或数组')
        if(命令.操作==='解除引用') return 指令集.解除引用(参数)
        const 目标=工具.取对象(命令.操作目标)
        if(命令.操作==='读取属性') return 指令集.读取属性(目标,参数)
        if(命令.操作==='写入属性') return 指令集.写入属性(目标,参数)
        if(命令.操作==='调用') return 指令集.调用(目标,参数)
        if(命令.操作==='创建对象') return 指令集.创建对象(目标,参数)
        throw new TypeError('未知操作:'+命令.操作)
    }

    static 执行调用(帧事件){
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
                    工具.回复成功(命令.操作ID,指令集.执行一条(命令))
                }catch(错误){
                    工具.回复失败(命令.操作ID,错误)
                }
            }
        }finally{
            正在执行=false
        }
    }
}

document.创建元素=function(描述){
    '按元素描述执行 createElement,返回根节点'
    const 文档=this
    return 建成(描述)
    function 建成(描述){
        if(typeof 描述==='string') return 文档.createTextNode(描述)
        if(描述===null||typeof 描述!=='object'||Array.isArray(描述)) throw new TypeError('元素描述格式不对')
        if(描述.类型==='jsobj'){
            if(typeof 描述.uuid!=='string') throw new TypeError('已有对象缺少uuid')
            return 工具.取对象(描述.uuid)
        }
        if(typeof 描述.类型!=='string') throw new TypeError('元素描述缺少类型')
        const 节点=文档.createElement(描述.类型)
        const 属性=描述.属性
        if(属性===null||typeof 属性!=='object'||Array.isArray(属性)) throw new TypeError('元素描述缺少属性')
        const 子元素=描述.子元素
        if(!Array.isArray(子元素)) throw new TypeError('元素描述缺少子元素')
        for(const 名 of Object.keys(属性)) 节点[名]=属性[名]
        const 容器=节点.tagName==='TEMPLATE'?节点.content:节点
        for(let 序号=0;序号<子元素.length;序号++) 容器.appendChild(建成(子元素[序号]))
        return 节点
    }
}

工具.启动桥接()
