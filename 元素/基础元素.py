from ..样式 import classList,style
from typing import Optional as 可选
from ..数据 import JavaScript对象

元素基本属性={
    'namespaceURI',
    'prefix',
    'localName',
    'tagName',
    'nodeName',
    'nodeType',
    'nodeValue',
    'id',
    'className',
    'slot',
    'innerHTML',
    'outerHTML',
    'textContent',
    'innerText',
    'outerText',
    'parentElement',
    'parentNode',
    'children',
    'childElementCount',
    'childNodes',
    'firstChild',
    'lastChild',
    'firstElementChild',
    'lastElementChild',
    'nextSibling',
    'previousSibling',
    'nextElementSibling',
    'previousElementSibling',
    'ownerDocument',
    'isConnected',
    'attributes',
    'dataset',
    'shadowRoot',
    'assignedSlot',
    'clientLeft',
    'clientTop',
    'clientWidth',
    'clientHeight',
    'scrollLeft',
    'scrollTop',
    'scrollWidth',
    'scrollHeight',
    'offsetParent',
    'offsetTop',
    'offsetLeft',
    'offsetWidth',
    'offsetHeight',
    'title',
    'lang',
    'dir',
    'hidden',
    'inert',
    'draggable',
    'spellcheck',
    'translate',
    'contentEditable',
    'isContentEditable',
    'tabIndex',
    'autofocus',
    'accessKey',
    'nonce',
    'autocapitalize',
    'autocorrect',
    'inputMode',
    'enterKeyHint',
    'popover',
    'role',
    'ariaAtomic',
    'ariaAutoComplete',
    'ariaBusy',
    'ariaChecked',
    'ariaColCount',
    'ariaColIndex',
    'ariaColSpan',
    'ariaCurrent',
    'ariaDescription',
    'ariaDisabled',
    'ariaExpanded',
    'ariaHasPopup',
    'ariaHidden',
    'ariaInvalid',
    'ariaKeyShortcuts',
    'ariaLabel',
    'ariaLevel',
    'ariaLive',
    'ariaModal',
    'ariaMultiLine',
    'ariaMultiSelectable',
    'ariaOrientation',
    'ariaPlaceholder',
    'ariaPosInSet',
    'ariaPressed',
    'ariaReadOnly',
    'ariaRelevant',
    'ariaRequired',
    'ariaRoleDescription',
    'ariaRowCount',
    'ariaRowIndex',
    'ariaRowSpan',
    'ariaSelected',
    'ariaSetSize',
    'ariaSort',
    'ariaValueMax',
    'ariaValueMin',
    'ariaValueNow',
    'ariaValueText',
}

