import sys
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QCheckBox
from PyQt5.QtGui import QIcon,QFont

# class Example(QWidget):
#     """创建窗口控件，
#     继承QWidget，界面的基本控件"""
#     def __init__(self):#定义对象的属性
#         super().__init__()#从超类即父类中继承对象的属性
#         self.initUI()
# 
#     def initUI(self):#定义initUI方法
#         btn1=QPushButton('按钮1',self)#在父控件self即Example下创建按钮控件，对象名称为btn1，文字为按钮1
#         btn1.move(30,50)#对btn1对象采用移动方法
#         btn2=QPushButton('按钮2', self)#在父控件self即Example下创建按钮控件，对象名称为btn2，文字为按钮2
#         btn2.setIcon(QIcon('favicon.ico'))#对对象btn2控件设置图标，QIcon是什么意思？
#         btn2.move(150, 50)  # 对btn1对象采用移动方法
#         btn1.clicked.connect(self.buttonClicked)
#         btn2.clicked.connect(self.buttonClicked)
#         self.setGeometry(300,300,390,350)#主控件的外观尺寸
#         self.setWindowTitle('按钮控件')#主控件的标题
#         self.show()#持续显示
#     def buttonClicked(self):#定义槽函数
#         print(self.sender())#返回被按下的对象
#         """网上找的的sender()函数的解释：当一个界面中有多少按钮需要输入时，我们不可能每一个按钮设计一个槽函数，
#         所以就需要我们在同一个槽函数里面对按钮进行区别，这里就需要用到sender()，sender()的返回值为触发这个事件的对象
#         ，比如我们定义0-9共10个按钮，将按钮对象名分别设置为0-9，那么当按钮按下1之后，sender()就返回1这个对象，
#         sender().text()就是对象名‘1’
#        ————————————————
#        版权声明：本文为CSDN博主「满开创」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
#        原文链接：https://blog.csdn.net/mankaichuang/article/details/105877514"""
#         print(self.sender().text()+'被按下')#打印那个按钮被按下
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex=Example()
#     sys.exit(app.exec_())
import random#使用random进行随机数字编码

class Game(QWidget):
    """定义猜拳游戏控件，继承QWidget"""
    def __init__(self):#定义Game类的属性
        super().__init__()#继承父类的属性
        self.initUI()  # 增加定义类的属性,调用类时自动运行，没有这个就不会运行initUI
    def initUI(self):#定义猜拳界面类的方法/函数
        self.result=QLabel(self)#创建result对象，作为self的一个属性（作用域比变量更广，可以在initUI函数外调用），将QLabel作为self的一个子控件/对象,赋值给result对象。
        self.result.setText('结局一片空白')#result对象设置文本，即输赢结果
        self.result.setFont(QFont('microsoft Yahei', 20))#设置文本字体
        self.result.move(80,150)#result控件移动
        btn1=QPushButton('剪刀',self)#创建剪刀控件，并实例化
        #
        btn1.move(30,50)#
        btn2=QPushButton('包子',self)
        btn2.move(150,50)
        btn3 = QPushButton('锤子',self)
        btn3.move(250, 50)
        #
        btn1.clicked.connect(self.buttonClicked)#控件按下的信号传递给槽函数
        btn2.clicked.connect(self.buttonClicked)
        btn3.clicked.connect(self.buttonClicked)
        self.setGeometry(300, 300, 390, 350)
        self.setWindowTitle('剪刀石头布')
        self.show()
    def buttonClicked(self):
        ls=['剪刀','石头','布']
        print(self.sender())#打印被按下的按钮对象
        print(self.sender().text()+'被按下')#打印被按下的按钮的文字+‘被按下’
        a = random.choice(ls)#列表随机选择文字，赋值给a

        if a=='剪刀':#函数
            if self.sender().text()=='剪刀':#如果被按下的按钮的文字为剪刀
                self.result.setText('平局')#结果控件的文字变为平局
            elif self.sender().text()=='石头':
                self.result.setText('您赢了')
            else:
                self.result.setText('电脑赢了')
        elif a=='石头':
            if self.sender().text()=='剪刀':
                self.result.setText('电脑赢了')
            elif self.sender().text()=='石头':
                self.result.setText('平局')
            else:
                self.result.setText('您赢了')
        else:#电脑出布
            if self.sender().text()=='剪刀':
                self.result.setText('您赢了')
            elif self.sender().text()=='石头':
                self.result.setText('电脑赢了')
            else:
                self.result.setText('平局')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Game()

    sys.exit(app.exec_())
