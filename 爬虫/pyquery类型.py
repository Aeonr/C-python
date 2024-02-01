from pyquery import PyQuery
html="""<li><a href="http://www.baidu.com">百度</a></li>"""
p=PyQuery(html)
#语法规则：pyquery对象直接（css选择器）,()可以一直往后加，链式操作
print(p("a"))
#p("li")("a")=p("li a")