class 元素(JavaScript对象):
    '所有元素的基类'
    元素标识:可选[str]=None
    自闭合:bool=None
    def __init__(自身):
        '固定存在的子对象'
        自身.classList=classList()
        自身.style=style()

    def getAttribute(自身,qualifiedName: str)->str|None:
        '读取属性，没有是 None'
        ...

    def getAttributeNS(自身,namespace: str|None,localName: str)->str|None:
        '按命名空间读取属性，没有是 None'
        ...

    def setAttribute(自身,qualifiedName: str,value: str)->None:
        '写入属性'
        ...

    def setAttributeNS(自身,namespace: str|None,qualifiedName: str,value: str)->None:
        '按命名空间写入属性'
        ...

    def removeAttribute(自身,qualifiedName: str)->None:
        '删除属性'
        ...

    def removeAttributeNS(自身,namespace: str|None,localName: str)->None:
        '按命名空间删除属性'
        ...

    def toggleAttribute(自身,qualifiedName: str,force: bool|None=None)->bool:
        '有就删、没有就加。force 为 True 时只加，False 时只删。返回是否还有'
        ...

    def hasAttribute(自身,qualifiedName: str)->bool:
        '有没有这个属性'
        ...

    def hasAttributeNS(自身,namespace: str|None,localName: str)->bool:
        '这个命名空间下有没有这个属性'
        ...

    def getAttributeNames(自身)->list:
        '全部属性名'
        ...

    def querySelector(自身,selectors: str)->object|None:
        '按选择器找第一个，没有是 None'
        ...

    def querySelectorAll(自身,selectors: str)->list:
        '按选择器找全部'
        ...

    def getElementsByClassName(自身,classNames: str)->object:
        '按 class 找，多个 class 用空格隔开'
        ...

    def getElementsByTagName(自身,qualifiedName: str)->object:
        '按标签名找'
        ...

    def getElementsByTagNameNS(自身,namespace: str|None,localName: str)->object:
        '按命名空间和标签名找'
        ...

    def closest(自身,selectors: str)->object|None:
        '自己或祖先里第一个匹配的，没有是 None'
        ...

    def matches(自身,selectors: str)->bool:
        '自己是否匹配选择器'
        ...

    def append(自身,*nodes: object)->None:
        '在末尾加上节点或字符串'
        ...

    def prepend(自身,*nodes: object)->None:
        '在开头加上节点或字符串'
        ...

    def replaceChildren(自身,*nodes: object)->None:
        '换成这些子节点，不传则清空'
        ...

    def before(自身,*nodes: object)->None:
        '在自己前面插入'
        ...

    def after(自身,*nodes: object)->None:
        '在自己后面插入'
        ...

    def replaceWith(自身,*nodes: object)->None:
        '用这些节点换掉自己'
        ...

    def remove(自身)->None:
        '从父节点移除自己'
        ...

    def appendChild(自身,node: object)->object:
        '把节点加到末尾'
        ...

    def removeChild(自身,child: object)->object:
        '移除子节点'
        ...

    def insertBefore(自身,node: object,child: object|None)->object:
        '插到 child 前面。child 为 None 时加到末尾'
        ...

    def replaceChild(自身,node: object,child: object)->object:
        '用 node 换掉 child'
        ...

    def insertAdjacentElement(自身,where: str,element: object)->object|None:
        'where 为 beforebegin、afterbegin、beforeend、afterend'
        ...

    def insertAdjacentHTML(自身,position: str,text: str)->None:
        'position 为 beforebegin、afterbegin、beforeend、afterend'
        ...

    def insertAdjacentText(自身,where: str,data: str)->None:
        'where 为 beforebegin、afterbegin、beforeend、afterend'
        ...

    def cloneNode(自身,deep: bool=False)->object:
        '复制节点。deep 为 True 时连子节点一起复制'
        ...

    def contains(自身,other: object|None)->bool:
        'other 是不是自己或后代'
        ...

    def hasChildNodes(自身)->bool:
        '有没有子节点'
        ...

    def normalize(自身)->None:
        '合并相邻文本节点，去掉空文本'
        ...

    def compareDocumentPosition(自身,other: object)->int:
        '比较两个节点在文档中的位置，返回位掩码'
        ...

    def isEqualNode(自身,otherNode: object|None)->bool:
        '结构是否相等'
        ...

    def isSameNode(自身,otherNode: object|None)->bool:
        '是不是同一个节点'
        ...

    def getRootNode(自身,options: dict|None=None)->object:
        '取根节点。options.composed 为 True 时穿过影子树'
        ...

    def lookupPrefix(自身,namespace: str|None)->str|None:
        '按命名空间找前缀'
        ...

    def lookupNamespaceURI(自身,prefix: str|None)->str|None:
        '按前缀找命名空间'
        ...

    def isDefaultNamespace(自身,namespace: str|None)->bool:
        '是不是默认命名空间'
        ...

    def getBoundingClientRect(自身)->dict:
        '返回 x、y、width、height、top、right、bottom、left'
        ...

    def getClientRects(自身)->list:
        '每行片段一个矩形，字段同 getBoundingClientRect'
        ...

    def scrollIntoView(自身,arg: bool|dict|None=None)->None:
        '滚到可见。字典可用 block、inline、behavior'
        ...

    def scroll(自身,x: float|dict|None=None,y: float|None=None)->None:
        '传两个数是横纵；只传字典时用 left、top、behavior'
        ...

    def scrollTo(自身,x: float|dict|None=None,y: float|None=None)->None:
        '滚到这个位置。传参同 scroll'
        ...

    def scrollBy(自身,x: float|dict|None=None,y: float|None=None)->None:
        '按偏移滚动。传参同 scroll'
        ...

    def attachShadow(自身,init: dict)->object:
        '挂上影子树。init.mode 为 open 或 closed'
        ...

    def computedStyleMap(自身)->object:
        '计算后样式的类型化映射'
        ...

    def getAnimations(自身)->list:
        '这个元素上的动画'
        ...

    def focus(自身,options: dict|None=None)->None:
        '聚焦。options 可用 preventScroll、focusVisible'
        ...

    def blur(自身)->None:
        '失焦'
        ...

    def click(自身)->None:
        '触发点击'
        ...

    def showPopover(自身)->None:
        '显示 popover'
        ...

    def hidePopover(自身)->None:
        '隐藏 popover'
        ...

    def togglePopover(自身,force: bool|None=None)->bool:
        '切换 popover，返回切换后是否显示'
        ...

    def addEventListener(自身,type: str,listener: object,options: bool|dict|None=None)->None:
        '监听事件。options 可以是捕获布尔，或含 capture、once、passive、signal 的字典'
        ...

    def removeEventListener(自身,type: str,listener: object,options: bool|dict|None=None)->None:
        '移除监听。capture 要和添加时一致'
        ...

    def dispatchEvent(自身,event: object)->bool:
        '派发事件。调用了 preventDefault 时返回 False'
        ...

