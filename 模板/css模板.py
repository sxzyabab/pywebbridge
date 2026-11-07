'中文和标准 css 都能解析、改写、再生成标准 css。不碰页面，也不碰 js'

class 样式错误(Exception):
    'css 写错了'

属性名={
    '显示':'display',
    '位置':'position',
    '上':'top',
    '右':'right',
    '下':'bottom',
    '左':'left',
    '层叠':'z-index',
    '浮动':'float',
    '清除':'clear',
    '溢出':'overflow',
    '横向溢出':'overflow-x',
    '纵向溢出':'overflow-y',
    '可见性':'visibility',
    '盒模型':'box-sizing',
    '弹性':'flex',
    '弹性方向':'flex-direction',
    '弹性换行':'flex-wrap',
    '伸展':'flex-grow',
    '收缩':'flex-shrink',
    '弹性基准':'flex-basis',
    '内容对齐':'justify-content',
    '对齐项目':'align-items',
    '对齐内容':'align-content',
    '自身对齐':'align-self',
    '各格对齐':'justify-items',
    '放置项目':'place-items',
    '放置内容':'place-content',
    '顺序':'order',
    '间距':'gap',
    '行间距':'row-gap',
    '列间距':'column-gap',
    '网格':'grid',
    '网格列模板':'grid-template-columns',
    '网格行模板':'grid-template-rows',
    '网格列':'grid-column',
    '网格行':'grid-row',
    '网格区域':'grid-area',
    '宽度':'width',
    '高度':'height',
    '最小宽度':'min-width',
    '最大宽度':'max-width',
    '最小高度':'min-height',
    '最大高度':'max-height',
    '边距':'margin',
    '上边距':'margin-top',
    '右边距':'margin-right',
    '下边距':'margin-bottom',
    '左边距':'margin-left',
    '内边距':'padding',
    '上内边距':'padding-top',
    '右内边距':'padding-right',
    '下内边距':'padding-bottom',
    '左内边距':'padding-left',
    '盒子阴影':'box-shadow',
    '不透明度':'opacity',
    '边框':'border',
    '边框宽度':'border-width',
    '边框样式':'border-style',
    '边框颜色':'border-color',
    '边框圆角':'border-radius',
    '上边框':'border-top',
    '右边框':'border-right',
    '下边框':'border-bottom',
    '左边框':'border-left',
    '轮廓':'outline',
    '轮廓偏移':'outline-offset',
    '背景':'background',
    '背景颜色':'background-color',
    '背景图像':'background-image',
    '背景尺寸':'background-size',
    '背景位置':'background-position',
    '背景重复':'background-repeat',
    '颜色':'color',
    '字体':'font',
    '字体族':'font-family',
    '字体大小':'font-size',
    '字重':'font-weight',
    '字体样式':'font-style',
    '行高':'line-height',
    '文字对齐':'text-align',
    '文字装饰':'text-decoration',
    '文字溢出':'text-overflow',
    '字距':'letter-spacing',
    '词距':'word-spacing',
    '断词':'word-break',
    '空白':'white-space',
    '文字阴影':'text-shadow',
    '光标':'cursor',
    '指针事件':'pointer-events',
    '用户选择':'user-select',
    '调整大小':'resize',
    '过渡':'transition',
    '过渡属性':'transition-property',
    '过渡时长':'transition-duration',
    '过渡函数':'transition-timing-function',
    '过渡延迟':'transition-delay',
    '动画':'animation',
    '动画名':'animation-name',
    '变换':'transform',
    '变换原点':'transform-origin',
    '对象适应':'object-fit',
    '对象位置':'object-position',
    '宽高比':'aspect-ratio',
    '内容':'content',
    '滤镜':'filter',
    '背景滤镜':'backdrop-filter',
    '列表样式':'list-style',
    '垂直对齐':'vertical-align',
    '表格布局':'table-layout',
    '边框合并':'border-collapse',
    '空单元格':'empty-cells',
    '容器名':'container-name',
    '视图过渡名':'view-transition-name',
}
标准属性集=set(属性名.values())
允许自定义标识={
    'animation',
    'animation-name',
    'font',
    'font-family',
    'container-name',
    'view-transition-name',
    'grid-area',
    'grid-row',
    'grid-column',
    'list-style',
    'list-style-type',
}
全局取值={
    '无':'none',
    '自动':'auto',
    '继承':'inherit',
    '初始':'initial',
    '还原':'unset',
    '恢复':'revert',
    '本层':'revert-layer',
    '透明':'transparent',
    '当前颜色':'currentcolor',
    '居中':'center',
    '左':'left',
    '右':'right',
    '上':'top',
    '下':'bottom',
    '块':'block',
    '内联':'inline',
    '内联块':'inline-block',
    '弹性':'flex',
    '内联弹性':'inline-flex',
    '网格':'grid',
    '内联网格':'inline-grid',
    '内容':'contents',
    '表格':'table',
    '表格行':'table-row',
    '单元格':'table-cell',
    '固定':'fixed',
    '相对':'relative',
    '绝对':'absolute',
    '静态':'static',
    '粘性':'sticky',
    '隐藏':'hidden',
    '可见':'visible',
    '滚动':'scroll',
    '指针':'pointer',
    '默认':'default',
    '禁止':'not-allowed',
    '等待':'wait',
    '文字':'text',
    '帮助':'help',
    '移动':'move',
    '抓':'grab',
    '抓取':'grabbing',
    '粗体':'bold',
    '更粗':'bolder',
    '更细':'lighter',
    '常规':'normal',
    '正常':'normal',
    '斜体':'italic',
    '实线':'solid',
    '虚线':'dashed',
    '点线':'dotted',
    '双线':'double',
    '凹槽':'groove',
    '凸脊':'ridge',
    '内嵌':'inset',
    '外凸':'outset',
    '缓动':'ease',
    '缓入':'ease-in',
    '缓出':'ease-out',
    '缓入出':'ease-in-out',
    '线性':'linear',
    '开始':'start',
    '结束':'end',
    '环绕':'space-around',
    '均匀':'space-evenly',
    '拉伸':'stretch',
    '基线':'baseline',
    '中间':'middle',
    '覆盖':'cover',
    '包含':'contain',
    '填充':'fill',
    '缩小':'scale-down',
    '重复':'repeat',
    '不重复':'no-repeat',
    '横向重复':'repeat-x',
    '纵向重复':'repeat-y',
    '行':'row',
    '列':'column',
    '反向行':'row-reverse',
    '反向列':'column-reverse',
    '换行':'wrap',
    '不换行':'nowrap',
    '大写':'uppercase',
    '小写':'lowercase',
    '首字大写':'capitalize',
    '下划线':'underline',
    '删除线':'line-through',
    '保留':'pre',
    '保留换行':'pre-wrap',
    '保留行':'pre-line',
    '省略':'ellipsis',
    '裁切':'clip',
    '全部':'all',
    '边框盒':'border-box',
    '内容盒':'content-box',
    '适应内容':'fit-content',
    '最小内容':'min-content',
    '最大内容':'max-content',
    '到':'to',
    '红':'red',
    '绿':'green',
    '蓝':'blue',
    '白':'white',
    '黑':'black',
    '黄':'yellow',
    '橙':'orange',
    '紫':'purple',
    '灰':'gray',
    '棕':'brown',
    '青':'cyan',
    '粉':'pink',
    '金':'gold',
    '银':'silver',
}
分属性取值={
    'text-align':{'两端':'justify'},
    'justify-content':{'两端':'space-between'},
    'align-content':{'两端':'space-between'},
    'place-content':{'两端':'space-between'},
    'border-collapse':{'合并':'collapse','分开':'separate'},
    'empty-cells':{'显示':'show','隐藏':'hide'},
    'visibility':{'折叠':'collapse'},
    'resize':{'横向':'horizontal','纵向':'vertical','两者':'both'},
}
函数名={
    '平移':'translate',
    '水平平移':'translateX',
    '垂直平移':'translateY',
    '纵深平移':'translateZ',
    '三维平移':'translate3d',
    '缩放':'scale',
    '水平缩放':'scaleX',
    '垂直缩放':'scaleY',
    '三维缩放':'scale3d',
    '旋转':'rotate',
    '横向旋转':'rotateX',
    '纵向旋转':'rotateY',
    '斜切':'skew',
    '横向斜切':'skewX',
    '纵向斜切':'skewY',
    '矩阵':'matrix',
    '三维矩阵':'matrix3d',
    '计算':'calc',
    '变量':'var',
    '最小':'min',
    '最大':'max',
    '限制':'clamp',
    '线性渐变':'linear-gradient',
    '径向渐变':'radial-gradient',
    '地址':'url',
    '模糊':'blur',
    '亮度':'brightness',
    '对比':'contrast',
    '灰度':'grayscale',
    '色相旋转':'hue-rotate',
    '反色':'invert',
    '饱和':'saturate',
    '褐色':'sepia',
    '投影':'drop-shadow',
    '内嵌':'inset',
}
伪类={
    '悬停':'hover',
    '激活':'active',
    '焦点':'focus',
    '焦点可见':'focus-visible',
    '焦点内':'focus-within',
    '禁用':'disabled',
    '选中':'checked',
    '必填':'required',
    '可选':'optional',
    '只读':'read-only',
    '可写':'read-write',
    '首个':'first-child',
    '末个':'last-child',
    '首类':'first-of-type',
    '末类':'last-of-type',
    '序号':'nth-child',
    '倒数序号':'nth-last-child',
    '空':'empty',
    '目标':'target',
    '链接':'link',
    '已访问':'visited',
    '根':'root',
    '非':'not',
    '匹配':'is',
    '其中':'where',
    '占位':'placeholder',
    '占位显示':'placeholder-shown',
    '选区':'selection',
    '之前':'before',
    '之后':'after',
    '首行':'first-line',
    '首字':'first-letter',
    '标记':'marker',
    '无效':'invalid',
    '有效':'valid',
}
艾特名={
    '媒体':'media',
    '关键帧':'keyframes',
    '支持':'supports',
    '字体':'font-face',
    '导入':'import',
    '字符集':'charset',
    '页':'page',
    '层':'layer',
    '容器':'container',
    '范围':'scope',
    '命名空间':'namespace',
    '计数样式':'counter-style',
}
标准艾特=set(艾特名.values())
条件词={
    '屏幕':'screen',
    '打印':'print',
    '语音':'speech',
    '全部':'all',
    '仅':'only',
    '非':'not',
    '与':'and',
    '或':'or',
    '竖屏':'portrait',
    '横屏':'landscape',
}
空白字符=' \t\r\n\f'
十六进制字符='0123456789abcdefABCDEF'

