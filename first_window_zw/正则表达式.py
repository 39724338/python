# '''爬取大学排名'''
#
# import requests
# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
# r = requests.get('https://www.university-list.net/rank1.htm',headers =header)
# print(r.status_code)
# print(r.text)
# print(type(r.text))
# r.encoding = r.apparent_encoding
# f = open('大学排名.html','wb')
# f.write(r.content)
# f.close()

'''导入正则库re'''
import re
'''match模块的使用
尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，
match()就返回none，如果匹配，就返回匹配成功的结果；
'''
# message = '钟南山、李兰娟、王辰、黄璐琦、张伯礼、陈薇、乔杰、仝小林'
# result = re.match('李兰娟',message)
# print(result)
# #
# result = re.search('李兰娟',message)
# print(result)   #span返回的是位置，索引号4到7(不包含)找到
# print(result.span())   #直接返回位置
# print(result.group())  #提取匹配的内容

#
'''找出字母数字字母形式的内容
    例如：d4e   e5f e1d
'''
'''正则表达式
表示范围：
[xyz]：字符集合。匹配所包含的任意一个字符。例如，“[abc]”可以匹配“plain”中的“a”。
[a-z]：字符范围。匹配指定范围内的任意字符。例如，“[a-z]”可以匹配“a”到“z”范围内的任意小写字母字符。

次数的限制：
*：匹配前面的子表达式任意次(大于等于0次）。例如，zo*能匹配“z”，也能匹配“zo”以及“zoo”。*等价于{0,}。
+：匹配前面的子表达式一次或多次(大于等于1次）。例如，“zo+”能匹配“zo”以及“zoo”，但不能匹配“z”。+等价于{1,}。
?：匹配前面的子表达式零次或一次。例如，“do(es)?”可以匹配“do”或“does”。?等价于{0,1}。
^：匹配输入行首。
$: 匹配输入行尾。
{n}：n是一个非负整数。匹配确定的n次。例如，“o{2}”不能匹配“Bob”中的“o”，但是能匹配“food”中的两个o。
{n,}：n是一个非负整数。至少匹配n次。例如，“o{2,}”不能匹配“Bob”中的“o”，但能匹配“foooood”中的所有o。“o{1,}”等价于“o+”。“o{0,}”则等价于“o*”。
{n,m}：m和n均为非负整数，其中n<=m。最少匹配n次且最多匹配m次。例如，“o{1,3}”将匹配“fooooood”中的前三个o为一组，后三个o为一组。“o{0,1}”等价于“o?”。请注意在逗号和两个数之间不能有空格。

\d:匹配一个数字字符。等价于[0-9]。
\D:匹配一个非数字字符。等价于[^0-9]。^在方括号中属于非，不是匹配输入字行首
\s:匹配任何不可见字符，包括空格、制表符、换页符等等。等价于[ \f\n\r\t\v]。
\S:匹配任何可见字符。等价于[^ \f\n\r\t\v]。  
\w:匹配包括下划线的任何单词字符。类似于“[A-Za-z0-9_]”，这里的"单词"字符使用Unicode字符集。
\W:匹配任何非单词字符。等价于“[^A-Za-z0-9_]”。
\b:匹配一个单词的边界，也就是指单词和空格间的位置
\B:匹配非单词边界。“er\B”能匹配“verb”中的“er”，但不能匹配“never”中的“er”。
\f：匹配一个换页符。
\n：配一个换行符。
\r：匹配一个回车符。
\t：匹配一个制表符。
\v：匹配一个垂直制表符。
. :匹配除“\n”和"\r"之外的任何单个字符。

|  :将两个匹配条件进行逻辑“或”（or）运算。   
( ):将(和) 之间的表达式定义为“组”（group），并且将匹配这个表达式的字符保存到一个临时区域（一个正则表达式中最多可以保存9个）。

'''
# message  = '11ndinwd1oinwqdoqje9dqedc' #从提取出abcde里面任意一个字母
# result = re.search('[abcde]',message)  #看到参数是pattern 模式：构成过滤的模式
# print(result)
#
# result = re.search('[a-z][a-d]',message)
# print(result)
# result = re.search('[a-z][0-9]',message)#寻找到第一个就会返回，不再继续寻找
# print(result)
# result = re.findall('[a-z][0-9][a-z]',message)
# print(result)
'''dir(re)查看re库的所有函数'''

'''找出字母 至少一个数字 字母；例如 a7d  e77y d777t d7777b数据'''
# message = 'da2a7ddbre77yifed777t3fefd7777b'
# result = re.findall('[a-z]*[0-9][a-z]',message)
# print(result)
'''验证手机号码正确性 例如：138********，1开头，11位数字'''
# phone_num = input("请输入您的手机号码：")
# result = re.match('1[0-9]{10}$',phone_num)  #match从头开始
# print(result)
# result = re.findall('^1[0-9]{10}$',phone_num)  #加入^  $
# print(result)

'''验证qq号码:从5位到11位，开头不能位0'''
# QQ_number = input("请输入您的QQ号：")
# result = re.findall('^[1-9][0-9]{4,10}$',QQ_number)
# print(result)