element=元素

class documentElement(元素):
    'HTML文档'
    元素标识='<html>'

class head(元素):
    'HTML头'
    元素标识='<head>'

class body(元素):
    'HTML正文'
    元素标识='<body>'

class 可校验元素(元素):
    '带约束校验的元素共有的'
    @property
    def willValidate(自身)->bool:
        ...
    @property
    def validity(自身)->object:
        ...
    @property
    def validationMessage(自身)->str:
        ...
    def checkValidity(自身)->bool:
        '是否通过校验'
        ...

    def reportValidity(自身)->bool:
        '校验并把问题报告给用户，返回是否通过'
        ...

    def setCustomValidity(自身,error: str)->None:
        '设置自定义错误。传空字符串表示清除'
        ...

class 媒体元素(元素):
    'audio 和 video 共有的'
    NETWORK_EMPTY: int=0
    NETWORK_IDLE: int=1
    NETWORK_LOADING: int=2
    NETWORK_NO_SOURCE: int=3
    HAVE_NOTHING: int=0
    HAVE_METADATA: int=1
    HAVE_CURRENT_DATA: int=2
    HAVE_FUTURE_DATA: int=3
    HAVE_ENOUGH_DATA: int=4
    @property
    def src(自身)->str:
        ...
    @src.setter
    def src(自身,值: str):
        ...
    @property
    def currentSrc(自身)->str:
        ...
    @property
    def srcObject(自身)->object:
        ...
    @srcObject.setter
    def srcObject(自身,值: object):
        ...
    @property
    def crossOrigin(自身)->str|None:
        ...
    @crossOrigin.setter
    def crossOrigin(自身,值: str|None):
        ...
    @property
    def preload(自身)->str:
        ...
    @preload.setter
    def preload(自身,值: str):
        ...
    @property
    def networkState(自身)->int:
        ...
    @property
    def buffered(自身)->object:
        ...
    @property
    def readyState(自身)->int:
        ...
    @property
    def seeking(自身)->bool:
        ...
    @property
    def currentTime(自身)->float:
        ...
    @currentTime.setter
    def currentTime(自身,值: float):
        ...
    @property
    def duration(自身)->float:
        ...
    @property
    def paused(自身)->bool:
        ...
    @property
    def defaultPlaybackRate(自身)->float:
        ...
    @defaultPlaybackRate.setter
    def defaultPlaybackRate(自身,值: float):
        ...
    @property
    def playbackRate(自身)->float:
        ...
    @playbackRate.setter
    def playbackRate(自身,值: float):
        ...
    @property
    def preservesPitch(自身)->bool:
        ...
    @preservesPitch.setter
    def preservesPitch(自身,值: bool):
        ...
    @property
    def played(自身)->object:
        ...
    @property
    def seekable(自身)->object:
        ...
    @property
    def ended(自身)->bool:
        ...
    @property
    def autoplay(自身)->bool:
        ...
    @autoplay.setter
    def autoplay(自身,值: bool):
        ...
    @property
    def loop(自身)->bool:
        ...
    @loop.setter
    def loop(自身,值: bool):
        ...
    @property
    def controls(自身)->bool:
        ...
    @controls.setter
    def controls(自身,值: bool):
        ...
    @property
    def volume(自身)->float:
        ...
    @volume.setter
    def volume(自身,值: float):
        ...
    @property
    def muted(自身)->bool:
        ...
    @muted.setter
    def muted(自身,值: bool):
        ...
    @property
    def defaultMuted(自身)->bool:
        ...
    @defaultMuted.setter
    def defaultMuted(自身,值: bool):
        ...
    @property
    def error(自身)->object:
        ...
    @property
    def textTracks(自身)->object:
        ...
    @property
    def audioTracks(自身)->object:
        ...
    @property
    def videoTracks(自身)->object:
        ...
    @property
    def sinkId(自身)->str:
        ...
    @property
    def remote(自身)->object:
        ...
    @property
    def disableRemotePlayback(自身)->bool:
        ...
    @disableRemotePlayback.setter
    def disableRemotePlayback(自身,值: bool):
        ...
    def load(自身)->None:
        '重新加载媒体'
        ...

    def canPlayType(自身,type: str)->str:
        '返回空字符串、maybe 或 probably'
        ...

    def play(自身)->object:
        '播放，返回 Promise'
        ...

    def pause(自身)->None:
        '暂停'
        ...

    def fastSeek(自身,time: float)->None:
        '快进到这个秒数'
        ...

    def getStartDate(自身)->object:
        '媒体时间线的起点日期'
        ...

    def addTextTrack(自身,kind: str,label: str='',language: str='')->object:
        '加上文字轨。kind 为 subtitles、captions、descriptions、chapters、metadata'
        ...

    def setSinkId(自身,sinkId: str)->object:
        '换音频输出设备，返回 Promise'
        ...

