class Geese():
    neck='脖子很长'
    numb=0
    print(numb)
    # print(id(numb))
    def __init__(self):
        Geese.numb += 1#静态属性程序一加载时 就初始化 存放在栈中
        # print(id(Geese.numb))
        # print(Geese.numb)
        self.numb+=1#实例属性 需要实例化后 才加载 存放在堆中
        print(id(self.numb))
        print(self.numb)
        print('我是第{}只大雁'.format(Geese.numb),"我有以下属性：")
        print(Geese.neck)
# list1=[]
list2=[]
for i in range(4):
    Geese1=Geese()
    # list1.append(Geese.numb)
    list2.append(Geese1.numb)
# print(list1)
print(list2)
# print('一共有{}只大雁'.format(Geese.numb))
print('一共有{}只大雁'.format(Geese1.numb))