'''验证用户名，字母(大小写)数字下划线组成，但数字不能开头，长度大于8'''
# use_name = input("请输入您的用户名：")
# result = re.findall('^[A-Za-z_][A-Za-z0-9_]{7,}$',use_name)   #^[A-Za-z_][A-Za-z_0-9]{7,}$
# print(result)
# result = re.findall('^[A-Za-z_]\w{7,}$',use_name)
# print(result)

# message = 'verb very never every'
# result = re.findall(r'\w+er\B',message)  #\b是转义字符
# print(result)
# #
# result = re.findall('.e',message)
# print(result)   #
# result = re.findall('\w+ev|\w+ry',message)
# print(result)

# message = '''<div class="c-span4  opr-recommends-merge-item "
#         data-click="{'rsv_re_ename:'百度知道','rsv_re_uri':'44dde326b21644c9a865d960fc6aa46d'}">
#         <div class="opr-recommends-merge-p">'''
# result =re.findall('^<div class=".+"',message)#匹配class的内容，div class=".+"
# print(result)
# result = re.findall(r"rsv_re_ename:.+,",message)#匹配'rsv_re_ename':'百度知道',
# print(result)
#匹配rsv_re_ename和rsv_re_uri
# result = re.findall("'rsv_re_ename:'(.+)','rsv_re_uri':'(.+)'",message)
# print(result)

# message ='<t1>首页</t1>'   #引用匹配,必须和前面匹配的内容一模一样
# result = re.findall(r'^<(\w+)>(.+)</\1>$',message)#r'^<(\w+)>(.+)</\1>$'
# print(result)              # 首页   首页      t1
#
# message ='<dt><a>首页</a></dt>'
# result = re.findall(r'^<(\w+)><(\w+)>(.+)</\2></\1>$',message)#
# print(result[0][2])
#
# '''当匹配的内容非常多，可以给子表达式起名字?P<name>'''
# result  = re.findall(r'^<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>$',message)
# print(result)


'''贪婪与非贪婪
贪婪模式：默认匹配模式为贪婪模式，尝试匹配尽可能多的字符；
非贪婪模式：总是尝试匹配尽可能少的字符。
在次数限制操作符 后面加上？转换为非贪婪模式
'''
# message = 'ccc739134792hd'
# result = re.findall('ccc\d+?',message)
# print(result)

'''修饰符
修饰符                 描述
re.I        使匹配对大小写不敏感
re.L        做本地化识别匹配
re.M       多行匹配，影响^和$
re.S        使.匹配包括换行在内的所有字符
re.U        根据Unicode 字符集解析字符。这个标志影响\w,\W,\b和\B
re.X        该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解
'''
# message = '''<dt><a>首页
#             内容都在这里</a></dt>'''
# result = re.findall(r'^<(\w+)><(\w+)>(.+)</\2></\1>$',message,re.S)#
# print(result)
#
#
#
#
'''sub:除了使用正则表达式提取信息外，有时候还需要借助它来修改文本 。'''
content ='dh932hf9f934hfnf39d'  #   O
content = re.sub('\d','O',content)
print(content)


'''compile:将正则字符串编译成正则表达式对象，以便在后面的匹配中复用'''
# 分别将 3 个日期中的时间去掉
contentl ='2020 12 15 12:00'
content2 ='2020-12-17 12:55'
content3 ='2020-12-22 13:21'
pattern = re.compile('\d{2}:\d{2}')
resultl = re.sub(pattern,'', contentl)
result2 = re.sub(pattern,'',content2)
result3 = re.sub(pattern,'',content3)
print(resultl, result2, result3)

'''项目-----抓取疫情数据，并制作成app'''
# import requests,re,sys,time
# from PyQt5.QtWidgets import (QWidget, QProgressBar,QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer

# url = 'http://www.5ppt.net/aricle.asp?id=3947&p='
# for i in range(1,5):
#     url_new = url + str(i)  #字符串的连接
#     r = requests.get(url_new)
#     if r.status_code == 200:
#         r.encoding = r.apparent_encoding
#         result = re.findall('([\u4e00-\u9fa5]+)：(\d+)例',r.text)
#         print(result)





# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.epidemic()
#         self.initUI()
#
#     def initUI(self):
#         self.pbar = []
#         for i in range(len(self.infos)):
#             self.pbar.append(QProgressBar(self))
#             self.pbar[i].setGeometry(100, 80+40*i, 200, 25)
#             self.pbar[i].setValue(0)
#
#         self.btn = QPushButton('显示数据', self)
#         self.btn.move(120, 20)
#         self.btn.clicked.connect(self.doAction)
#         self.setGeometry(600, 100, 380, 800)
#         self.setWindowTitle('进度条')
#         self.show()
#
#     def epidemic(self):
#         url = 'http://www.5ppt.net/aricle.asp?id=3947&p='
#         self.infos = []
#         for i in range(1, 5):
#             url_new = url + str(i)
#             r = requests.get(url_new)
#             if r.status_code == 200:
#                 r.encoding = r.apparent_encoding
#                 result = re.findall('([\u4e00-\u9fa5]+)：(\d+)例', r.text)
#                 if result != []:
#                     for one_info in result:
#                         self.infos.append(one_info)
#         print(self.infos)
#
#     def doAction(self):
#         self.btn.setText('整理中...')
#         for i in range(len(self.infos)):
#             time.sleep(0.3)
#             self.pbar[i].setValue(int(self.infos[i][1])/1000)
#         self.btn.setText('显示完成')
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