class 单元格(元素):
    'td 和 th 共有的'
    @property
    def colSpan(自身)->int:
        ...
    @colSpan.setter
    def colSpan(自身,值: int):
        ...
    @property
    def rowSpan(自身)->int:
        ...
    @rowSpan.setter
    def rowSpan(自身,值: int):
        ...
    @property
    def headers(自身)->str:
        ...
    @headers.setter
    def headers(自身,值: str):
        ...
    @property
    def cellIndex(自身)->int:
        ...
    @property
    def scope(自身)->str:
        ...
    @scope.setter
    def scope(自身,值: str):
        ...
    @property
    def abbr(自身)->str:
        ...
    @abbr.setter
    def abbr(自身,值: str):
        ...

class 表格区(元素):
    'thead、tbody、tfoot 共有的'
    @property
    def rows(自身)->object:
        ...
    def insertRow(自身,index: int=-1)->object:
        '插入一行。-1 加到末尾'
        ...

    def deleteRow(自身,index: int)->None:
        '按下标删除一行'
        ...

class address(元素):
    '联系地址'
    元素标识='<address>'

class article(元素):
    '独立成篇的内容'
    元素标识='<article>'

class aside(元素):
    '旁边的附属内容'
    元素标识='<aside>'

class audio(媒体元素):
    '音频'
    元素标识='<audio>'

class base(元素):
    '页面链接的基准地址'
    元素标识='<base>'
    自闭合=True
    @property
    def href(自身)->str:
        ...
    @href.setter
    def href(自身,值: str):
        ...
    @property
    def target(自身)->str:
        ...
    @target.setter
    def target(自身,值: str):
        ...

class canvas(元素):
    '画布'
    元素标识='<canvas>'
    @property
    def width(自身)->int:
        ...
    @width.setter
    def width(自身,值: int):
        ...
    @property
    def height(自身)->int:
        ...
    @height.setter
    def height(自身,值: int):
        ...
    def getContext(自身,contextId: str,options: dict|None=None)->object|None:
        '取绘制上下文。contextId 为 2d、bitmaprenderer、webgl、webgl2、webgpu。没有是 None'
        ...

    def toDataURL(自身,type: str='image/png',quality: float|None=None)->str:
        '导出成 data URL'
        ...

    def toBlob(自身,callback: object,type: str='image/png',quality: float|None=None)->None:
        '导出成图片二进制，完成后调用 callback'
        ...

    def captureStream(自身,frameRate: float|None=None)->object:
        '把画面收成媒体流'
        ...

    def transferControlToOffscreen(自身)->object:
        '把控制权交给离屏画布'
        ...

class caption(元素):
    '表格标题'
    元素标识='<caption>'

class col(元素):
    '表格的一列'
    元素标识='<col>'
    自闭合=True
    @property
    def span(自身)->int:
        ...
    @span.setter
    def span(自身,值: int):
        ...

class colgroup(元素):
    '表格的一组列'
    元素标识='<colgroup>'
    @property
    def span(自身)->int:
        ...
    @span.setter
    def span(自身,值: int):
        ...

class data(元素):
    '带机器可读值的内容'
    元素标识='<data>'
    @property
    def value(自身)->str:
        ...
    @value.setter
    def value(自身,值: str):
        ...

class dd(元素):
    '描述列表中的说明'
    元素标识='<dd>'

class div(元素):
    '通用容器'
    元素标识='<div>'

class dl(元素):
    '描述列表'
    元素标识='<dl>'

