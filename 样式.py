
class 样式:
    def __init__(自身,初始样式:dict):
        自身.样式=翻译css(dict(初始样式))

    def __getitem__(自身,属性:str)->str:
        return 自身.样式[样式名称映射.get(属性,属性)]

    def __setitem__(自身,属性:str,值:str)->None:
        自身.样式[样式名称映射.get(属性,属性)]=值

    def __delitem__(自身,属性:str)->None:
        del 自身.样式[样式名称映射.get(属性,属性)]

    def __format__(自身,format_spec:str,/)->str:
        return ';'.join(f'{k}:{v}' for k,v in 自身.样式.items())

    def __str__(自身)->str:
        return ';'.join(f'{k}:{v}' for k,v in 自身.样式.items())
         
class 样式选择器:
    ...

def 翻译css(css:dict)->dict:
    return {
        样式名称映射.get(k,k):v
        for k,v in css.items()
    }

样式名称映射={
    #盒模型与尺寸
    '宽度':'width',
    '高度':'height',
    '最小宽度':'min-width',
    '最小高度':'min-height',
    '最大宽度':'max-width',
    '最大高度':'max-height',
    '行向尺寸':'inline-size',
    '块向尺寸':'block-size',
    '最小行向尺寸':'min-inline-size',
    '最小块向尺寸':'min-block-size',
    '最大行向尺寸':'max-inline-size',
    '最大块向尺寸':'max-block-size',
    '盒模型':'box-sizing',
    '宽高比':'aspect-ratio',
    '尺寸插值':'interpolate-size',
    '包含':'contain',
    '包含固有尺寸':'contain-intrinsic-size',
    '包含固有宽度':'contain-intrinsic-width',
    '包含固有高度':'contain-intrinsic-height',
    '包含固有行向尺寸':'contain-intrinsic-inline-size',
    '包含固有块向尺寸':'contain-intrinsic-block-size',
    #外边距、内边距、定位边
    '外边距':'margin',
    '上外边距':'margin-top',
    '右外边距':'margin-right',
    '下外边距':'margin-bottom',
    '左外边距':'margin-left',
    '块向外边距':'margin-block',
    '块起始外边距':'margin-block-start',
    '块结束外边距':'margin-block-end',
    '行向外边距':'margin-inline',
    '行起始外边距':'margin-inline-start',
    '行结束外边距':'margin-inline-end',
    '外边距修剪':'margin-trim',
    '外边距断裂':'margin-break',
    '内边距':'padding',
    '上内边距':'padding-top',
    '右内边距':'padding-right',
    '下内边距':'padding-bottom',
    '左内边距':'padding-left',
    '块向内边距':'padding-block',
    '块起始内边距':'padding-block-start',
    '块结束内边距':'padding-block-end',
    '行向内边距':'padding-inline',
    '行起始内边距':'padding-inline-start',
    '行结束内边距':'padding-inline-end',
    '上':'top',
    '右':'right',
    '下':'bottom',
    '左':'left',
    '内嵌':'inset',
    '块向内嵌':'inset-block',
    '块起始内嵌':'inset-block-start',
    '块结束内嵌':'inset-block-end',
    '行向内嵌':'inset-inline',
    '行起始内嵌':'inset-inline-start',
    '行结束内嵌':'inset-inline-end',
    #边框、圆角、角形状
    '边框':'border',
    '边框宽度':'border-width',
    '边框样式':'border-style',
    '边框颜色':'border-color',
    '上边框':'border-top',
    '上边框宽度':'border-top-width',
    '上边框样式':'border-top-style',
    '上边框颜色':'border-top-color',
    '右边框':'border-right',
    '右边框宽度':'border-right-width',
    '右边框样式':'border-right-style',
    '右边框颜色':'border-right-color',
    '下边框':'border-bottom',
    '下边框宽度':'border-bottom-width',
    '下边框样式':'border-bottom-style',
    '下边框颜色':'border-bottom-color',
    '左边框':'border-left',
    '左边框宽度':'border-left-width',
    '左边框样式':'border-left-style',
    '左边框颜色':'border-left-color',
    '块向边框':'border-block',
    '块向边框宽度':'border-block-width',
    '块向边框样式':'border-block-style',
    '块向边框颜色':'border-block-color',
    '块起始边框':'border-block-start',
    '块起始边框宽度':'border-block-start-width',
    '块起始边框样式':'border-block-start-style',
    '块起始边框颜色':'border-block-start-color',
    '块结束边框':'border-block-end',
    '块结束边框宽度':'border-block-end-width',
    '块结束边框样式':'border-block-end-style',
    '块结束边框颜色':'border-block-end-color',
    '行向边框':'border-inline',
    '行向边框宽度':'border-inline-width',
    '行向边框样式':'border-inline-style',
    '行向边框颜色':'border-inline-color',
    '行起始边框':'border-inline-start',
    '行起始边框宽度':'border-inline-start-width',
    '行起始边框样式':'border-inline-start-style',
    '行起始边框颜色':'border-inline-start-color',
    '行结束边框':'border-inline-end',
    '行结束边框宽度':'border-inline-end-width',
    '行结束边框样式':'border-inline-end-style',
    '行结束边框颜色':'border-inline-end-color',
    '边框圆角':'border-radius',
    '左上圆角':'border-top-left-radius',
    '右上圆角':'border-top-right-radius',
    '右下圆角':'border-bottom-right-radius',
    '左下圆角':'border-bottom-left-radius',
    '起始起始圆角':'border-start-start-radius',
    '起始结束圆角':'border-start-end-radius',
    '结束起始圆角':'border-end-start-radius',
    '结束结束圆角':'border-end-end-radius',
    '边框图像':'border-image',
    '边框图像来源':'border-image-source',
    '边框图像切片':'border-image-slice',
    '边框图像宽度':'border-image-width',
    '边框图像外延':'border-image-outset',
    '边框图像重复':'border-image-repeat',
    '边框合并':'border-collapse',
    '边框间距':'border-spacing',
    '角形状':'corner-shape',
    '左上角形状':'corner-top-left-shape',
    '右上角形状':'corner-top-right-shape',
    '右下角形状':'corner-bottom-right-shape',
    '左下角形状':'corner-bottom-left-shape',
    '起始起始角形状':'corner-start-start-shape',
    '起始结束角形状':'corner-start-end-shape',
    '结束起始角形状':'corner-end-start-shape',
    '结束结束角形状':'corner-end-end-shape',
    #轮廓
    '轮廓':'outline',
    '轮廓颜色':'outline-color',
    '轮廓样式':'outline-style',
    '轮廓宽度':'outline-width',
    '轮廓偏移':'outline-offset',
    #背景
    '背景':'background',
    '背景颜色':'background-color',
    '背景图像':'background-image',
    '背景重复':'background-repeat',
    '背景附着':'background-attachment',
    '背景位置':'background-position',
    '背景水平位置':'background-position-x',
    '背景垂直位置':'background-position-y',
    '背景裁剪':'background-clip',
    '背景原点':'background-origin',
    '背景尺寸':'background-size',
    '背景混合模式':'background-blend-mode',
    #显示、定位、溢出
    '显示':'display',
    '定位':'position',
    '浮动':'float',
    '清除':'clear',
    '层叠顺序':'z-index',
    '可见性':'visibility',
    '内容可见性':'content-visibility',
    '不透明度':'opacity',
    '溢出':'overflow',
    '水平溢出':'overflow-x',
    '垂直溢出':'overflow-y',
    '块向溢出':'overflow-block',
    '行向溢出':'overflow-inline',
    '溢出裁剪边距':'overflow-clip-margin',
    '溢出锚点':'overflow-anchor',
    '文本溢出':'text-overflow',
    '叠加':'overlay',
    '缩放比例':'zoom',
    '隔离':'isolation',
    '混合模式':'mix-blend-mode',
    #弹性、网格、对齐、多列
    '弹性':'flex',
    '弹性增长':'flex-grow',
    '弹性收缩':'flex-shrink',
    '弹性基准':'flex-basis',
    '弹性方向':'flex-direction',
    '弹性换行':'flex-wrap',
    '弹性流':'flex-flow',
    '顺序':'order',
    '网格':'grid',
    '网格模板':'grid-template',
    '网格列模板':'grid-template-columns',
    '网格行模板':'grid-template-rows',
    '网格区域模板':'grid-template-areas',
    '网格自动列':'grid-auto-columns',
    '网格自动行':'grid-auto-rows',
    '网格自动流向':'grid-auto-flow',
    '网格列':'grid-column',
    '网格列起始':'grid-column-start',
    '网格列结束':'grid-column-end',
    '网格行':'grid-row',
    '网格行起始':'grid-row-start',
    '网格行结束':'grid-row-end',
    '网格区域':'grid-area',
    '网格间距':'grid-gap',
    '网格列间距':'grid-column-gap',
    '网格行间距':'grid-row-gap',
    '间距':'gap',
    '行间距':'row-gap',
    '列间距':'column-gap',
    '主轴对齐':'justify-content',
    '项目主轴对齐':'justify-items',
    '自身主轴对齐':'justify-self',
    '交叉轴对齐':'align-items',
    '自身交叉轴对齐':'align-self',
    '交叉轴内容对齐':'align-content',
    '内容简写对齐':'place-content',
    '项目简写对齐':'place-items',
    '自身简写对齐':'place-self',
    '多列':'columns',
    '列数':'column-count',
    '列宽':'column-width',
    '列填充':'column-fill',
    '列跨越':'column-span',
    '列分隔线':'column-rule',
    '列分隔线颜色':'column-rule-color',
    '列分隔线样式':'column-rule-style',
    '列分隔线宽度':'column-rule-width',
    #字体与文本
    '字体':'font',
    '字体族':'font-family',
    '字号':'font-size',
    '字体样式':'font-style',
    '字体变体':'font-variant',
    '字重':'font-weight',
    '字体拉伸':'font-stretch',
    '字号调整':'font-size-adjust',
    '字距微调':'font-kerning',
    '字体特性设置':'font-feature-settings',
    '字体可变设置':'font-variation-settings',
    '字体光学尺寸':'font-optical-sizing',
    '字体调色板':'font-palette',
    '字体合成':'font-synthesis',
    '字重合成':'font-synthesis-weight',
    '字体样式合成':'font-synthesis-style',
    '小型大写合成':'font-synthesis-small-caps',
    '上下标合成':'font-synthesis-position',
    '连字变体':'font-variant-ligatures',
    '大写变体':'font-variant-caps',
    '数字变体':'font-variant-numeric',
    '替代字形':'font-variant-alternates',
    '东亚字形':'font-variant-east-asian',
    '上下标变体':'font-variant-position',
    '表情符号变体':'font-variant-emoji',
    '字体语言覆盖':'font-language-override',
    '行高':'line-height',
    '字间距':'letter-spacing',
    '词间距':'word-spacing',
    '文本对齐':'text-align',
    '末行对齐':'text-align-last',
    '文本齐行':'text-justify',
    '文本缩进':'text-indent',
    '文本转换':'text-transform',
    '文本装饰':'text-decoration',
    '文本装饰线':'text-decoration-line',
    '文本装饰颜色':'text-decoration-color',
    '文本装饰样式':'text-decoration-style',
    '文本装饰粗细':'text-decoration-thickness',
    '文本装饰跳过':'text-decoration-skip',
    '文本装饰避墨':'text-decoration-skip-ink',
    '下划线偏移':'text-underline-offset',
    '下划线位置':'text-underline-position',
    '文本强调':'text-emphasis',
    '文本强调颜色':'text-emphasis-color',
    '文本强调样式':'text-emphasis-style',
    '文本强调位置':'text-emphasis-position',
    '文本阴影':'text-shadow',
    '文本换行':'text-wrap',
    '文本换行模式':'text-wrap-mode',
    '文本换行样式':'text-wrap-style',
    '空白':'white-space',
    '空白折叠':'white-space-collapse',
    '断词':'word-break',
    '行断':'line-break',
    '溢出换行':'overflow-wrap',
    '单词换行':'word-wrap',
    '连字符':'hyphens',
    '连字符字符':'hyphenate-character',
    '连字符长度限制':'hyphenate-limit-chars',
    '连字符行数限制':'hyphenate-limit-lines',
    '连字符末行限制':'hyphenate-limit-last',
    '制表符尺寸':'tab-size',
    '垂直对齐':'vertical-align',
    '文本渲染':'text-rendering',
    '文本尺寸调整':'text-size-adjust',
    '文本自动间距':'text-autospace',
    '文本间距修剪':'text-spacing-trim',
    '文本盒':'text-box',
    '文本盒修剪':'text-box-trim',
    '文本盒边缘':'text-box-edge',
    '悬挂标点':'hanging-punctuation',
    '首字母':'initial-letter',
    '行数限制':'line-clamp',
    '方向':'direction',
    'Unicode双向':'unicode-bidi',
    '书写模式':'writing-mode',
    '文本方向':'text-orientation',
    '文本直立合并':'text-combine-upright',
    #列表、计数、生成内容、表格、分页
    '列表样式':'list-style',
    '列表标记类型':'list-style-type',
    '列表标记位置':'list-style-position',
    '列表图像':'list-style-image',
    '计数器递增':'counter-increment',
    '计数器重置':'counter-reset',
    '计数器设置':'counter-set',
    '内容':'content',
    '引号':'quotes',
    '表格布局':'table-layout',
    '标题侧':'caption-side',
    '空单元格':'empty-cells',
    '断前':'break-before',
    '断后':'break-after',
    '断内':'break-inside',
    '分页前':'page-break-before',
    '分页后':'page-break-after',
    '分页内':'page-break-inside',
    '孤行':'orphans',
    '寡行':'widows',
    '盒装饰断裂':'box-decoration-break',
    '页面':'page',
    #变换、滤镜、遮罩、形状
    '盒阴影':'box-shadow',
    '滤镜':'filter',
    '背景滤镜':'backdrop-filter',
    '裁剪':'clip',
    '裁剪路径':'clip-path',
    '遮罩':'mask',
    '遮罩图像':'mask-image',
    '遮罩模式':'mask-mode',
    '遮罩重复':'mask-repeat',
    '遮罩位置':'mask-position',
    '遮罩裁剪':'mask-clip',
    '遮罩原点':'mask-origin',
    '遮罩尺寸':'mask-size',
    '遮罩合成':'mask-composite',
    '遮罩类型':'mask-type',
    '遮罩边框':'mask-border',
    '遮罩边框来源':'mask-border-source',
    '遮罩边框切片':'mask-border-slice',
    '遮罩边框宽度':'mask-border-width',
    '遮罩边框外延':'mask-border-outset',
    '遮罩边框重复':'mask-border-repeat',
    '遮罩边框模式':'mask-border-mode',
    '变换':'transform',
    '变换原点':'transform-origin',
    '变换样式':'transform-style',
    '变换盒':'transform-box',
    '透视':'perspective',
    '透视原点':'perspective-origin',
    '背面可见性':'backface-visibility',
    '平移':'translate',
    '旋转':'rotate',
    '缩放':'scale',
    '路径偏移':'offset',
    '偏移路径':'offset-path',
    '偏移距离':'offset-distance',
    '偏移旋转':'offset-rotate',
    '偏移锚点':'offset-anchor',
    '偏移位置':'offset-position',
    '将改变':'will-change',
    '对象适应':'object-fit',
    '对象位置':'object-position',
    '对象视图框':'object-view-box',
    '形状外绕':'shape-outside',
    '形状外边距':'shape-margin',
    '形状图像阈值':'shape-image-threshold',
    '图像渲染':'image-rendering',
    '图像方向':'image-orientation',
    '图像分辨率':'image-resolution',
    #过渡与动画
    '过渡':'transition',
    '过渡属性':'transition-property',
    '过渡时长':'transition-duration',
    '过渡时间函数':'transition-timing-function',
    '过渡延迟':'transition-delay',
    '过渡行为':'transition-behavior',
    '动画':'animation',
    '动画名称':'animation-name',
    '动画时长':'animation-duration',
    '动画时间函数':'animation-timing-function',
    '动画延迟':'animation-delay',
    '动画迭代次数':'animation-iteration-count',
    '动画方向':'animation-direction',
    '动画填充模式':'animation-fill-mode',
    '动画播放状态':'animation-play-state',
    '动画合成':'animation-composition',
    '动画时间线':'animation-timeline',
    '动画范围':'animation-range',
    '动画范围起始':'animation-range-start',
    '动画范围结束':'animation-range-end',
    '滚动时间线':'scroll-timeline',
    '滚动时间线名称':'scroll-timeline-name',
    '滚动时间线轴':'scroll-timeline-axis',
    '视图时间线':'view-timeline',
    '视图时间线名称':'view-timeline-name',
    '视图时间线轴':'view-timeline-axis',
    '视图时间线内嵌':'view-timeline-inset',
    '时间线作用域':'timeline-scope',
    #滚动
    '滚动行为':'scroll-behavior',
    '滚动外边距':'scroll-margin',
    '上滚动外边距':'scroll-margin-top',
    '右滚动外边距':'scroll-margin-right',
    '下滚动外边距':'scroll-margin-bottom',
    '左滚动外边距':'scroll-margin-left',
    '块向滚动外边距':'scroll-margin-block',
    '块起始滚动外边距':'scroll-margin-block-start',
    '块结束滚动外边距':'scroll-margin-block-end',
    '行向滚动外边距':'scroll-margin-inline',
    '行起始滚动外边距':'scroll-margin-inline-start',
    '行结束滚动外边距':'scroll-margin-inline-end',
    '滚动内边距':'scroll-padding',
    '上滚动内边距':'scroll-padding-top',
    '右滚动内边距':'scroll-padding-right',
    '下滚动内边距':'scroll-padding-bottom',
    '左滚动内边距':'scroll-padding-left',
    '块向滚动内边距':'scroll-padding-block',
    '块起始滚动内边距':'scroll-padding-block-start',
    '块结束滚动内边距':'scroll-padding-block-end',
    '行向滚动内边距':'scroll-padding-inline',
    '行起始滚动内边距':'scroll-padding-inline-start',
    '行结束滚动内边距':'scroll-padding-inline-end',
    '滚动吸附类型':'scroll-snap-type',
    '滚动吸附对齐':'scroll-snap-align',
    '滚动吸附停止':'scroll-snap-stop',
    '过度滚动行为':'overscroll-behavior',
    '水平过度滚动':'overscroll-behavior-x',
    '垂直过度滚动':'overscroll-behavior-y',
    '块向过度滚动':'overscroll-behavior-block',
    '行向过度滚动':'overscroll-behavior-inline',
    '滚动条宽度':'scrollbar-width',
    '滚动条颜色':'scrollbar-color',
    '滚动条槽':'scrollbar-gutter',
    #交互与界面
    '光标':'cursor',
    '光标颜色':'caret-color',
    '光标形状':'caret-shape',
    '指针事件':'pointer-events',
    '用户选择':'user-select',
    '触摸动作':'touch-action',
    '调整大小':'resize',
    '外观':'appearance',
    '强调色':'accent-color',
    '字段尺寸':'field-sizing',
    '输入安全':'input-security',
    '交互性':'interactivity',
    '颜色':'color',
    '配色方案':'color-scheme',
    '强制颜色调整':'forced-color-adjust',
    '打印颜色调整':'print-color-adjust',
    '颜色调整':'color-adjust',
    '动态范围限制':'dynamic-range-limit',
    '全部':'all',
    #排版进阶、注音、数学、锚点、容器、视图过渡
    '对齐基线':'alignment-baseline',
    '主基线':'dominant-baseline',
    '基线偏移':'baseline-shift',
    '基线来源':'baseline-source',
    '注音位置':'ruby-position',
    '注音对齐':'ruby-align',
    '注音合并':'ruby-merge',
    '注音外伸':'ruby-overhang',
    '数学样式':'math-style',
    '数学深度':'math-depth',
    '数学移位':'math-shift',
    '容器':'container',
    '容器类型':'container-type',
    '容器名称':'container-name',
    '锚点名称':'anchor-name',
    '锚点作用域':'anchor-scope',
    '定位锚点':'position-anchor',
    '定位区域':'position-area',
    '定位尝试':'position-try',
    '定位尝试回退':'position-try-fallbacks',
    '定位尝试顺序':'position-try-order',
    '定位可见性':'position-visibility',
    '视图过渡名称':'view-transition-name',
    '视图过渡类':'view-transition-class',
    '阅读流':'reading-flow',
    '阅读顺序':'reading-order',
    #SVG
    '填充':'fill',
    '填充不透明度':'fill-opacity',
    '填充规则':'fill-rule',
    '描边':'stroke',
    '描边宽度':'stroke-width',
    '描边线帽':'stroke-linecap',
    '描边连接':'stroke-linejoin',
    '描边斜接限制':'stroke-miterlimit',
    '描边虚线':'stroke-dasharray',
    '描边虚线偏移':'stroke-dashoffset',
    '描边不透明度':'stroke-opacity',
    '标记':'marker',
    '起始标记':'marker-start',
    '中间标记':'marker-mid',
    '结束标记':'marker-end',
    '颜色插值':'color-interpolation',
    '滤镜颜色插值':'color-interpolation-filters',
    '颜色渲染':'color-rendering',
    '形状渲染':'shape-rendering',
    '洪泛颜色':'flood-color',
    '洪泛不透明度':'flood-opacity',
    '光照颜色':'lighting-color',
    '停止颜色':'stop-color',
    '停止不透明度':'stop-opacity',
    '裁剪规则':'clip-rule',
    '矢量效果':'vector-effect',
    '绘制顺序':'paint-order',
    '文本锚点':'text-anchor',
    '路径数据':'d',
    '圆心横坐标':'cx',
    '圆心纵坐标':'cy',
    '半径':'r',
    '水平半径':'rx',
    '垂直半径':'ry',
    '横坐标':'x',
    '纵坐标':'y',
    #语音
    '语音族':'voice-family',
    '语速':'voice-rate',
    '音高':'voice-pitch',
    '音域':'voice-range',
    '语音重音':'voice-stress',
    '音量':'voice-volume',
    '语音平衡':'voice-balance',
    '语音时长':'voice-duration',
    '朗读':'speak',
    '朗读方式':'speak-as',
    '暂停':'pause',
    '前暂停':'pause-before',
    '后暂停':'pause-after',
    '停顿':'rest',
    '前停顿':'rest-before',
    '后停顿':'rest-after',
    '提示音':'cue',
    '前提示音':'cue-before',
    '后提示音':'cue-after',
}

