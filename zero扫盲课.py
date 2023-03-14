##字符串、列表输出
# string='失望之酒，希望之杯.'
# list121=['沙发垫','222','host','健康']
# print(string[-1])
# print(string[1:5:2])
# print(list121[0:3:2])
#
# #序列相加，只允许同类型相加
# list121=['沙发垫','222','host','健康']
# list122=['看后感','222','噶','几个号']
# list123=list122+list121
# print(list123)
# string1='失望之酒，希望之杯.'
# string2='还是法国，火锅店.'
# string3=string2+string1
# print(string3)
# tuple11=('合格，好过分的话.','干豆腐')
# tuple12=('火狐','成功之母')
# tuple13=tuple11+tuple12
# print(tuple13)
#
# #初始化序列，包含多个元素,不能用于元组
# emptylist=[None]*5
# print(emptylist)
#
# #判断元素是否属于序列
# nba=['乔丹','科比']
# print('科比'in nba)
#
# #计算序列长度，最大值，最小值,和，排序，翻转
# numb1=[234,24,63]
# print(len(numb1))
# print(max(numb1))
# print(sum(numb1))
# print(sorted(numb1))



##列表的创建方式3种
# listname=[2,3,4]  #第一种
# a12=list(range(2,21,2)) #第二种
# print(a12)
# string3="明日科技"  #第三种
# ad1=list(string3)
# print(ad1)

# #删除列表
# del ad1

##访问列表的三种方式：使用print、索引、切片
##输出列表的方式：使用for循环、使用enumerate()枚举、列举函数
# lst = [1,2,3,4,5,6]
# for index,value in enumerate(lst,10):#10代表索引开始值
#     print("%s,%s"%(index,value))#%s中%是占位符，s是字符串

##列表添加,修改，删除某个元素
# listname=[1,2,3,4]
# listname1=[1,2,3,4]
# listname.append(5)
# listname.insert(0,6)
# listname[1]=10
# del listname[-2]
# listname.remove(3)
# listname.extend(listname1)
# print(listname)

##对列表进行统计计算
# listname11=['云在飞','forf','云在飞',4]
# count1=listname11.count('云在飞') #统计出现的次数
# print(count1)
# print(listname11.index('forf'))#统计第一次出现的索引

##对列表进行排序：1、列表对象的sort()方法。2、内置的sorted函数
# grade1=['Cat','dog''horse']
# grade1.sort(key=str.lower)#不区分大小写进行降序（非默认)排序,改变原列表顺序
# grade2=sorted(grade1,reverse=True)#不区分大小写进行降序（非默认)排序，不改变原列表顺序

##列表推导式
##使用推导式前的语句
# import random
# listd1=[]
# for i in range(10):
#     listd1.append(random.randint(10,100))
#     print(listd1)
##使用推导式后的语句
# import random
# listd1=[random.randint(10,100) for i in range(10)]
# print(listd1)
# listd2=[i*i for i in range(1,50,2) if i*i<1000]
# print(listd2)

##二维列表，如room[行索引][列索引]，两种创建方式
# room1=[[None]*5,[None]*5,[None]*5]#创建二维列表
# room2=[]
# for i in range(1,5):
#     room2.append([])#加行
#     for j in range(1,7):
#         room2[i-1].append(i*100+10+j)#嵌套加列
# print(room1,room2)
# room3=[[i*100+10+j for j in range(1,7)]for i in range(1,5)]
# print(room3)

##元组创建,与列表相同
# tuplename1=(3,4,5,6)
# tuplename2=()
# tuplename3=tuple(range(2,21,2))
# print(tuplename3)

##访问元组元素，同列表：print,索引，切片，for循环遍历
##修改元组，只能重新全部定义，才能修改。不能修改单个元素
##两个元组可以连接形成一个新元组，使用加号。
##元组推导式同列表推导式一样，只是将[]换成()，还需要使用tuple函数转换。
##元组的访问速度比列表快
##元组可以作为字典的键，而列表不可以