class dt(元素):
    '描述列表中的术语'
    元素标识='<dt>'

class embed(元素):
    '嵌入的外部内容'
    元素标识='<embed>'
    自闭合=True
    @property
    def src(自身)->str:
        ...
    @src.setter
    def src(自身,值: str):
        ...
    @property
    def type(自身)->str:
        ...
    @type.setter
    def type(自身,值: str):
        ...
    @property
    def width(自身)->str:
        ...
    @width.setter
    def width(自身,值: str):
        ...
    @property
    def height(自身)->str:
        ...
    @height.setter
    def height(自身,值: str):
        ...
    def getSVGDocument(自身)->object|None:
        '嵌入的 SVG 文档，没有是 None'
        ...

class figcaption(元素):
    '图的说明'
    元素标识='<figcaption>'

class figure(元素):
    '独立的图'
    元素标识='<figure>'

class footer(元素):
    '页脚'
    元素标识='<footer>'

class header(元素):
    '页眉'
    元素标识='<header>'

class hgroup(元素):
    '标题组'
    元素标识='<hgroup>'

class iframe(元素):
    '嵌入的页面'
    元素标识='<iframe>'
    @property
    def src(自身)->str:
        ...
    @src.setter
    def src(自身,值: str):
        ...
    @property
    def srcdoc(自身)->str:
        ...
    @srcdoc.setter
    def srcdoc(自身,值: str):
        ...
    @property
    def name(自身)->str:
        ...
    @name.setter
    def name(自身,值: str):
        ...
    @property
    def sandbox(自身)->object:
        ...
    @property
    def allow(自身)->str:
        ...
    @allow.setter
    def allow(自身,值: str):
        ...
    @property
    def allowFullscreen(自身)->bool:
        ...
    @allowFullscreen.setter
    def allowFullscreen(自身,值: bool):
        ...
    @property
    def width(自身)->str:
        ...
    @width.setter
    def width(自身,值: str):
        ...
    @property
    def height(自身)->str:
        ...
    @height.setter
    def height(自身,值: str):
        ...
    @property
    def referrerPolicy(自身)->str:
        ...
    @referrerPolicy.setter
    def referrerPolicy(自身,值: str):
        ...
    @property
    def loading(自身)->str:
        ...
    @loading.setter
    def loading(自身,值: str):
        ...
    @property
    def contentDocument(自身)->object:
        ...
    @property
    def contentWindow(自身)->object:
        ...
    def getSVGDocument(自身)->object|None:
        '嵌入的 SVG 文档，没有是 None'
        ...

class img(元素):
    '图片'
    元素标识='<img>'
    自闭合=True
    @property
    def alt(自身)->str:
        ...
    @alt.setter
    def alt(自身,值: str):
        ...
    @property
    def src(自身)->str:
        ...
    @src.setter
    def src(自身,值: str):
        ...
    @property
    def srcset(自身)->str:
        ...
    @srcset.setter
    def srcset(自身,值: str):
        ...
    @property
    def sizes(自身)->str:
        ...
    @sizes.setter
    def sizes(自身,值: str):
        ...
    @property
    def crossOrigin(自身)->str|None:
        ...
    @crossOrigin.setter
    def crossOrigin(自身,值: str|None):
        ...
    @property
    def useMap(自身)->str:
        ...
    @useMap.setter
    def useMap(自身,值: str):
        ...
    @property
    def isMap(自身)->bool:
        ...
    @isMap.setter
    def isMap(自身,值: bool):
        ...
    @property
    def width(自身)->int:
        ...
    @width.setter
    def width(自身,值: int):
        ...
    @property
    def height(自身)->int:
        ...
    @height.setter
    def height(自身,值: int):
        ...
    @property
    def naturalWidth(自身)->int:
        ...
    @property
    def naturalHeight(自身)->int:
        ...
    @property
    def complete(自身)->bool:
        ...
    @property
    def currentSrc(自身)->str:
        ...
    @property
    def referrerPolicy(自身)->str:
        ...
    @referrerPolicy.setter
    def referrerPolicy(自身,值: str):
        ...
    @property
    def decoding(自身)->str:
        ...
    @decoding.setter
    def decoding(自身,值: str):
        ...
    @property
    def loading(自身)->str:
        ...
    @loading.setter
    def loading(自身,值: str):
        ...
    @property
    def fetchPriority(自身)->str:
        ...
    @fetchPriority.setter
    def fetchPriority(自身,值: str):
        ...
    def decode(自身)->object:
        '解码完成，返回 Promise'
        ...

