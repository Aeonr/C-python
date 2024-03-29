#xpath是在xml中搜索内容的语言
#html是xml的一个子集
from lxml import etree
xml="""
<book>
    <id>1</id>
    <name>野花</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">周大强</nick>
        <nick id="10010">周芷若</nick>
        <nick class="joy">周结论</nick>
        <nick class="jolin">蔡依林</nick>
        <div>
            <nick>热</nick>
        </div>
    </author>
    
    <partner>
        <nick id="ppc">胖胖陈</nick>
        <nick id="ppbc">胖胖不陈</nick>
    </partner>
</book>
"""
tree=etree.XML(xml)
#r=tree.xpath("/book") #/表示层级关系
#r=tree.xpath("/book/name/text()") # text()拿文本
#r=tree.xpath("/book/author/nick/text()")
#r=tree.xpath("/book/author//nick/text()")#//表示找到所有的nick
#r=tree.xpath("/book/author/*/nick/text()")#*表示找到任意节点，通配符
#r=tree.xpath("/book/author/nick[1]/text()")#[]数字表示索引，从1开始；@标签="标签值"表示索引属性
#print(r)
list=tree.xpath("/book/author/nick")
print(list)
for i in list:
    a=i.xpath("./text()") #. ：表示相对查找，接着上面的路径
    print(a)
    #a=i.xpath("./@href")  拿到属性值