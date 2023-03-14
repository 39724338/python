##一个学校，有3个办公室，现在有8位老师等待工位的分配，编写随机分配程序
#encoding=utf-8
import random
# 定义一个列表用来保存3个办公室
offices = [[],[],[]]
# 定义一个列表用来存储8位老师的名字
names = [' 罗斯福 ',' 里根 ',' 尼克松 ',' 特朗普 ',' 拜登 ',' 奥巴马 ',' 克林顿 ',' 小布什 ']
i = 0
for name in names:
    index = random.randint(0,2)

    offices[index].append(name)
    print(offices)
i = 1
for tempNames in offices:
    print('办公室%d的人数为:%d'%(i,len(tempNames)))#%d为格式化十进制整数输出
    i+=1
    for name in tempNames:
        print("%s"%name,end='')#%s为格式化字符串str输出
        print(id(name))
        print(id(tempNames))
    print("\n")
    print("-"*20)