class li(元素):
    '列表项'
    元素标识='<li>'
    @property
    def value(自身)->int:
        ...
    @value.setter
    def value(自身,值: int):
        ...

class link(元素):
    '关联的外部资源'
    元素标识='<link>'
    自闭合=True
    @property
    def href(自身)->str:
        ...
    @href.setter
    def href(自身,值: str):
        ...
    @property
    def crossOrigin(自身)->str|None:
        ...
    @crossOrigin.setter
    def crossOrigin(自身,值: str|None):
        ...
    @property
    def rel(自身)->str:
        ...
    @rel.setter
    def rel(自身,值: str):
        ...
    @property
    def as_(自身)->str:
        ...
    @as_.setter
    def as_(自身,值: str):
        ...
    @property
    def relList(自身)->object:
        ...
    @property
    def media(自身)->str:
        ...
    @media.setter
    def media(自身,值: str):
        ...
    @property
    def hreflang(自身)->str:
        ...
    @hreflang.setter
    def hreflang(自身,值: str):
        ...
    @property
    def type(自身)->str:
        ...
    @type.setter
    def type(自身,值: str):
        ...
    @property
    def sizes(自身)->object:
        ...
    @property
    def imageSrcset(自身)->str:
        ...
    @imageSrcset.setter
    def imageSrcset(自身,值: str):
        ...
    @property
    def imageSizes(自身)->str:
        ...
    @imageSizes.setter
    def imageSizes(自身,值: str):
        ...
    @property
    def referrerPolicy(自身)->str:
        ...
    @referrerPolicy.setter
    def referrerPolicy(自身,值: str):
        ...
    @property
    def disabled(自身)->bool:
        ...
    @disabled.setter
    def disabled(自身,值: bool):
        ...
    @property
    def integrity(自身)->str:
        ...
    @integrity.setter
    def integrity(自身,值: str):
        ...
    @property
    def fetchPriority(自身)->str:
        ...
    @fetchPriority.setter
    def fetchPriority(自身,值: str):
        ...
    @property
    def blocking(自身)->object:
        ...
    @property
    def sheet(自身)->object:
        ...

setattr(link,'as',link.as_)
delattr(link,'as_')

class main(元素):
    '页面的主要内容'
    元素标识='<main>'

class map(元素):
    '图片热区'
    元素标识='<map>'
    @property
    def name(自身)->str:
        ...
    @name.setter
    def name(自身,值: str):
        ...
    @property
    def areas(自身)->object:
        ...

class menu(元素):
    '菜单'
    元素标识='<menu>'

class meta(元素):
    '页面元数据'
    元素标识='<meta>'
    自闭合=True
    @property
    def name(自身)->str:
        ...
    @name.setter
    def name(自身,值: str):
        ...
    @property
    def httpEquiv(自身)->str:
        ...
    @httpEquiv.setter
    def httpEquiv(自身,值: str):
        ...
    @property
    def content(自身)->str:
        ...
    @content.setter
    def content(自身,值: str):
        ...
    @property
    def media(自身)->str:
        ...
    @media.setter
    def media(自身,值: str):
        ...

class nav(元素):
    '导航'
    元素标识='<nav>'

class noscript(元素):
    '脚本不可用时显示的内容'
    元素标识='<noscript>'

class objectElement(可校验元素):
    '嵌入的外部对象'
    元素标识='<object>'
    @property
    def data(自身)->str:
        ...
    @data.setter
    def data(自身,值: str):
        ...
    @property
    def type(自身)->str:
        ...
    @type.setter
    def type(自身,值: str):
        ...
    @property
    def name(自身)->str:
        ...
    @name.setter
    def name(自身,值: str):
        ...
    @property
    def form(自身)->object:
        ...
    @property
    def width(自身)->str:
        ...
    @width.setter
    def width(自身,值: str):
        ...
    @property
    def height(自身)->str:
        ...
    @height.setter
    def height(自身,值: str):
        ...
    @property
    def contentDocument(自身)->object:
        ...
    @property
    def contentWindow(自身)->object:
        ...
    def getSVGDocument(自身)->object|None:
        '嵌入的 SVG 文档，没有是 None'
        ...

class ol(元素):
    '有序列表'
    元素标识='<ol>'
    @property
    def reversed(自身)->bool:
        ...
    @reversed.setter
    def reversed(自身,值: bool):
        ...
    @property
    def start(自身)->int:
        ...
    @start.setter
    def start(自身,值: int):
        ...
    @property
    def type(自身)->str:
        ...
    @type.setter
    def type(自身,值: str):
        ...

