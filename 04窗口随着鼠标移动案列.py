from PyQt5.Qt import *
import sys

class Window(QWidget):
    # QMouseEvent
    # def __init__(self,*args,**kwargs):
    #     super().__init__(self,*args,**kwargs)
    #     self.af=self.QMouseEvent.globalPos()
    # QMouseEvent
    # Qt.MouseButton
    def __init__(self):
        # super(Window, self).__init__()
        super().__init__()
        self.mouse_flag=False
        self.setWindowTitle('标题')
        self.resize(500, 500)
        self.setMouseTracking(True)

    def mousePressEvent(self, mou):

        if mou.button() == Qt.LeftButton:
            # print(mou)
            # print('鼠标被按下了')
            self.mouse_flag = True
            #计算窗口坐标即左上角位置
            self.windowX=self.pos().x()
            self.windowY=self.pos().y()

            #计算鼠标按下时，鼠标的全局坐标
            self.mouseX=mou.globalX()
            self.mouseY = mou.globalY()
            print(self.windowX,self.windowY,self.mouseX,self.mouseY)

    def mouseMoveEvent(self, ec):
        # pass
        if self.mouse_flag:

        # 计算移动向量
            move_X=ec.globalX()-self.mouseX
            move_Y = ec.globalY() - self.mouseY
            new_x=self.windowX+move_X
            new_y = self.windowY + move_Y
            # print(move_X,move_Y)
            self.move(new_x,new_y)


    def mouseReleaseEvent(self,Qs) :
        # print(Qs)
        if Qs.button() == Qt.LeftButton:
            print('鼠标被释放了')
            self.mouse_flag = False



if __name__=='__main__':
    app=QApplication(sys.argv)
    win=Window()

    qlb=QLabel(win)

    qlb.setText('发生LLL ')
    qlb.setStyleSheet('background-color:red;')
    # win.setMouseTracking(False)
    # qlb.setGeometry(qlb.af.x(),qlb.af.y(),100,100)
    # win.setMouseTracking(True)
    win.show()
    sys.argv(app.exec_())


