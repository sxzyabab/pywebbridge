'拼好的界面块。种类、侧向会再加「样式类-取值」，例如按钮-主要'
from ..元素.基础元素 import 元素
from .预制件 import 预制件

class 交互式控件(预制件):
    '能点的控件。禁用时根上另有样式类禁用'
    @property
    def 禁用(自身)->bool:
        '是否点不了'
        ...
    @禁用.setter
    def 禁用(自身,值: bool):
        ...

class 按钮(交互式控件):
    '圆角按钮。种类为主要、次要、危险、文字'
    样式类='按钮'
    @property
    def 文字(自身)->str:
        '按钮上的字'
        ...
    @文字.setter
    def 文字(自身,值: str):
        ...
    @property
    def 种类(自身)->str:
        '主要、次要、危险、文字'
        ...
    @种类.setter
    def 种类(自身,值: str):
        ...

class 图标按钮(按钮):
    '图标为主的按钮，文字可空'
    样式类='图标按钮'
    @property
    def 图标(自身)->str:
        '按钮上的图形'
        ...
    @图标.setter
    def 图标(自身,值: str):
        ...

class 开关(交互式控件):
    '左右滑动的开关。打开时另有样式类开'
    样式类='开关'
    @property
    def 开(自身)->bool:
        '是否打开'
        ...
    @开.setter
    def 开(自身,值: bool):
        ...

class 分段控制(交互式控件):
    '横排互斥的几项'
    样式类='分段控制'
    @property
    def 各项(自身)->list:
        '每一项的文字'
        ...
    @各项.setter
    def 各项(自身,值: list):
        ...
    @property
    def 当前(自身)->int:
        '选中项下标'
        ...
    @当前.setter
    def 当前(自身,值: int):
        ...

class 标签页(交互式控件):
    '一排标签，下面一块内容'
    样式类='标签页'
    @property
    def 各项(自身)->list:
        '每个标签的文字'
        ...
    @各项.setter
    def 各项(自身,值: list):
        ...
    @property
    def 当前(自身)->int:
        '当前标签下标'
        ...
    @当前.setter
    def 当前(自身,值: int):
        ...
    @property
    def 内容(自身)->元素:
        '当前标签下面的那一块'
        ...

class 搜索框(交互式控件):
    '带清空的搜索输入'
    样式类='搜索框'
    @property
    def 文字(自身)->str:
        '已经输入的字'
        ...
    @文字.setter
    def 文字(自身,值: str):
        ...
    @property
    def 占位(自身)->str:
        '没输入时的提示'
        ...
    @占位.setter
    def 占位(自身,值: str):
        ...
    def 清空(自身)->None:
        '清掉已输入的字'
        ...

class 菜单项(交互式控件):
    '菜单里的一行。危险时另有样式类危险'
    样式类='菜单项'
    @property
    def 文字(自身)->str:
        '这一行的字'
        ...
    @文字.setter
    def 文字(自身,值: str):
        ...
    @property
    def 危险(自身)->bool:
        '是否是会出事的操作'
        ...
    @危险.setter
    def 危险(自身,值: bool):
        ...

class 浮层(预制件):
    '浮在页面上的一层'
    样式类='浮层'
    @property
    def 开(自身)->bool:
        '是否正显示'
        ...
    def 打开(自身)->None:
        '显示出来'
        ...

    def 关闭(自身)->None:
        '收起来'
        ...

class 菜单(浮层):
    '点开后的一列操作'
    样式类='菜单'
    def 加入(自身,项: 菜单项)->None:
        '加一项到末尾'
        ...

class 下拉(交互式控件):
    '点开后从各项里选一项'
    样式类='下拉'
    @property
    def 各项(自身)->list:
        '可选项的文字'
        ...
    @各项.setter
    def 各项(自身,值: list):
        ...
    @property
    def 当前(自身)->int:
        '选中项下标'
        ...
    @当前.setter
    def 当前(自身,值: int):
        ...
    def 打开(自身)->None:
        '展开选项'
        ...

    def 关闭(自身)->None:
        '收起选项'
        ...

class 提示泡(浮层):
    '指着某个元素的短说明'
    样式类='提示泡'
    @property
    def 文字(自身)->str:
        '泡里的字'
        ...
    @文字.setter
    def 文字(自身,值: str):
        ...
    def 指向(自身,目标: 元素)->None:
        '显示在这个元素旁边'
        ...

class 吐司(浮层):
    '角落里短暂出现的一条。种类为提示、成功、失败'
    样式类='吐司'
    @property
    def 文字(自身)->str:
        '这条上的字'
        ...
    @文字.setter
    def 文字(自身,值: str):
        ...
    @property
    def 种类(自身)->str:
        '提示、成功、失败'
        ...
    @种类.setter
    def 种类(自身,值: str):
        ...

class 模态(浮层):
    '挡在页面中间的一块'
    样式类='模态'
    @property
    def 标题(自身)->str:
        '顶上的字'
        ...
    @标题.setter
    def 标题(自身,值: str):
        ...

class 确认框(模态):
    '模态上多一段说明，以及确定、取消'
    样式类='确认框'
    @property
    def 说明(自身)->str:
        '标题下面的字'
        ...
    @说明.setter
    def 说明(自身,值: str):
        ...
    @property
    def 确定文字(自身)->str:
        '确定按钮上的字'
        ...
    @确定文字.setter
    def 确定文字(自身,值: str):
        ...
    @property
    def 取消文字(自身)->str:
        '取消按钮上的字'
        ...
    @取消文字.setter
    def 取消文字(自身,值: str):
        ...

