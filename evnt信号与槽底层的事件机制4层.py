from PyQt5.Qt import *
import sys
#

class Btn(QPushButton):
    def event(self,evt):#重新定义控件事件
        if evt.type()==QEvent.MouseButtonPress:
            print(evt,'第2层事件-控件event事件')
        return super().event(evt)#将所有事件、接受者继续传递，如没有该行，就不继续向下传递

    def mousePressEvent(self, *args,**kwargs):
        print('鼠标被点击了...','第3层事件-控件动作event事件')
        return super().mousePressEvent(*args,**kwargs)

class Windows(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400,400)
        self.setWindowTitle('fsda')
        self.initUI()
        self.dianji()


    def initUI(self):
        self.btn1=Btn(self)
        self.btn1.setText('按钮')
        self.btn1.move(150,100)
        # print(id(self.btn1))

    def cao(self):
            print('按钮被点击了','第4层事件-信号与槽表层事件')

    def dianji(self):
        self.btn1.pressed.connect(self.cao)
class App(QApplication):
    # QEvent
    def notify(self,obj,evt):
        if obj.inherits('QPushButton') and evt.type()==QEvent.MouseButtonPress:
            print(obj,evt,'第一层事件-notify事件')
        return super().notify(obj,evt)

if __name__ == '__main__':
    app=App(sys.argv)
    win=Windows()
    win.show()
    sys.exit(app.exec_())