from .js import JavaScript对象


class classList(JavaScript对象):
    '元素的 class 列表'
    length: int=...
    value: str=...
    def add(自身,*tokens: str)->None:
        '加上 class'
        ...

    def remove(自身,*tokens: str)->None:
        '去掉 class'
        ...

    def toggle(自身,token: str,force: bool|None=None)->bool:
        '有就去掉、没有就加上。force 为 True 只加，False 只去。返回是否还在'
        ...

    def contains(自身,token: str)->bool:
        '是否包含这个 class'
        ...

    def replace(自身,oldToken: str,newToken: str)->bool:
        '替换 class，原来没有则返回 False'
        ...

    def item(自身,index: int)->str|None:
        '按下标取 class，越界是 None'
        ...

    def supports(自身,token: str)->bool:
        '这个记号是否受支持。class 列表没有支持表，调用会抛 TypeError'
        ...

    def toString(自身)->str:
        '用空格拼起来'
        ...

    def entries(自身)->object:
        '下标和 class 的迭代'
        ...

    def keys(自身)->object:
        '下标迭代'
        ...

    def values(自身)->object:
        'class 迭代'
        ...

    def forEach(自身,callback: object,thisArg: object|None=None)->None:
        '逐个 class 调用'
        ...

class style(JavaScript对象):
    '元素的行内样式。驼峰 CSS 属性不逐个列'
    cssText: str=...
    cssFloat: str=...
    length: int=...
    parentRule: object=...
    def getPropertyValue(自身,property: str)->str:
        '读取属性值，没有是空字符串'
        ...

    def getPropertyPriority(自身,property: str)->str:
        '读取优先级，重要时是 important，否则是空字符串'
        ...

    def setProperty(自身,property: str,value: str,priority: str='')->None:
        '写入属性。priority 要重要时传 important'
        ...

    def removeProperty(自身,property: str)->str:
        '删除属性，返回删掉的值'
        ...

    def item(自身,index: int)->str:
        '按下标取属性名'
        ...

class CSSStyleSheet(JavaScript对象):
    '一张样式表'
    cssRules: object=...
    rules: object=...
    ownerNode: object=...
    ownerRule: object=...
    disabled: bool=...
    href: str|None=...
    title: str|None=...
    type: str=...
    media: object=...
    parentStyleSheet: object=...
    def insertRule(自身,rule: str,index: int=0)->int:
        '插入一条规则，返回下标'
        ...

    def deleteRule(自身,index: int)->None:
        '按下标删除规则'
        ...

    def replace(自身,text: str)->object:
        '整表替换，返回 Promise'
        ...

    def replaceSync(自身,text: str)->None:
        '整表同步替换'
        ...

    def addRule(自身,selector: str,style: str='',index: int|None=None)->int:
        '旧接口，插入一条样式规则'
        ...

    def removeRule(自身,index: int=0)->None:
        '旧接口，按下标删除'
        ...

class styleSheets(JavaScript对象):
    '页面上的样式表'
    length: int=...
    def item(自身,index: int)->CSSStyleSheet|None:
        '按下标取样式表，越界是 None'
        ...
