import json,sys
from shutil import copyfile

from logging import *
from PyQt5.QtWidgets import QHBoxLayout, QWidget,QApplication,QMessageBox,QTreeWidget

# from Log.logg import logger#logg
# from tests.statementanalysis111.HedgeRecord1111 import HedgeTreeWidget#HedgeTreeWidget


class StatementAnalysisMgr(QWidget):
    def __init__(self):
        super(StatementAnalysisMgr, self).__init__()
        self.Recvmsg = "StatementAnalysisMgr"
        # setCB(self.Recvmsg, self.recvmsgSign)
        self.initUi()
        self.resetOrInit()

    def initUi(self):
        self.mainWidget = QTreeWidget()#HedgeTreeWidget
        self.setLayout(QHBoxLayout())#
        self.layout().addWidget(self.mainWidget)
        self.setGeometry(300, 300, 1000, 800)
        self.setWindowTitle('HedgeTreeWidget')
        self.show()
        self.getData()

    def getData(self):
        data = json.loads(sys.argv[1])
        self.data = data
        self.mainWidget.setData(data)

    def recvmsgSign(self, msg):

        hbox = QHBoxLayout()
        hbox.addWidget(self.mainWidget)
        self.setLayout(hbox)

        # 服务
        self.mainWidget.resetClicked.connect(self.resetOrInit)
        self.mainWidget.queryClicked.connect(self.query)
        self.mainWidget.orderClicked.connect(self.order)
        self.mainWidget.pageBtnClicked.connect(self.exchangePage)
        self.mainWidget.clicked.connect(self.treeMenuClicked)

    def handleMSG(self, code, msg):
        '''回调'''
        try:
            self.dict = eval(msg)
            if self.dict['head']['cmd'] == "listtradeorder":
                combox_list = []
                if len(self.dict['body']) > 0:
                    table_msg = self.dict['body'][0]['mainorderlist']
                    if len(table_msg) > 0:
                        for i in range(len(table_msg)):
                            if 'varietyname' in table_msg[i]:
                                combox_list.append(table_msg[i]['varietyname'])
                        if self.dict['head']['setCombox'] == 1:
                            self.mainWidget.getCurrentTableObject().categCombox.clear()
                            self.mainWidget.getCurrentTableObject().categCombox.addItems(set(combox_list))
                        self.updateTable(table_msg)
            else:
                categCombox = self.mainWidget.getRights()
                list_select = []
                if len(self.dict['body']) > 0:
                    if categCombox == "":
                        list_select = self.dict['body'][0]
                    else:
                        for i in range(len(self.dict['body'][0])):
                            if 'varietyname' in self.dict['body'][0][i]:
                                if self.dict['body'][0][i]['varietyname'] == categCombox:
                                    list_select.append(self.dict['body'][0][i])
                    table_msg = list_select
                    if len(table_msg) > 0:
                        self.updateTable(table_msg)
        except Exception as e:
            pass

    def treeMenuClicked(self):
        """菜单展开"""
        self.resetOrInit()

    def order(self):
        '''下单'''
        print("order")
        pass

    def resetOrInit(self):
        '''重置/初始化'''
        try:
            dateRange = self.mainWidget.getDataRange()
            startdate = dateRange[1].replace('-', '')
            enddate = startdate
            data = {"head": {"cmd": "listtradeorder", "setCombox": 1, "recvhandle": self.Recvmsg}, 'body': [{'autohedge': self.mainWidget.getCurrentHedgeStatus(), 'deptid': Variable.Variable.deptid, 'startdate': startdate, 'enddate': enddate}]}
            data = json.dumps(data)
            pass

        except Exception as e:
            pass

    def query(self):
        '''查询'''
        try:
            varietyId = self.mainWidget.getCurrentTableObject().categCombox.currentText()
            dateRange = self.mainWidget.getDataRange()
            startdate = dateRange[0].replace('-', '')
            enddate = dateRange[1].replace('-', '')
            if startdate > enddate:
                QMessageBox.information(self, '提示', '请输入正确的日期')
            else:
                if varietyId == "":
                    data = {"head": {"cmd": "listtradeorder", "setCombox": 0, "recvhandle": self.Recvmsg}, 'body': [
                        {'autohedge': self.mainWidget.getCurrentHedgeStatus(), 'deptid': Variable.Variable.deptid,
                         'startdate': startdate, 'enddate': enddate}]}
                else:
                    data = {"head": {"cmd": "listtradeorder", "setCombox": 0, "recvhandle": self.Recvmsg}, 'body': [
                        {'varietyId': varietyId, 'autohedge': self.mainWidget.getCurrentHedgeStatus(), 'deptid': Variable.Variable.deptid,
                             'startdate': startdate, 'enddate': enddate}]}
                data = json.dumps(data)
                pass
        except Exception as e:
            pass

    def exchangePage(self):
        '''换页'''
        currentPage = self.mainWidget.getCurrentTableObject().pageGroupButton.currentPage
        if currentPage == 1:
            self.mainWidget.getCurrentTableObject().table.verticalScrollBar().setSliderPosition(0)
        else:
            num = (currentPage - 1) * 35 * 24
            self.mainWidget.getCurrentTableObject().table.verticalScrollBar().setValue(num)

    def updateTable(self, data_list):
        '''更新表格'''
        # 查询tableObject，查询当前页码
        # 查询当前日期区间（筛选功能）
        currentTable =  self.mainWidget.getCurrentTableObject()
        currentTable.updateTable(data_list)



if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = StatementAnalysisMgr()
    ex.show()
    sys.exit(app.exec_())