##字典的创建:1、直接定义。2、zip函数转换。3、元组加列表组合、4、创建空字典。5、使用dict()函数创建
## cag= {'che':'车','chen':'尘'}#方法1：直接定义
# key=['che','chen','cheng','chi'] #方法2：zip函数，注意是将列表转换
# value=['车','尘','称','吃']
# zip1=zip(key,value)
# print(dict(zip1))
# key1=('che','chen','cheng','chi') #方法3：元组加列表组合
# value1=['车','尘','称','吃']
# dict11={key1:value1}
# print(dict(dict11))
# cag= dict('che'='车','chen'='尘')#利用dict函数创建
# dict2=dict.fromkeys(key)#利用dict对象的fromkeys创建

# #访问字典内容

##通过对应的键访问字典的值（相当于列表的索引）
# print(zip['che'] if '车' in zip else '没有此人')

##利用get函数访问键，输出值
# print(zip.get('che','没有此人'))

##遍历字典
# sign= {'che':'车','chen':'尘'}
# for item in sign.items():
#     print(item)
# for key,value in sign.items():
#     print(key,'的值是',value)
# for key in sign.keys():
#     print(key)

##字典添加，与list类似
# dict[key]=value

##字典推导式，与list类似
# import random
# randomdict={i:random.randint(10,20) for i in range(5)}
# print(randomdict)

##集合的创建，与list类似，集合是可变序列
# set1={'水瓶座','射手座','双鱼座'}#集合是无序的，去重的
# set2=set()#字典定义空字典使用{}，为便于区分，集合定义空集合使用函数
# list22=['车','尘','称','吃']
# set3=set(list22)#将列表转换为集合

##向集合中添加元素
# set4={'车','尘','称','吃'}
# set4.add('好')

##集合中删除元素
# set4.remove('尘')#删除制定元素
# set4.pop()#任意删除元素，并将删除的元素返回
# set4.clear()#清空集合

##集合的交集&、并集|、差集-、对称差集^

##encode()编码 decode()解码方法进行字符转换
##字符串str包括ASCII码(包括数字、大小写及特殊符号)共256个
##字符串strGBK/GB2312中文编码1字节表示英文两个字节表示中文、
# #字符串str还包括UTF8国际通用编码，3个字节中文。python默认
##python中采用两种字符 str和bytes，str用unicode字符，
##unicode字符表示多个字节，即字符串：'拼搏到感动自己‘
##bytes字符表示b前缀的二进制字符串：b'\xd2\xb0\'和b’mr‘
##unicode字符不能与bytes拼接一起使用，
##网络传输或保存到磁盘时需要将unicode转换为bytes，内存使用unicode

###语法格式如下
# str.encode([encodings='utf-8'][,errors='strict'])
# str1='野渡无人舟自横'
# newstr=str1.encode('utf-8')
# print(newstr)
# oldstr=newstr.decode('utf-8')
# print(oldstr)
##结果：b'\xe9\x87\x8e\xe6\xb8\xa1\xe6\x97\xa0\xe4\xba\xba\xe8\x88\x9f\xe8\x87\xaa\xe6\xa8\xaa'
##野渡无人舟自横

##分割字符listname=str.split(sep,maxsplit)
# list10='你 有 多 自行，\n世界就多相信你'
# list11=list10.split(' ',5) #以空格为分隔符，分割5次
# print(list11)
##结果：['你', '有', '多', '自行，\n世界就多相信你']

##合并字符串使用join（）方法
# list01=['明日科技','扎克伯格','勤奋的天使']
# str01='@'.join(list01)##将各元素用@连接起来
# print(str01)
##结果：明日科技@扎克伯格@勤奋的天使

##检索在字符串中出现的次数
##str.count（sub[,start[,end])#start.end表示索引
##检索是否包含制定字符串，返回0或-1。比“发” in str1多始末位置。
##str.find（sub[,start[,end])#start.end表示索引
# print(str1.rfind('自'))#返回索引
###str.index（sub[,start[,end])返回第一次出现的索引
###str.rindex（sub[,start[,end])返回最后一次出现的索引
##str.startswith(prefix[,start[,end]])返回是否以制定字符开始。
##str.endswith(prefix[,start[,end]])返回是否以制定字符结束

