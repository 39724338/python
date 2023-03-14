from lxml import etree

# text = '''
# <table border="2">
#     <tr>
#         <th>标题1</th>
#         <th>标题2</th>
#     </tr>
#     <tr>
#         <th>内容1</th>
#         <th>内容2
#     </tr>
# </table>>'''
# html = etree.HTML(text)#类似open函数，调用HTML类进行初始化，解析字符串常量HTML文档,成功构造了一个XPath解析对象。
# result= etree.tostring(html,encoding="utf-8")#将元素序列化为其XML树的编码字符串表示形式，最后一个li节点没有闭合，自动修正，但返回的为bytes类型数据
# print(result.decode('utf-8')) #decode将数据转换为utf-8的字符串类型

'''解析html文档的方法'''
# from lxml import etree   #html   xml
# html = etree.parse('解析html.html',etree.HTMLParser()) #HTMLParser解析器可以将HTML读入普通的XML树
# result= etree.tostring(html,encoding='utf-8')
# print(result.decode('utf-8'))


'''表达式选择内容'''
# from lxml import etree  #f = open()print(f)_
# html = etree.parse('解析html.html',etree.HTMLParser()) #HTMLParser解析器可以将HTML读入普通的XML树
# result_1= html.xpath('/tr')  #lxml库其实本质上是将xpath规则结合进来的，
# print(result_1)
# result_2 = html.xpath('//span')
# print(result_2)
# result_3 = html.xpath('//span/text()')
# print(result_3)

'''XPath常用规则
______________________________________________
表达式                     描述
----------------------------------------------
nodename            选取此节点的所有子节点
   /                从当前节点选取直接子节点
  //                从当前节点选取子孙节点
   .                选取当前节点
   ..               选取当前节点的父节点
   @                选取属性
----------------------------------------------
   
'''
# from lxml import etree
# html = etree.parse('解析html.html',etree.HTMLParser())
# result_0 = html.xpath('.')   #根节点，从返回的对象中显示html
# print(result_0)
# result_1 = html.xpath('./*')  #匹配根节点的所有子节点
# print(result_1)
# result_1 = html.xpath('.//*') #匹配根节点的所有子孙节点
# print(result_1)
# result_1 = html.xpath('/head/link')  #.//link
# print(result_1)
# result_2 = html.xpath('//div/h3')  #获取h3标签，父标签位div
# print(result_2)
# result_2 = html.xpath('//tr/..')   #获取tr标签的父标签
# print(result_2)
# result_3 = html.xpath('./@lang')   #获取根标签的属性
# print(result_3)
# result_3 = html.xpath('//table[@border="3"]')#获取指定属性的标签
# print(result_3)
# result_4 = html.xpath('//li[@class ="li li-first "]') #当包含了多个属性值时
# print(result_4)
#属性值非常多，
# result_4 = html.xpath('//li[contains(@class,"li")]') #可以使用contains函数
# print(result_4)
# result_4 = html.xpath('//table/@border')
# print(result_4)
# result_5 = html.xpath('//h3/text()') #文本获取
# print(result_5)

'''########运算符##############'''
from lxml import etree
html = etree.parse('解析html.html',etree.HTMLParser())
# result_0 = html.xpath('//li[@class ="one" name="jia"]')#错误
# result_0 = html.xpath('//li[contains(@class,"one") and contains(@name,"jia")]')#如果标签属性有两个属性内容，需要使用contains来获取
# result_0 = html.xpath('//li[contains(@class,"one") or contains(@name,"jia")]/text()')
# result_0 = html.xpath('//li[1]/text()')#使用索引的方式获取指定标签，但从1开始
# result_0 = html.xpath('//li[5mod2]/text()')  #5%2 =1,获取的是第一个标签,/text()
# result_0 = html.xpath('//li[last()]/text()')
# result_0 = html.xpath('//li[last()-1]/text()')
# result_0 = html.xpath('//li[position()<3]/text()')#位置小于3的，序号为1、2的标签
# print(result_0)

'''________________________________________________________________________________________
运算符   描述	            实例	                返回值
or	    或	            contains(class ="1") or contains(name="2")	   	
and	    与	            contains(class ="1") and contains(name="2")    
mod	    计算除法的余数	5 mod 2	                    1
|	    计算两个节点集	//book | //cd	            返回所有拥有 book 和 cd 元素的节点集
+	    加法	        6 + 4	                    10
-	    减法	        6 - 4	                    2
*	    乘法	        6 * 4	                    24
div	    除法	        8 div 4	                    2
=	    等于	        class=5	                如果class是5，则返回true。如果class是6，则返回false。
!=	    不等于	        class!=5	            如果class是6，则返回true。如果class是5，则返回false。
<	    小于	        class<5	                如果class是4，则返回true。如果class是6，则返回false。
<=	    小于或等于	    class<=5	            如果class是5，则返回true。如果class是6，则返回false。
>	    大于	        class>5	                如果class是6，则返回true。如果class是4，则返回false。
>=	    大于或等于	    class>=5	            如果class是5，则返回true。如果class是4，则返回false。
-------------------------------------------------------------------------------------
'''

'''节点轴'''
from lxml import etree
html = etree.parse('解析html.html',etree.HTMLParser())
# result_0 = html.xpath('//img/ancestor::*') #获取当前节点的父祖节点
# result_0 = html.xpath('//img/ancestor::body') #获取当前节点的父祖节点
# result_0 = html.xpath('//li/attribute::*') #获取当前节点的全部属性值
# result_0 = html.xpath('//table/child::*') #获取当前节点的全部子节点
# result_0 = html.xpath('//table/*') #获取当前节点的全部子节点
# result_0 = html.xpath('//table/descendant::*') #获取当前节点的全部属性值
result_0 = html.xpath('//table//*') #获取当前节点的全部属性值
print(result_0)
