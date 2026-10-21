'换行,加粗等排版用标签'
from .基础元素 import 元素

class abbr(元素):
    '缩写'
    元素标识='<abbr>'

class b(元素):
    '需要注意的文字'
    元素标识='<b>'

class bdi(元素):
    '隔开文字方向'
    元素标识='<bdi>'

class bdo(元素):
    '指定文字方向'
    元素标识='<bdo>'

class blockquote(元素):
    '成段引用'
    元素标识='<blockquote>'
    @property
    def cite(自身)->str:
        ...
    @cite.setter
    def cite(自身,值: str):
        ...

class br(元素):
    '换行'
    元素标识='<br>'
    自闭合=True

class cite(元素):
    '作品名称'
    元素标识='<cite>'

class code(元素):
    '代码'
    元素标识='<code>'

class delElement(元素):
    '已删除的内容'
    元素标识='<del>'
    @property
    def cite(自身)->str:
        ...
    @cite.setter
    def cite(自身,值: str):
        ...
    @property
    def dateTime(自身)->str:
        ...
    @dateTime.setter
    def dateTime(自身,值: str):
        ...

class dfn(元素):
    '术语定义'
    元素标识='<dfn>'

class em(元素):
    '强调的文字'
    元素标识='<em>'

class h1(元素):
    '一级标题'
    元素标识='<h1>'

class h2(元素):
    '二级标题'
    元素标识='<h2>'

class h3(元素):
    '三级标题'
    元素标识='<h3>'

class h4(元素):
    '四级标题'
    元素标识='<h4>'

class h5(元素):
    '五级标题'
    元素标识='<h5>'

class h6(元素):
    '六级标题'
    元素标识='<h6>'

class hr(元素):
    '主题之间的分隔'
    元素标识='<hr>'
    自闭合=True

class i(元素):
    '不同于正文的文字'
    元素标识='<i>'

class ins(元素):
    '后加的内容'
    元素标识='<ins>'
    @property
    def cite(自身)->str:
        ...
    @cite.setter
    def cite(自身,值: str):
        ...
    @property
    def dateTime(自身)->str:
        ...
    @dateTime.setter
    def dateTime(自身,值: str):
        ...

class kbd(元素):
    '键盘输入'
    元素标识='<kbd>'

class mark(元素):
    '标出的文字'
    元素标识='<mark>'

class p(元素):
    '段落'
    元素标识='<p>'

class pre(元素):
    '保留空格和换行的文字'
    元素标识='<pre>'

class q(元素):
    '行内引用'
    元素标识='<q>'
    @property
    def cite(自身)->str:
        ...
    @cite.setter
    def cite(自身,值: str):
        ...

class rp(元素):
    '不支持注音时的括号'
    元素标识='<rp>'

class rt(元素):
    '注音文字'
    元素标识='<rt>'

class ruby(元素):
    '带注音的文字'
    元素标识='<ruby>'

class s(元素):
    '已经不对的文字'
    元素标识='<s>'

class samp(元素):
    '程序输出的样例'
    元素标识='<samp>'

class small(元素):
    '附属的小字'
    元素标识='<small>'

class span(元素):
    '一段行内文字'
    元素标识='<span>'

class strong(元素):
    '重要的文字'
    元素标识='<strong>'

class sub(元素):
    '下标'
    元素标识='<sub>'

class sup(元素):
    '上标'
    元素标识='<sup>'

class u(元素):
    '带标注的文字'
    元素标识='<u>'

class var(元素):
    '变量'
    元素标识='<var>'

class wbr(元素):
    '可以换行的位置'
    元素标识='<wbr>'
    自闭合=True
