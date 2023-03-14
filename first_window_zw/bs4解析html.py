import requests,bs4

# r = requests.get('https://news.china.com/socialgd/10000169/20200427/38145978.html')
# print(r.status_code)
# r.encoding = r.apparent_encoding
# print(r.text)

# rel_soup = bs4.BeautifulSoup(r.text,'html5lib')#可以是自带的'html.parser'或lxml或和html5lib
#如果打开一个已经下载好的文件使用方法为：
rel_soup = bs4.BeautifulSoup(open("解析html.html",encoding='utf-8'),'html5lib')
# print('1',rel_soup.a)                #通过点取属性的方式只能获得当前名字的第一个tag
# print('2',rel_soup.a['href'])       # tag的属性的操作方法与字典相同
# print('3',rel_soup.a['target'])
# print('标签内容：',rel_soup.a.string)
# print('标签内容：',rel_soup.a.contents)
# print('标签内容：',rel_soup.div.contents)
# print('标签内容：',rel_soup.div.string)#如果tag(标签)包含了多个子节点,tag就无法确定 .string 方法应该调用哪个子节点的内容, .string 的输出结果是 None

'''一个Tag可能包含多个字符串或其它的Tag,这些都是这个Tag的子节点.'''
# print('获取子标签：',rel_soup.div.h3)
# print('获取子标签的内容：',rel_soup.div.h3.contents)


'''获取对应名称的全部标签'''
# print('获取全部h3标签:',rel_soup.find_all('h3'))   #返回内容为列表形式
# print('获取div标签中全部的h3标签:',rel_soup.div.find_all('h3'))

'''通过tag的.children 生成器,可以对tag的子节点进行循环'''
# for child in rel_soup.div.children:
#     print('children生成器：',child)
# for child in rel_soup.div:
#     print('无生成器：',child)

# print(rel_soup.prettify()) #把要解析的内容以标准的缩进格式输出

'''选择指定标签时，有时候不能做到一步就选到想要的节点元素，需要先
选中某一个节点元素，然后以它为基准再选择它的子节点、父节点、 兄弟节点等，'''
'''获取某个节点元素的父节点，可以调用 parent 属性'''
# print('p标签的父节点：',rel_soup.p.parent)
'''获取某个节点元素的父辈节点，可以调用 parents 属性，返回结果是生成器类型'''
# print('p标签的祖先节点：',rel_soup.p.parents)
# print('th标签的祖先节点：',rel_soup.th.parents)
# num=0
# for i in rel_soup.th.parents:
#     num += 1;
#     print('第',num,'次：\n',i,'\n\n\n\n')

'''获取同级的节点（也就是兄弟节点），如果没有兄弟节点则返回None'''
# print('a节点的下一个兄弟节点：',rel_soup.a.next_sibling)
# print('a节点的上一个兄弟节点：',rel_soup.a.previous_sibling)


'''通过当前节点获取的兄弟节点们，并迭代输出'''
# for i in rel_soup.a.next_siblings:
#     print('后面的兄弟节点们：',i)
# for i in rel_soup.a.previous_siblings:
#     print('前面的兄弟节点们：',i)

'''find_all函数---多种使用方法
    查找结合正则表达式re库'''
import re
# for tag in rel_soup.find_all(re.compile('t')):
#     print('标签名中有t的标签：',tag)

'''表格中的t标签'''
# for tag in rel_soup.find_all(re.compile('^t\w$')):
#     print('表格中的t标签：',tag)

'''搜索多个标签，如果传入列表参数,Beautiful Soup会将与列表中
    任一元素匹配的内容返回.'''
# print(rel_soup.find_all(['a','h3','p']))

'''按照标签属性搜索'''
# print(rel_soup.find_all(src=re.compile('31424e')))#搜索属性src的值有31424e的标签
# print(rel_soup.find_all(rel="icon"))#搜索属性rel的值为icon的标签
# print(rel_soup.find_all(rel=True))#搜索带有rel属性的标签

'''如果文档树很大那么搜索会很慢.如果我们不需要全部结果,
可以使用 limit 参数限制返回结果的数量.'''
# print(rel_soup.find_all('th',limit =1))


'''find直接返回结果.相当于对find_all设置了limit =1的返回结果'''
# print(rel_soup.find(rel=True))
# print(rel_soup.find('th'))
# print(rel_soup.find_all('th',limit =1))


'''Beautiful Soup的强项是文档树的搜索,但同时也可以方便的修改文档树
    注：只是修改文档树，并不是直接修改html文件内容'''
# print(rel_soup.td.string)
# rel_soup.td.string = '修改内容'
# print(rel_soup.td.string)

'''Tag.append() 方法向tag中添加内容,就好像Python的列表的 .append() 方法:'''
# rel_soup.td.append('新内容')
# print(rel_soup.td)

'''增加一个子标签'''
# rel_soup.td.append('<span>nihao</span>')#不能直接添加
# print(rel_soup.td)

new_tag = rel_soup.new_tag("a", href="https://www.hao123.com/")
rel_soup.td.append(new_tag)
print(rel_soup.td)

# new_tag.string = 'hao123网站'
# print(rel_soup.td)

'''移除当前tag的内容'''
# rel_soup.td.a.clear()
# print(rel_soup.td)

'''decompose() 方法将当前节点移除文档树并完全销毁:'''
# rel_soup.td.a.decompose()
# print(rel_soup.td)

'''输出'''
'''prettify()方法将Beautiful Soup的文档树格式化后以Unicode编码输出,
    每个XML/HTML标签都独占一行'''
# print(rel_soup.prettify())


'''更多细节的内容看官方文档'''
'''https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/'''