class picture(元素):
    '按条件选用的图片'
    元素标识='<picture>'

class script(元素):
    '脚本'
    元素标识='<script>'
    @property
    def src(自身)->str:
        ...
    @src.setter
    def src(自身,值: str):
        ...
    @property
    def type(自身)->str:
        ...
    @type.setter
    def type(自身,值: str):
        ...
    @property
    def noModule(自身)->bool:
        ...
    @noModule.setter
    def noModule(自身,值: bool):
        ...
    @property
    def 异步(自身)->bool:
        ...
    @异步.setter
    def 异步(自身,值: bool):
        ...
    @property
    def defer(自身)->bool:
        ...
    @defer.setter
    def defer(自身,值: bool):
        ...
    @property
    def crossOrigin(自身)->str|None:
        ...
    @crossOrigin.setter
    def crossOrigin(自身,值: str|None):
        ...
    @property
    def text(自身)->str:
        ...
    @text.setter
    def text(自身,值: str):
        ...
    @property
    def integrity(自身)->str:
        ...
    @integrity.setter
    def integrity(自身,值: str):
        ...
    @property
    def referrerPolicy(自身)->str:
        ...
    @referrerPolicy.setter
    def referrerPolicy(自身,值: str):
        ...
    @property
    def fetchPriority(自身)->str:
        ...
    @fetchPriority.setter
    def fetchPriority(自身,值: str):
        ...
    @property
    def blocking(自身)->object:
        ...

setattr(script,'async',script.异步)
delattr(script,'异步')

class search(元素):
    '搜索区域'
    元素标识='<search>'

class section(元素):
    '章节'
    元素标识='<section>'

class slot(元素):
    '插槽'
    元素标识='<slot>'
    @property
    def name(自身)->str:
        ...
    @name.setter
    def name(自身,值: str):
        ...
    def assignedNodes(自身,options: dict|None=None)->list:
        '分配到这个插槽的节点。options.flatten 为 True 时展开嵌套插槽'
        ...

    def assignedElements(自身,options: dict|None=None)->list:
        '分配到这个插槽的元素。options 同 assignedNodes'
        ...

class source(元素):
    '图片或媒体的来源'
    元素标识='<source>'
    自闭合=True
    @property
    def src(自身)->str:
        ...
    @src.setter
    def src(自身,值: str):
        ...
    @property
    def type(自身)->str:
        ...
    @type.setter
    def type(自身,值: str):
        ...
    @property
    def srcset(自身)->str:
        ...
    @srcset.setter
    def srcset(自身,值: str):
        ...
    @property
    def sizes(自身)->str:
        ...
    @sizes.setter
    def sizes(自身,值: str):
        ...
    @property
    def media(自身)->str:
        ...
    @media.setter
    def media(自身,值: str):
        ...
    @property
    def width(自身)->int:
        ...
    @width.setter
    def width(自身,值: int):
        ...
    @property
    def height(自身)->int:
        ...
    @height.setter
    def height(自身,值: int):
        ...

class styleElement(元素):
    '样式'
    元素标识='<style>'
    @property
    def disabled(自身)->bool:
        ...
    @disabled.setter
    def disabled(自身,值: bool):
        ...
    @property
    def media(自身)->str:
        ...
    @media.setter
    def media(自身,值: str):
        ...
    @property
    def blocking(自身)->object:
        ...
    @property
    def sheet(自身)->object:
        ...

class table(元素):
    '表格'
    元素标识='<table>'
    @property
    def caption(自身)->object:
        ...
    @caption.setter
    def caption(自身,值: object):
        ...
    @property
    def tHead(自身)->object:
        ...
    @tHead.setter
    def tHead(自身,值: object):
        ...
    @property
    def tFoot(自身)->object:
        ...
    @tFoot.setter
    def tFoot(自身,值: object):
        ...
    @property
    def tBodies(自身)->object:
        ...
    @property
    def rows(自身)->object:
        ...
    def createCaption(自身)->object:
        '有标题就返回，没有就创建'
        ...

    def deleteCaption(自身)->None:
        '删除标题'
        ...

    def createTHead(自身)->object:
        '有表头就返回，没有就创建'
        ...

    def deleteTHead(自身)->None:
        '删除表头'
        ...

    def createTFoot(自身)->object:
        '有表尾就返回，没有就创建'
        ...

    def deleteTFoot(自身)->None:
        '删除表尾'
        ...

    def createTBody(自身)->object:
        '新建一个 tbody'
        ...

    def insertRow(自身,index: int=-1)->object:
        '插入一行。-1 加到末尾'
        ...

    def deleteRow(自身,index: int)->None:
        '按下标删除一行'
        ...

