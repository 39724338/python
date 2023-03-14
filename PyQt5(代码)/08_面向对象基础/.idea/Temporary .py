##需求分析
##一个叫王敏的人，有一条狗。
##这条狗叫旺财，能叫能跑。

##狗类

##属性：名称
##动作：能叫
###调用枪类

##定义人类
###属性：名称
###动作：能和狗玩耍，狗能叫能跑。

class Dog(object):
    def __init__(self,name):
        self.name=name

    def paojiao(self):
        print('%s跑和叫'%self.name)

class Person(object):
    def __init__(self,name):
        self.name=name
    def game_withdog(self,dog):
        print('%s和%s 一起玩'%(self.name,dog.name))
        dog.paojiao()
wc=Dog('旺财')
xm =Person(
    '小明'
)
xm.game_withdog(wc)