##大小写转换
##str.lower()  str.up()

##去除空格和特殊字符
##str.strip()去除左右两端的空格、换行和回车符
##str.strip('*')去除左右两端的*
##str.lstrip('*')去除左端的*

## 格式化字符串如1800变为1800.00
##早期版本使用%，python3.0使用format方法
##%格式化字符语法：'%[-][+][0][m][.n]格式化字符'%exp（exp为要转换项

##正则表达式是匹配字符串的规则
##行定位符：用来定位行的开始和结束，^表示开始，$表示结束
##'Hi python Hi明日科技'  '^Hi'匹配前面的'Hi'，'科技$'匹配'科技'
##元字符：具有特殊意义的专用字符，如'^','\d'匹配数字
##限定符：用来限定匹配数量，如？为匹配前面的字符零次或1次。*为0次或多次
##字符类：定义一个用来匹配的字符集合，用[],如[\u4e00-\u9fa5]表示匹配任意汉字
##排查字符：排除不符合的字符串，用[]里面的^，如[^a-zA-Z]匹配一个不是字母的 字符
##选择字符：与或意义相同，用|表示。[a-z]|[0-9]表示匹配a-z或者0-9的字符
##转义字符：用\表示，把特殊字符转换为普通字符
##分组：用()表示. (\.[0-9]{1,3}){3}表示（）里的分组，进行重复3次匹配
##模式字符串：用1对单引号括起来
##原生字符串，在单引号前加r，如r'\bm\w'，就可以不对\转义

##用re模块实现正则表达式操作
##匹配即查找字符，用match(),search(),findall()方法
##re.match(pattern,string,[flags])，返回match对象,不存在返回None
##pattern为模式字符串，string为要匹配的字符串，
##flags为标志位即匹配方式，如re.I为不区分大小写，re.Arang\w不匹配汉字
##{}一般用来表示匹配的长度
##[0-9]{0,9} 表示长度为 0 到 9 的数字字符串
# import re
# pattern=r'mr1\w'#\w为元字符
# string='MR1SHOP mr1_shop'
# match=re.match(pattern,string,re.I)
# print(match)
# print('起始位置：',match.start())
# print('结束位置：',match.end())
# print('匹配数据:',match.group())#找的匹配的数据
##结果：<_sre.SRE_Match object; span=(0, 4), match='MR1S'>
##起始位置： 0
##结束位置： 4
##匹配数据: MR1S


# import re
# pattern=r'(13[4-9])\d{8}|(15[01289]\d{8})$'
# mobile='13634226989'
# match=re.match(pattern,mobile)
# if match==None:
#     print(mobile,'不是中国移动号码')
# else:
#     print(mobile,'是中国移动号码')
##结果：13634226989 是中国移动号码

####re.search(pattern,string,[flags])，返回search对象,不存在返回None
###match()和search()都只匹配一个结果，但是match()是从字符串的开头开始匹配的，
# #如果匹配的字符不是在开头处，那么它将会报错，匹配成功返回结果，没有返回None。
# #而search()是从头开始匹配，匹配整一个字符串得出结果, 如有多个则是第1个
# import re
# pattern=r'mr1\w'#\w为元字符
# string='MR1SHOP mr1_shop'
# search=re.search(pattern,string,re.I)
# print(search)
# print('起始位置：',search.start())
# print('结束位置：',search.end())
# print('匹配数据:',search.group())#找的匹配的数据
##结果：<_sre.SRE_Match object; span=(0, 4), match='MR1S'>
##起始位置： 0
##结束位置： 4
##匹配数据: MR1S


###findall（）：匹配所有包含匹配字符串，返回结果列表
##re.findall(pattern,string,[flags])，返回结果列表,不存在返回None
# import re
# pattern=r'mr1\w'#\w为元字符
# string='MR1SHOP mr1_shop'
# findall=re.findall(pattern,string,re.I)
# print(findall)
# ##结果：['MR1S', 'mr1_']