class tbody(表格区):
    '表体'
    元素标识='<tbody>'

class td(单元格):
    '单元格'
    元素标识='<td>'

class template(元素):
    '模板'
    元素标识='<template>'
    @property
    def content(自身)->object:
        ...
    @property
    def shadowRootMode(自身)->str:
        ...
    @shadowRootMode.setter
    def shadowRootMode(自身,值: str):
        ...
    @property
    def shadowRootDelegatesFocus(自身)->bool:
        ...
    @shadowRootDelegatesFocus.setter
    def shadowRootDelegatesFocus(自身,值: bool):
        ...
    @property
    def shadowRootClonable(自身)->bool:
        ...
    @shadowRootClonable.setter
    def shadowRootClonable(自身,值: bool):
        ...
    @property
    def shadowRootSerializable(自身)->bool:
        ...
    @shadowRootSerializable.setter
    def shadowRootSerializable(自身,值: bool):
        ...

class tfoot(表格区):
    '表尾'
    元素标识='<tfoot>'

class th(单元格):
    '表头单元格'
    元素标识='<th>'

class thead(表格区):
    '表头'
    元素标识='<thead>'

class time(元素):
    '日期或时间'
    元素标识='<time>'
    @property
    def dateTime(自身)->str:
        ...
    @dateTime.setter
    def dateTime(自身,值: str):
        ...

class title(元素):
    '文档标题'
    元素标识='<title>'
    @property
    def text(自身)->str:
        ...
    @text.setter
    def text(自身,值: str):
        ...

class tr(元素):
    '表格的一行'
    元素标识='<tr>'
    @property
    def rowIndex(自身)->int:
        ...
    @property
    def sectionRowIndex(自身)->int:
        ...
    @property
    def cells(自身)->object:
        ...
    def insertCell(自身,index: int=-1)->object:
        '插入单元格。-1 加到末尾'
        ...

    def deleteCell(自身,index: int)->None:
        '按下标删除单元格'
        ...

class track(元素):
    '媒体的文字轨道'
    元素标识='<track>'
    自闭合=True
    NONE: int=0
    LOADING: int=1
    LOADED: int=2
    ERROR: int=3
    @property
    def kind(自身)->str:
        ...
    @kind.setter
    def kind(自身,值: str):
        ...
    @property
    def src(自身)->str:
        ...
    @src.setter
    def src(自身,值: str):
        ...
    @property
    def srclang(自身)->str:
        ...
    @srclang.setter
    def srclang(自身,值: str):
        ...
    @property
    def label(自身)->str:
        ...
    @label.setter
    def label(自身,值: str):
        ...
    @property
    def default(自身)->bool:
        ...
    @default.setter
    def default(自身,值: bool):
        ...
    @property
    def readyState(自身)->int:
        ...
    @property
    def track(自身)->object:
        ...

class ul(元素):
    '无序列表'
    元素标识='<ul>'

class video(媒体元素):
    '视频'
    元素标识='<video>'
    @property
    def width(自身)->int:
        ...
    @width.setter
    def width(自身,值: int):
        ...
    @property
    def height(自身)->int:
        ...
    @height.setter
    def height(自身,值: int):
        ...
    @property
    def videoWidth(自身)->int:
        ...
    @property
    def videoHeight(自身)->int:
        ...
    @property
    def poster(自身)->str:
        ...
    @poster.setter
    def poster(自身,值: str):
        ...
    @property
    def playsInline(自身)->bool:
        ...
    @playsInline.setter
    def playsInline(自身,值: bool):
        ...
    @property
    def disablePictureInPicture(自身)->bool:
        ...
    @disablePictureInPicture.setter
    def disablePictureInPicture(自身,值: bool):
        ...
    def requestPictureInPicture(自身)->object:
        '进入画中画，返回 Promise'
        ...

    def getVideoPlaybackQuality(自身)->object:
        '播放质量计数'
        ...

    def requestVideoFrameCallback(自身,callback: object)->int:
        '下一帧画面时调用，返回编号'
        ...

    def cancelVideoFrameCallback(自身,handle: int)->None:
        '取消下一帧画面回调'
        ...

class 未知元素(元素):
    '浏览器不认识的标签'