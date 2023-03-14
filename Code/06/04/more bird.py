class Geese:
   neck = "脖子较长" # 类属性（脖子）
   wing = "振翅频率高" # 类属性（翅膀）
   leg = "腿位于身体的中心支点，行走自如" # 类属性（腿）
   number = 0 # 编号
   def __init__(self): # 构造方法
       Geese.number += 1 # 将编号加1
       print("\n我是第"+str(Geese.number)+"只大雁，我属于雁类！我有以下特征：")
       print(Geese.neck) # 输出脖子的特征
       print(Geese.wing) # 输出翅膀的特征
       print(Geese.leg) # 输出腿的特征
# 创建4个雁类的对象（相当于有4只大雁)
list1 = []
for i in range(4): # 循环4次
      list1.append(Geese()) # 创建一个雁类的实例
print("一共有"+str(Geese.number)+"只大雁")