##替换字符串
##re.sub(pattern,repl,string,count,flags)#pattern为模式字符串
# import re
# pattern1=r'1[345678]\d{9}'
# string='中奖号码：84659789 联系电话：13564697896'
# result=re.sub(pattern1,'1*********',string)
# print(result)
##结果：中奖号码：84659789 联系电话：1*********

##使用正则表达式分割字符串
##re.split(pattern,string,[maxsplit],[flags])
##pattern为模式字符串，string为要匹配的字符串，maxsplit为最大拆分次数
# import re
# pattern=r'[?|&]'#分割符，模式字符串
# url="http://www.mingrisoft.com/login.jsp?username='mr'&pwd='mrsoft'"
# result=re.split(pattern,url)
# print(result)
##结果：['http://www.mingrisoft.com/login.jsp', "username='mr'", "pwd='mrsoft'"]

##函数的帮助文档可以用：函数名.__doc__或help(函数名）并结合print查看
##形式参数的值传递：针对不可变对象，不改变形式参数的值。
# #形式参数的引用传递：针对可变对象，改变形式参数的值
# def demo(obj):
#     print(obj)
#     obj+=obj
# str='奔跑吧'
# demo(str)#结果：奔跑吧
# demo(str)#值传递，结果还是：奔跑吧
# list=['网络','科目']
# demo(list)#结果：['网络', '科目']
# demo(list)#引用传递，结果：['网络', '科目', '网络', '科目'

##python中可变对象有：列表、字典、集合
##不可变对象有：元组、字符串、数值
##可以访问https://www.jb51.net/article/223840.htm
##https://www.jb51.net/article/223842.htm
##列表中存储的并不是我们看到的元素的值，而是这些元素的地址
##元组是不可变的！！！ 一旦改变了，就不再是这个元组了，而是一个新的元组
##所以要对元组执行操作，都是先产生一个新元组，再在新元组上执行相应操作
##字典与列表类似
##列表中出现了可变类型的元素，我们想对列表进行一个安全的复制，
# #\n那么就不能浅拷贝，而是需要深拷贝使得能够独立操作而不影响原列表copy.deepcopy()
# ab = {'a':1, 'b':2}
# list1 = []
# a=ab.get('a')
# print(id(a))##1853386208
# for i in range(2,5):
#     ab['a'] = i
#     list1.append(ab)
# print(list1)     # [{'a': 4, 'b': 2}, {'a': 4, 'b': 2}, {'a': 4, 'b': 2}]
# print(id(a))##1853386208
##这段代码本以为结果应该是[{‘a': 2, ‘b': 2}, {‘a': 3, ‘b': 2}, {‘a': 4, ‘b': 2}]
##但是列表中的每一个字典里键a的值都变成了最后一次的值4



##注意下述情况
# list=[1,2,3,4]
# def solution(list):
#     list=[1,2,3,4,5]
#     return list
# solution(list)
# print(list)#结果：[1,2,3,4]
##在函数内部用了"=" ，其实就相当于重新创建了一块内存存放
# #新的对象，将list指向了新的对象，所以并没有改变全局中的list

# list=[1,2,3,4]
# def solution(list):
#     list.append(5)
#     return list
# solution(list)
# print(list)#结果：[1,2,3,4,5]
##使用append，即改变原对象的值，因此还是对原对象的操作

##函数中定义可变参数：*parameter、**parameter，分别采用1/2个*
## *parameter：表示可以接受任意多个参数，放到元组中,是按位置传递
# def coffee(*coffeename):##*parameter：表示可以接受任意多个参数，放到元组中,是按位置传递
#     print('\n我喜欢的咖啡有：')
#     for item in coffeename:
#         print(item)
# coffee('蓝山')
# coffee('巴西','卡布奇诺','蓝山')
# list1=['巴西','卡布奇诺','蓝山']
# coffee(*list1)

## **parameter：表示可以接受任意多个参数，放到字典中,是按关键字传递
# def sign(**sign):
#     for key,value in sign.items():
#         print(key,'的星座是：',value)
# sign(绮梦='水瓶座',冷依='射手座')
# sign(香凝='水双鱼座',冷依='巨蟹座')
# dict1={'香凝':'双鱼座','冷依':'巨蟹座'}
# sign(**dict1)