class 样式表:
    '一张样式表。规则直接存在这里，中文和标准 css 都由这个对象改'
    def __init__(自身,文本: str=''):
        '文本是整张样式表，中文英文都可以'
        自身.各规则=[]
        自身.源=''
        自身.位置=0
        自身.种类=''
        自身.起点=0
        自身.终点=0
        自身.解码=''
        if 文本:
            自身.替换(文本)

    def 替换(自身,文本: str)->None:
        '整张表换成这段文本'
        自身.打开(文本)
        自身.各规则=自身.读规则列表(False)

    def 插入(自身,规则: str,下标: int|None=None)->int:
        '插入一条规则，返回它的下标。不传下标则加到末尾'
        if not isinstance(规则,str):
            raise TypeError('规则必须是字符串')
        旧源=自身.源
        旧位置=自身.位置
        自身.打开(规则)
        try:
            各条=自身.读规则列表(False)
        finally:
            自身.源=旧源
            自身.位置=旧位置
        if len(各条)!=1:
            raise 样式错误('一次插入一条规则')
        if 下标 is None:
            自身.各规则.append(各条[0])
            return len(自身.各规则)-1
        自身.检查下标(下标,len(自身.各规则),True)
        自身.各规则.insert(下标,各条[0])
        return 下标

    def 删除(自身,下标: int)->None:
        '按下标删掉一条规则'
        自身.检查下标(下标,len(自身.各规则),False)
        自身.各规则.pop(下标)

    def 取(自身,下标: int)->tuple:
        '按下标取一条规则。样式是(样式,选择器,声明)，条件是(条件,名字,前序,子规则)，单行是(单行,名字,前序)'
        自身.检查下标(下标,len(自身.各规则),False)
        return 自身.各规则[下标]

    def 设置(自身,下标: int,属性: str,值: str,优先级: str='')->None:
        '给这条样式规则写一条声明。属性、取值、优先级可以用中文。取值空字符串表示删掉'
        各声明=自身.取声明(下标)
        标准属性=自身.翻译属性(属性)
        if 值.strip()=='':
            自身.删掉声明(各声明,标准属性)
            return
        标准优先级=自身.翻译优先级(优先级)
        标准值,值优先级=自身.翻译值(标准属性,值)
        if 值优先级 and 标准优先级 and 值优先级!=标准优先级:
            raise 样式错误('优先级写了两次')
        if 值优先级:
            标准优先级=值优先级
        自身.写入声明(各声明,标准属性,标准值,标准优先级)

    def 读取(自身,下标: int,属性: str)->str:
        '读这条样式规则里的标准取值。没有这条时是空字符串'
        各声明=自身.取声明(下标)
        标准属性=自身.翻译属性(属性)
        for 项 in 各声明:
            if 项[0]==标准属性:
                return 项[1]
        return ''

    def 删声明(自身,下标: int,属性: str)->str:
        '删掉这条声明并返回原来的取值。没有时是空字符串'
        各声明=自身.取声明(下标)
        return 自身.删掉声明(各声明,自身.翻译属性(属性))

    def 有(自身,下标: int,属性: str)->bool:
        '这条样式规则里有没有这个属性'
        各声明=自身.取声明(下标)
        标准属性=自身.翻译属性(属性)
        for 项 in 各声明:
            if 项[0]==标准属性:
                return True
        return False

    def 优先级(自身,下标: int,属性: str)->str:
        '重要时是 important，没有这条或没标重要时是空字符串'
        各声明=自身.取声明(下标)
        标准属性=自身.翻译属性(属性)
        for 项 in 各声明:
            if 项[0]==标准属性:
                return 项[2]
        return ''

    def 转义标识(自身,标识: str)->str:
        '按 css 标识的序列化规则转义。空字符串得到空字符串'
        if not isinstance(标识,str):
            raise TypeError('标识必须是字符串')
        结果=[]
        for 序号,字 in enumerate(标识):
            码=ord(字)
            if 码==0:
                结果.append('\ufffd')
            elif 1<=码<=0x1F or 码==0x7F:
                结果.append('\\'+format(码,'x')+' ')
            elif 序号==0 and 0x30<=码<=0x39:
                结果.append('\\'+format(码,'x')+' ')
            elif 序号==1 and 标识[0]=='-' and 0x30<=码<=0x39:
                结果.append('\\'+format(码,'x')+' ')
            elif 序号==0 and 字=='-' and len(标识)==1:
                结果.append('\\-')
            elif 码>=0x80 or 字 in '-_' or (字.isascii() and 字.isalnum()):
                结果.append(字)
            else:
                结果.append('\\'+字)
        return ''.join(结果)

    @property
    def 条数(自身)->int:
        '规则条数'
        return len(自身.各规则)

    def 文本(自身)->str:
        '序列化成标准 css。规则之间换行'
        各行=[]
        for 规则 in 自身.各规则:
            各行.append(自身.规则文本(规则))
        return '\n'.join(各行)

    def 打开(自身,文本: str)->None:
        '换上正在读的文本，从头开始'
        if not isinstance(文本,str):
            raise TypeError('样式表文本必须是字符串')
        自身.源=文本
        自身.位置=0

    def 读完(自身)->bool:
        '当前位置是否已经到末尾'
        return 自身.位置>=len(自身.源)

    def 记下(自身,种类: str,起点: int,终点: int,解码: str)->None:
        '记下刚读到的片段，并把位置移到片段后面'
        自身.种类=种类
        自身.起点=起点
        自身.终点=终点
        自身.解码=解码
        自身.位置=终点

    def 含中文(自身,文本: str)->bool:
        '有没有中日韩统一表意文字'
        for 字 in 文本:
            码=ord(字)
            if 0x3400<=码<=0x9FFF or 0xF900<=码<=0xFAFF:
                return True
        return False

    def 是名称字符(自身,字: str)->bool:
        '标识里可以接着出现的字符'
        if 字 in '-_':
            return True
        if ord(字)>=0x80:
            return True
        return 字.isascii() and 字.isalnum()

    def 在标识开头(自身,位置: int)->bool:
        '这个位置是不是标识的开头'
        文本=自身.源
        if 位置>=len(文本):
            return False
        字=文本[位置]
        if 字=='-':
            if 位置+1>=len(文本):
                return False
            下一个=文本[位置+1]
            if 下一个=='-' or 下一个=='\\':
                return True
            return 自身.是名称字符(下一个) and not 下一个.isdigit()
        if 字=='\\':
            return True
        if ord(字)>=0x80 or 字=='_':
            return True
        return 字.isascii() and 字.isalpha()

    def 在数字开头(自身,位置: int)->bool:
        '这个位置是不是数'
        文本=自身.源
        if 位置>=len(文本):
            return False
        字=文本[位置]
        if 字 in '+-':
            if 位置+1<len(文本) and 文本[位置+1].isdigit():
                return True
            return 位置+2<len(文本) and 文本[位置+1]=='.' and 文本[位置+2].isdigit()
        if 字=='.':
            return 位置+1<len(文本) and 文本[位置+1].isdigit()
        return 字.isdigit()

    def 读转义(自身,位置: int)->tuple:
        '读掉一个反斜杠转义，返回字符和新位置'
        文本=自身.源
        位置+=1
        if 位置>=len(文本):
            raise 样式错误('反斜杠后面没有字符')
        字=文本[位置]
        if 字=='\n':
            return '',位置+1
        if 字 in 十六进制字符:
            数字=''
            while 位置<len(文本) and len(数字)<6 and 文本[位置] in 十六进制字符:
                数字+=文本[位置]
                位置+=1
            if 位置<len(文本) and 文本[位置] in 空白字符:
                位置+=1
            码=int(数字,16)
            if 码==0 or 码>0x10FFFF:
                return '\ufffd',位置
            return chr(码),位置
        return 字,位置+1

    def 读标识(自身,位置: int)->tuple:
        '从位置读一个标识，返回解码和新位置'
        文本=自身.源
        起点=位置
        解码=[]
        while 位置<len(文本):
            字=文本[位置]
            if 字=='\\':
                字符,位置=自身.读转义(位置)
                解码.append(字符)
                continue
            if 自身.是名称字符(字):
                解码.append(字)
                位置+=1
                continue
            break
        if 位置==起点:
            raise 样式错误('这里不是标识')
        return ''.join(解码),位置

    def 读数字(自身,位置: int)->int:
        '从位置读一个数，返回终点'
        文本=自身.源
        if 文本[位置] in '+-':
            位置+=1
        有数字=False
        while 位置<len(文本) and 文本[位置].isdigit():
            有数字=True
            位置+=1
        if 位置<len(文本) and 文本[位置]=='.':
            下一位=位置+1
            if 下一位<len(文本) and 文本[下一位].isdigit():
                位置=下一位
                while 位置<len(文本) and 文本[位置].isdigit():
                    有数字=True
                    位置+=1
        if not 有数字:
            raise 样式错误('这里不是数')
        if 位置<len(文本) and 文本[位置] in 'eE':
            指数=位置+1
            if 指数<len(文本) and 文本[指数] in '+-':
                指数+=1
            if 指数<len(文本) and 文本[指数].isdigit():
                位置=指数
                while 位置<len(文本) and 文本[位置].isdigit():
                    位置+=1
        return 位置

    def 读字符串(自身,位置: int)->int:
        '从位置读一个引号字符串，返回终点'
        文本=自身.源
        引号=文本[位置]
        位置+=1
        长度=len(文本)
        while 位置<长度:
            字=文本[位置]
            if 字=='\\':
                if 位置+1>=长度:
                    raise 样式错误('字符串没有结束')
                位置+=2
                continue
            if 字=='\n':
                raise 样式错误('字符串没有结束')
            if 字==引号:
                return 位置+1
            位置+=1
        raise 样式错误('字符串没有结束')

    def 读片段(自身)->None:
        '从当前位置读一个片段，并前进'
        文本=自身.源
        位置=自身.位置
        if 位置>=len(文本):
            raise 样式错误('已经读完了')
        字=文本[位置]
        if 字 in 空白字符:
            起点=位置
            位置+=1
            while 位置<len(文本) and 文本[位置] in 空白字符:
                位置+=1
            自身.记下('空白',起点,位置,'')
            return
        if 字=='/' and 位置+1<len(文本) and 文本[位置+1]=='*':
            结束=文本.find('*/',位置+2)
            if 结束<0:
                raise 样式错误('注释没有结束')
            自身.记下('注释',位置,结束+2,'')
            return
        if 字 in '"\'':
            终点=自身.读字符串(位置)
            自身.记下('字符串',位置,终点,文本[位置:终点])
            return
        if 自身.在数字开头(位置):
            终点=自身.读数字(位置)
            自身.记下('数字',位置,终点,文本[位置:终点])
            return
        if 自身.在标识开头(位置):
            解码,终点=自身.读标识(位置)
            自身.记下('标识',位置,终点,解码)
            return
        自身.记下('符号',位置,位置+1,字)

    def 读到闭括号(自身)->str:
        '当前位置在左括号后面。读到配对的右括号，返回内部文本'
        起点=自身.位置
        深度=1
        while not 自身.读完():
            自身.读片段()
            if 自身.种类=='符号' and 自身.解码=='(':
                深度+=1
            elif 自身.种类=='符号' and 自身.解码==')':
                深度-=1
                if 深度==0:
                    return 自身.源[起点:自身.起点]
        raise 样式错误('括号没有闭合')

    def 前一个有效(自身,片段: list)->str:
        '已经写出的文本里，最后一个非空白字符'
        for 一段 in reversed(片段):
            纯=一段.rstrip(空白字符)
            if 纯:
                return 纯[-1]
        return ''

    def 翻译属性(自身,名称: str)->str:
        '中文或英文属性名换成标准属性名。不认识的中文直接报错'
        名称=名称.strip()
        if not 名称:
            raise 样式错误('属性是空的')
        if 名称.startswith('--'):
            return 名称
        if 名称 in 属性名:
            return 属性名[名称]
        if 名称.isascii():
            return 名称.lower()
        if 自身.含中文(名称):
            raise 样式错误('不认识的属性：'+名称)
        raise 样式错误('不认识的属性：'+名称)

    def 翻译艾特(自身,名称: str)->str:
        '中文或英文 @ 名字换成标准名字，不带 @'
        if 名称 in 艾特名:
            return 艾特名[名称]
        if 名称.isascii():
            return 名称.lower()
        if 自身.含中文(名称):
            raise 样式错误('不认识的@规则：'+名称)
        raise 样式错误('不认识的@规则：'+名称)

    def 翻译优先级(自身,优先级: str)->str:
        '空字符串、important、重要。其它直接报错'
        if 优先级 is None or 优先级=='':
            return ''
        if 优先级.lower()=='important' or 优先级=='重要':
            return 'important'
        raise 样式错误('优先级只能是 important 或 重要')

    def 对应标识(自身,解码: str,原文: str,模式: str,属性: str,是函数: bool,前一字符: str)->str:
        '按所在位置把一个标识换成标准写法。对不上的中文直接报错'
        if 模式=='选择器':
            if 前一字符==':':
                if 解码 in 伪类:
                    return 伪类[解码]
                if 自身.含中文(解码):
                    raise 样式错误('不认识的伪类：'+解码)
                return 原文
            if 前一字符 not in '.#[ ' and 解码=='从':
                return 'from'
            if 前一字符 not in '.#[ ' and 解码=='到':
                return 'to'
            return 原文
        if 模式=='前序':
            if 前一字符==':':
                if 解码 in 伪类:
                    return 伪类[解码]
                if 自身.含中文(解码):
                    raise 样式错误('不认识的伪类：'+解码)
                return 原文
            if 前一字符 in '.#':
                return 原文
            if 是函数 and 解码 in 函数名:
                return 函数名[解码]
            if 解码 in 条件词:
                return 条件词[解码]
            if 解码 in 属性名:
                return 属性名[解码]
            if 解码 in 全局取值:
                return 全局取值[解码]
            return 原文
        if 解码.startswith('--'):
            return 原文
        if 是函数:
            if 解码 in 函数名:
                return 函数名[解码]
            if 自身.含中文(解码):
                raise 样式错误('不认识的函数：'+解码)
            return 原文
        if 属性 in 分属性取值 and 解码 in 分属性取值[属性]:
            return 分属性取值[属性][解码]
        if 解码 in 全局取值:
            return 全局取值[解码]
        if 解码 in 属性名:
            return 属性名[解码]
        是已知属性=属性 in 标准属性集
        允许名字=属性 in 允许自定义标识 or 属性.startswith('--')
        if 自身.含中文(解码) and 是已知属性 and not 允许名字:
            raise 样式错误('不认识的取值：'+解码)
        return 原文

    def 扫描替换(自身,原文: str,模式: str,属性: str='')->str:
        '丢掉注释，并把标识换成标准写法。字符串里的字保持原样'
        旧源=自身.源
        旧位置=自身.位置
        自身.源=原文
        自身.位置=0
        输出=[]
        try:
            while not 自身.读完():
                自身.读片段()
                if 自身.种类=='注释':
                    continue
                if 自身.种类=='标识':
                    紧跟函数=自身.终点<len(自身.源) and 自身.源[自身.终点]=='('
                    替换=自身.对应标识(自身.解码,自身.源[自身.起点:自身.终点],模式,属性,紧跟函数,自身.前一个有效(输出))
                    输出.append(替换)
                    if 紧跟函数 and 替换=='url':
                        自身.位置=自身.终点+1
                        内部=自身.读到闭括号()
                        输出.append('(')
                        输出.append(内部)
                        输出.append(')')
                    continue
                输出.append(自身.源[自身.起点:自身.终点])
        finally:
            自身.源=旧源
            自身.位置=旧位置
        return ''.join(输出)

    def 拆优先级(自身,值: str)->tuple:
        '取值末尾的 !important 或 !重要 拆出来。返回剩余文本和优先级'
        旧源=自身.源
        旧位置=自身.位置
        自身.源=值
        自身.位置=0
        try:
            while not 自身.读完():
                自身.读片段()
                if 自身.种类 in ('空白','注释'):
                    continue
                if 自身.种类=='符号' and 自身.解码=='!':
                    叹号起点=自身.起点
                    找到=False
                    种2=''
                    解2=''
                    终2=自身.位置
                    while not 自身.读完():
                        自身.读片段()
                        if 自身.种类 in ('空白','注释'):
                            continue
                        种2=自身.种类
                        解2=自身.解码
                        终2=自身.终点
                        找到=True
                        break
                    if not 找到:
                        raise 样式错误('优先级没有写完')
                    if 种2=='标识' and (解2.lower()=='important' or 解2=='重要'):
                        while not 自身.读完():
                            自身.读片段()
                            if 自身.种类 not in ('空白','注释'):
                                raise 样式错误('优先级不在取值末尾')
                        return 值[:叹号起点].rstrip(),'important'
        finally:
            自身.源=旧源
            自身.位置=旧位置
        return 值,''

    def 翻译值(自身,属性: str,值: str)->tuple:
        '把一条取值换成标准 css，并拆出优先级'
        剩余,优先级=自身.拆优先级(值)
        标准=自身.扫描替换(剩余,'取值',属性).strip()
        if 标准=='' and not 属性.startswith('--'):
            raise 样式错误('取值是空的')
        return 标准,优先级

    def 翻译选择器(自身,原文: str)->str:
        '伪类和关键帧的从、到换成标准写法。类名保持原样'
        标准=自身.扫描替换(原文,'选择器').strip()
        if not 标准:
            raise 样式错误('选择器是空的')
        return 标准

    def 翻译前序(自身,原文: str)->str:
        '@ 规则头里认识的词换成标准写法，起的名字保持原样'
        return 自身.扫描替换(原文,'前序').strip()

    def 写入声明(自身,各声明: list,属性: str,值: str,优先级: str)->None:
        '同名属性原地换掉，新属性加到末尾'
        for 序号,项 in enumerate(各声明):
            if 项[0]==属性:
                各声明[序号]=(属性,值,优先级)
                return
        各声明.append((属性,值,优先级))

    def 删掉声明(自身,各声明: list,属性: str)->str:
        '删掉同名属性，返回它的取值'
        for 序号,项 in enumerate(各声明):
            if 项[0]==属性:
                各声明.pop(序号)
                return 项[1]
        return ''

    def 清属性名(自身,原文: str)->str:
        '去掉属性名里的空白和注释'
        旧源=自身.源
        旧位置=自身.位置
        自身.源=原文
        自身.位置=0
        输出=[]
        try:
            while not 自身.读完():
                自身.读片段()
                if 自身.种类 not in ('空白','注释'):
                    输出.append(自身.源[自身.起点:自身.终点])
        finally:
            自身.源=旧源
            自身.位置=旧位置
        名称=''.join(输出)
        if not 名称:
            raise 样式错误('属性是空的')
        return 名称

    def 读声明(自身,停在右括号: bool)->list:
        '从当前位置读声明。停在右括号时吃掉右括号'
        各声明=[]
        while not 自身.读完():
            记=自身.位置
            自身.读片段()
            if 自身.种类 in ('空白','注释'):
                continue
            if 自身.种类=='符号' and 自身.解码==';':
                continue
            if 自身.种类=='符号' and 自身.解码=='}':
                if 停在右括号:
                    return 各声明
                raise 样式错误('声明里多了右括号')
            自身.位置=记
            属性起点=记
            圆括号=0
            方括号=0
            找到冒号=False
            while not 自身.读完():
                自身.读片段()
                if 自身.种类=='符号' and 自身.解码==':' and 圆括号==0 and 方括号==0:
                    找到冒号=True
                    break
                if 自身.种类=='符号' and 自身.解码==';' and 圆括号==0 and 方括号==0:
                    raise 样式错误('属性缺少冒号')
                if 自身.种类=='符号' and 自身.解码=='(':
                    圆括号+=1
                elif 自身.种类=='符号' and 自身.解码==')':
                    圆括号-=1
                elif 自身.种类=='符号' and 自身.解码=='[':
                    方括号+=1
                elif 自身.种类=='符号' and 自身.解码==']':
                    方括号-=1
            if not 找到冒号:
                raise 样式错误('属性缺少冒号')
            属性原文=自身.源[属性起点:自身.起点]
            值起点=自身.位置
            圆括号=0
            方括号=0
            值终点=len(自身.源)
            结束符=''
            while not 自身.读完():
                自身.读片段()
                if 自身.种类=='符号' and 自身.解码=='}' and (圆括号!=0 or 方括号!=0):
                    raise 样式错误('括号没有闭合')
                if 自身.种类=='符号' and 自身.解码 in ';}' and 圆括号==0 and 方括号==0:
                    值终点=自身.起点
                    结束符=自身.解码
                    break
                if 自身.种类=='符号' and 自身.解码=='(':
                    圆括号+=1
                elif 自身.种类=='符号' and 自身.解码==')':
                    if 圆括号==0:
                        raise 样式错误('括号没有闭合')
                    圆括号-=1
                elif 自身.种类=='符号' and 自身.解码=='[':
                    方括号+=1
                elif 自身.种类=='符号' and 自身.解码==']':
                    if 方括号==0:
                        raise 样式错误('括号没有闭合')
                    方括号-=1
            if 圆括号!=0 or 方括号!=0:
                raise 样式错误('括号没有闭合')
            标准属性=自身.翻译属性(自身.清属性名(属性原文))
            标准值,优先级=自身.翻译值(标准属性,自身.源[值起点:值终点])
            自身.写入声明(各声明,标准属性,标准值,优先级)
            if 结束符=='}':
                if 停在右括号:
                    return 各声明
                raise 样式错误('声明里多了右括号')
        if 停在右括号:
            raise 样式错误('缺少右括号')
        return 各声明

    def 读样式规则(自身)->tuple:
        '从当前位置读一条选择器加声明块的规则'
        起点=自身.位置
        圆括号=0
        方括号=0
        while not 自身.读完():
            片段起点=自身.位置
            自身.读片段()
            if 自身.种类=='符号' and 自身.解码=='{' and 圆括号==0 and 方括号==0:
                选择器=自身.翻译选择器(自身.源[起点:片段起点])
                各声明=自身.读声明(True)
                return ('样式',选择器,各声明)
            if 自身.种类=='符号' and 自身.解码==';' and 圆括号==0 and 方括号==0:
                raise 样式错误('规则缺少声明块')
            if 自身.种类=='符号' and 自身.解码=='(':
                圆括号+=1
            elif 自身.种类=='符号' and 自身.解码==')':
                圆括号-=1
            elif 自身.种类=='符号' and 自身.解码=='[':
                方括号+=1
            elif 自身.种类=='符号' and 自身.解码==']':
                方括号-=1
        raise 样式错误('规则没有写完')

    def 读艾特(自身)->tuple:
        '从当前位置读一条 @ 规则，位置必须在 @ 上'
        if 自身.读完() or 自身.源[自身.位置]!='@':
            raise 样式错误('这里不是@规则')
        if 自身.位置+1>=len(自身.源) or not 自身.在标识开头(自身.位置+1):
            raise 样式错误('@后面不是名字')
        自身.位置+=1
        自身.读片段()
        if 自身.种类!='标识':
            raise 样式错误('@后面不是名字')
        标准名=自身.翻译艾特(自身.解码)
        前序起点=自身.位置
        圆括号=0
        方括号=0
        while not 自身.读完():
            片段起点=自身.位置
            自身.读片段()
            if 自身.种类=='符号' and 自身.解码 in ';{' and 圆括号==0 and 方括号==0:
                前序=自身.翻译前序(自身.源[前序起点:片段起点])
                if 自身.解码==';':
                    return ('单行',标准名,前序)
                子规则=自身.读规则列表(True)
                return ('条件',标准名,前序,子规则)
            if 自身.种类=='符号' and 自身.解码=='(':
                圆括号+=1
            elif 自身.种类=='符号' and 自身.解码==')':
                圆括号-=1
            elif 自身.种类=='符号' and 自身.解码=='[':
                方括号+=1
            elif 自身.种类=='符号' and 自身.解码==']':
                方括号-=1
        raise 样式错误('规则没有写完')

    def 读规则列表(自身,停在右括号: bool)->list:
        '从当前位置读若干条规则。停在右括号时吃掉右括号'
        各规则=[]
        while not 自身.读完():
            记=自身.位置
            自身.读片段()
            if 自身.种类 in ('空白','注释'):
                continue
            if 自身.种类=='符号' and 自身.解码=='}':
                if 停在右括号:
                    return 各规则
                raise 样式错误('多出来的右括号')
            if 自身.种类=='符号' and 自身.解码=='@':
                自身.位置=记
                各规则.append(自身.读艾特())
                continue
            自身.位置=记
            各规则.append(自身.读样式规则())
        if 停在右括号:
            raise 样式错误('缺少右括号')
        return 各规则

    def 取声明(自身,下标: int)->list:
        '取出这条样式规则的声明列表'
        自身.检查下标(下标,len(自身.各规则),False)
        规则=自身.各规则[下标]
        if 规则[0]!='样式':
            raise 样式错误('这条不是样式规则')
        return 规则[2]

    def 检查下标(自身,下标: int,上限: int,允许末尾: bool)->None:
        '下标必须是整数，并且落在范围内'
        if isinstance(下标,bool) or not isinstance(下标,int):
            raise 样式错误('下标必须是整数')
        if 下标<0 or 下标>上限 or (下标==上限 and not 允许末尾):
            raise 样式错误('下标超出范围')

    def 声明文本(自身,各声明: list)->str:
        '把声明列表序列化成标准文本'
        各段=[]
        for 名称,值,优先级 in 各声明:
            一段=名称+': '+值
            if 优先级:
                一段+=' !important'
            各段.append(一段+';')
        return ' '.join(各段)

    def 规则文本(自身,规则: tuple)->str:
        '把一条规则序列化成标准 css'
        if 规则[0]=='样式':
            声明=自身.声明文本(规则[2])
            if 声明:
                return 规则[1]+' { '+声明+' }'
            return 规则[1]+' { }'
        if 规则[0]=='单行':
            if 规则[2]:
                return '@'+规则[1]+' '+规则[2]+';'
            return '@'+规则[1]+';'
        内部=[]
        for 子规则 in 规则[3]:
            内部.append(自身.规则文本(子规则))
        内部文本=' '.join(内部)
        if 规则[2]:
            头='@'+规则[1]+' '+规则[2]
        else:
            头='@'+规则[1]
        if 内部文本:
            return 头+' { '+内部文本+' }'
        return 头+' { }'