class 抽屉(浮层):
    '从一侧滑出的一块。侧为左、右'
    样式类='抽屉'
    @property
    def 标题(自身)->str:
        '顶上的字'
        ...
    @标题.setter
    def 标题(自身,值: str):
        ...
    @property
    def 侧(自身)->str:
        '左、右'
        ...
    @侧.setter
    def 侧(自身,值: str):
        ...

class 卡片(预制件):
    '圆角带阴影的一块内容'
    样式类='卡片'
    @property
    def 标题(自身)->str:
        '卡片顶上的字'
        ...
    @标题.setter
    def 标题(自身,值: str):
        ...

class 胶囊(预制件):
    '短的圆角标记'
    样式类='胶囊'
    @property
    def 文字(自身)->str:
        '标记上的字'
        ...
    @文字.setter
    def 文字(自身,值: str):
        ...

class 空状态(预制件):
    '没有内容时占着的一块'
    样式类='空状态'
    @property
    def 文字(自身)->str:
        '主要的那句'
        ...
    @文字.setter
    def 文字(自身,值: str):
        ...
    @property
    def 说明(自身)->str:
        '下面一行小字'
        ...
    @说明.setter
    def 说明(自身,值: str):
        ...

class 折叠行(预制件):
    '点标题展开的一行。展开时另有样式类展开'
    样式类='折叠行'
    @property
    def 标题(自身)->str:
        '这行的字'
        ...
    @标题.setter
    def 标题(自身,值: str):
        ...
    @property
    def 展开(自身)->bool:
        '内容是否露在外面'
        ...
    @展开.setter
    def 展开(自身,值: bool):
        ...

class 列表行(预制件):
    '左标题、右说明的一行'
    样式类='列表行'
    @property
    def 标题(自身)->str:
        '左边的字'
        ...
    @标题.setter
    def 标题(自身,值: str):
        ...
    @property
    def 说明(自身)->str:
        '右边的字'
        ...
    @说明.setter
    def 说明(自身,值: str):
        ...

class 键值行(预制件):
    '左边名字、右边值'
    样式类='键值行'
    @property
    def 名(自身)->str:
        '左边的名字'
        ...
    @名.setter
    def 名(自身,值: str):
        ...
    @property
    def 值(自身)->str:
        '右边的值'
        ...
    @值.setter
    def 值(自身,值: str):
        ...

class 代码块(预制件):
    '保留换行的一段代码'
    样式类='代码块'
    @property
    def 代码(自身)->str:
        '块里的文本'
        ...
    @代码.setter
    def 代码(自身,值: str):
        ...
    @property
    def 语言(自身)->str:
        '这段代码的语言'
        ...
    @语言.setter
    def 语言(自身,值: str):
        ...

class 树节点(预制件):
    '树上的一层。展开时另有样式类展开'
    样式类='树节点'
    @property
    def 文字(自身)->str:
        '这一层的字'
        ...
    @文字.setter
    def 文字(自身,值: str):
        ...
    @property
    def 展开(自身)->bool:
        '子层是否露在外面'
        ...
    @展开.setter
    def 展开(自身,值: bool):
        ...
    def 加入(自身,节点: '树节点')->None:
        '加一个子层到末尾'
        ...

class 树(预制件):
    '可展开的层级'
    样式类='树'
    def 加入(自身,节点: 树节点)->None:
        '加一个顶层节点到末尾'
        ...

class 状态点(预制件):
    '一颗圆点。种类为空闲、进行、成功、失败'
    样式类='状态点'
    @property
    def 种类(自身)->str:
        '空闲、进行、成功、失败'
        ...
    @种类.setter
    def 种类(自身,值: str):
        ...

class 路径标签(预制件):
    '等宽的一段路径'
    样式类='路径标签'
    @property
    def 路径(自身)->str:
        '显示出来的路径'
        ...
    @路径.setter
    def 路径(自身,值: str):
        ...

class 复制反馈(交互式控件):
    '点了之后换成已复制。已复制时另有样式类已复制'
    样式类='复制反馈'
    @property
    def 文字(自身)->str:
        '平时显示的字'
        ...
    @文字.setter
    def 文字(自身,值: str):
        ...
    def 标记已复制(自身)->None:
        '换成已复制的样子'
        ...

class 连接横幅(预制件):
    '顶上的一条连接状态。种类为正常、断开'
    样式类='连接横幅'
    @property
    def 文字(自身)->str:
        '横幅上的字'
        ...
    @文字.setter
    def 文字(自身,值: str):
        ...
    @property
    def 种类(自身)->str:
        '正常、断开'
        ...
    @种类.setter
    def 种类(自身,值: str):
        ...

class 披露行(交互式控件):
    '点标题露出下面的内容。展开时另有样式类展开'
    样式类='披露行'
    @property
    def 标题(自身)->str:
        '这行的字'
        ...
    @标题.setter
    def 标题(自身,值: str):
        ...
    @property
    def 展开(自身)->bool:
        '内容是否露在外面'
        ...
    @展开.setter
    def 展开(自身,值: bool):
        ...
    @property
    def 内容(自身)->元素:
        '标题下面的那一块'
        ...


class markdown(元素):
    ...

md=markdown