##函数返回值如有多个，如将函数赋值给变量，则该变量为元组。

##匿名函数：如只使用次数小，可用匿名函数，简洁，免得费劲去起名，使用lambda表达式实现。
##基本语法为：result=lambda [arg1[,arg2,..argn]]:expression
##表达式expression中不能出现for或while等非表达式语句
# import math
# def circlearea(r):
#     return  math.pi*r*r
# r=10
# print('半径为',r,'的圆面积为：',circlearea(r))
# ##上述函数可改为
# r=10
# result=lambda r:math.pi*r*r
# print(result(r))

##类的公有属性
# class Swan:
#     '''天鹅类 '''
#     neck_swan='天鹅的脖子很长'#公有类型的属性
#     def __init__(self):
#         print('__init__:',Swan.neck_swan)#在实例方法中访问
# swan=Swan()
# print('通过实例名访问：',swan.neck_swan)

##类的私有方法、属性，访问限制：在定义方法或属性时，加__或两边都加__，不能访问也不能读取
##在方法、属性XX前加__，可以用实例名._类名.__XX进行访问,即多加_类名.
##在方法、属性前后加__，是系统属性

##property属性，不同于类属性和实例属性。
##类属性和实例属性返回所存储的值，而property访问计算后的值
##创建用于计算的属性，称为装饰器，语法：@property
# class Rect:
#     def __init__(self,width,heigth):
#         self.width=width
#         self.height=heigth
#     @property
#     def area(self):
#         return self.width*self.height
# rect=Rect(800,900)
# print('面积为：',rect.area)

##为属性加保护机制，可以读取但不能修改值，即通过装饰圈获取私有属性
# class TVShow:
#     def __init__(self,show):
#         self.__show=show
#     @property
#     def show(self ):
#         return self.__show#返回私有属性
# tvshow=TVShow('正在播放战狼2')#创建类的实例
# print('默认：',tvshow.show)##show为只读属性，不能修改，即不能重新赋值。

##https://blog.csdn.net/zhh763984017/article/details/120072425
##闭包：函数中再嵌套一个函数，并且引用外部函数的变量
# def demo(x):
#     def de(y):
#        return x+y
#     return de
# print(demo(5)(6))

##一个有意思的程序
# def baiyu():
#     print("我是攻城狮白")
# def blog(name):
#     print('进入blog函数')
#     name()
#     print('我的博客是 https://blog.csdn.net/zhh763984017')
# if __name__ == '__main__':
#     func = baiyu  # 这里是把baiyu这个函数名赋值给变量func
#     print(type(baiyu),id(baiyu))#<class 'function'> 1909998431768
#     print(type(func),id(func))#<class 'function'> 1909998431768
#     func()  # 执行func函数  #结果：我是攻城狮白
#     print('------------')
#     blog(baiyu)#把baiyu这个函数作为参数传递给blog

##类的继承
# class Fruit():
#     fruit='绿色的'
#     def harvest(self):
#         print('水果已经收获')
#         print('水果的颜色是'+self.fruit)
# class Apple(Fruit):
#     apple='红色的'
#     def __init__(self):
#         print('我是苹果')
# apple=Apple()#我是苹果
# apple.harvest()#水果已经收获#水果的颜色是绿色的


##文件的打开
# file=open('ff.txt','w')
# list1=['fsa','是','234','沙发沙发']
# file.writelines('@'+i+' ' for i in list1)
# file.close()
##读取字符read([size])，打开文件只能是R或R+
# with open('ff.txt','r') as ff1:
#     ff1.seek(3)#指针移动几个字符，对于汉字，如是UTF-8则暂用个字节
#     # string=ff1.read(6)#读取前6个字符（汉字1个字节）
#     string=ff1.readline()#读取行
#     string = ff1.readlines()  # 读取全部行
#     print(string)

##OS模块：与python内置的操作系统和文件系统相关的模块，是标准模块。
##OS模块中的语句执行结果与操作系统相关。
##os.path模块
# import os
# print(os.getcwd())



