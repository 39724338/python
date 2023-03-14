import time

import win32con
import os
import sys
import win32gui
import win32print
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
# from Main.Views.Easytrade.statementanalysis.order import Order
from Main.Views.Easytrade.statementanalysis.qss import *
from Resources.Widget.PageGroupButton import PageGroupButton


class HedgeRecordWidget(QWidget):
    """
    :信号说明：
    :resetClicked: 点击触发重置按钮
    :queryClicked: 点击触发查询按钮
    :orderClicked: 点击触发下单按钮
    :pageBtnClicked: 点击触发页码控件
    """
    resetClicked = pyqtSignal()
    queryClicked = pyqtSignal()
    orderClicked = pyqtSignal()
    pageBtnClicked = pyqtSignal()

    def __init__(self):
        super(HedgeRecordWidget, self).__init__()
        self.autoHedgStatus = 0  # 控件属性，0：未初始化， 1：已套保，2：未套保
        self.initUi()

    def initUi(self):
        self.font5 = QFont("微软雅黑")
        pointsize5 = self.font5.pointSize()
        self.font5.setPixelSize(pointsize5 * 90 / 72)
        self.frame = QFrame()
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("#frame{border:1px solid #828790;background-color:#fff;border-top:0px;}")
        # 生成套保记录表
        self.table = HedgeTableWidget()
        tableFrame = QFrame()
        tableFrame.setStyleSheet("background:#e2e2e2;")
        categLable = QLabel()
        categLable.setText('品种')
        dateLabel = QLabel()
        dateLabel.setText('日    期')
        # 品种下拉框
        self.categCombox = CustomizeComboBoxWidget()
        self.startDateEdit = QDateEdit(QDate.currentDate().addDays(-90))  # 日历初始
        self.startDateEdit.setCalendarPopup(True)
        self.startDateEdit.setDisplayFormat("yyyy-MM-dd")
        self.endDateEdit = QDateEdit(QDate.currentDate(), self)  # 日历结束
        self.endDateEdit.setCalendarPopup(True)
        self.endDateEdit.setDisplayFormat("yyyy-MM-dd")
        betweenLabel = QLabel('至')

        self.resetBtn = QPushButton('重置')
        self.queryBtn = QPushButton('查询')
        self.orderBtn = QPushButton('下单')
        self.resetBtn.clicked.connect(self.onResetBtnClicked)
        self.queryBtn.clicked.connect(self.onQueryBtnClicked)
        self.orderBtn.clicked.connect(self.onOrderBtnClicked)

        if os.path.isdir("../Resources"):
            self.resetBtn.setStyleSheet(Qss.btnStyle1)
            self.resetBtn.setIcon(QIcon(QPixmap('client/yzClient/Resources/Images/reset.png')))
            self.queryBtn.setStyleSheet(Qss.btnStyle1)
            self.queryBtn.setIcon(QIcon(QPixmap('../Resources/Images/select.png')))
            self.orderBtn.setStyleSheet(Qss.btnStyle2)
            self.startDateEdit.setStyleSheet(Qss.dateEditStyle1)
            self.endDateEdit.setStyleSheet(Qss.dateEditStyle1)

        else:
            self.resetBtn.setStyleSheet(Qss.btnStyle1)
            self.resetBtn.setIcon(QIcon(QPixmap('./Resources/Images/reset.png')))
            self.queryBtn.setStyleSheet(Qss.btnStyle1)
            self.queryBtn.setIcon(QIcon(QPixmap('./Resources/Images/select.png')))
            self.orderBtn.setStyleSheet(Qss.btnStyle2)
            self.startDateEdit.setStyleSheet(Qss.dateEditStyle2)
            self.endDateEdit.setStyleSheet(Qss.dateEditStyle2)
        self.resetBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.queryBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.orderBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        head_frame = QFrame()
        head_frame.setObjectName("head_frame")
        head_frame.setStyleSheet(Qss.headFrameStyle)

        hbox_head = QHBoxLayout()
        hbox_head.addStretch(1)
        hbox_head.addWidget(categLable)
        hbox_head.addWidget(self.categCombox)
        hbox_head.addStretch(2)
        hbox_head.addWidget(dateLabel)
        hbox_head.addWidget(self.startDateEdit, 2)
        hbox_head.addWidget(betweenLabel)
        hbox_head.addWidget(self.endDateEdit, 2)
        hbox_head.addWidget(self.resetBtn)
        hbox_head.addWidget(self.queryBtn)
        hbox_head.addStretch(10)
        hbox_head.addWidget(self.orderBtn)
        hbox_head.addStretch(1)
        hbox_head.setContentsMargins(0, 11, 0, 0)
        head_frame.setLayout(hbox_head)

        bottom_frame = QFrame()
        bottom_frame.setObjectName("bottom_frame")
        bottom_frame.setStyleSheet(Qss.bottomFrameStyle)
        self.sumLabel = QLabel()
        self.sumLabel.setText('总计')
        self.purchaseLabel = QLabel()
        self.purchaseLabel.setText('采购:')
        self.purchaseNumLabel = QLabel()
        self.purchaseNumLabel.setText('')
        self.saleLabel = QLabel()
        self.saleLabel.setText('销售:')
        self.saleNumLabel = QLabel()
        self.saleNumLabel.setText('')
        hbox_bottom = QHBoxLayout()
        hbox_bottom.addStretch(1)
        hbox_bottom.addWidget(self.sumLabel)
        hbox_bottom.addStretch(3)
        hbox_bottom.addWidget(self.purchaseLabel)
        hbox_bottom.addWidget(self.purchaseNumLabel)
        hbox_bottom.addStretch(10)
        hbox_bottom.addWidget(self.saleLabel)
        hbox_bottom.addWidget(self.saleNumLabel)
        hbox_bottom.addStretch(15)
        bottom_frame.setLayout(hbox_bottom)
        fy_frame = QFrame()
        fy_frame.setObjectName("fy_frame")
        fy_frame.setStyleSheet(Qss.pageButtonFrame)
        # 分页功能控件
        self.pageGroupButton = PageGroupButton(1)
        self.pageGroupButton.clicked.connect(self.onPageBtnClicked)
        fy_box = QHBoxLayout()
        fy_box.addStretch(10)
        fy_box.addWidget(self.pageGroupButton)
        fy_box.addStretch(1)
        fy_box.setContentsMargins(0, 0, 0, 0)
        fy_frame.setLayout(fy_box)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.table)
        hbox4.setContentsMargins(0, 0, 0, 0)
        tableFrame.setLayout(hbox4)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(head_frame)
        vbox1.addWidget(tableFrame)
        vbox1.addWidget(bottom_frame)
        vbox1.addWidget(fy_frame)
        vbox1.setContentsMargins(0, 0, 0, 0)
        self.frame.setLayout(vbox1)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.frame)
        hbox2.setContentsMargins(0, 0, 0, 0)

        self.setLayout(hbox2)
        self.setContentsMargins(0, 0, 0, 0)

    def updateTable(self, data_list):
        """
       :function: set the table text
       :return: None
       """
        all_rows = len(data_list)
        if all_rows <= 22:
            maxPageNum = 1
        elif all_rows / 22 > all_rows // 22:
            maxPageNum = all_rows // 22 + 1
        else:
            maxPageNum = all_rows // 22
        self.pageGroupButton.maxPage = maxPageNum
        self.table.setRowCount(all_rows)
        num = 1
        purchaseNum = 0
        saleNum = 0
        # hedge_row_name = ['序号','订单编号','订单状态','品种','品牌','采销','数量','报单编号','套保状态','时间','']
        for i in range(all_rows):
            newitem = QTableWidgetItem('%s' % num)
            newitem.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            # 为每个表格内添加数据
            self.table.setItem(num - 1, 0, newitem)
            hedge_list = ['ordernumber', 'orderstatus', 'varietyname', 'brandname', 'direction',
                          'orderamount', 'serialid', 'hedgestatus', 'updatetime']
            num += 1
            # print(data_list[i])
            for j in range(1, len(hedge_list)):
                res = self.TransformData(hedge_list[j - 1], data_list[i][hedge_list[j - 1]], data_list[i]['tradetype'])
                newitem = QTableWidgetItem('{}'.format(res))
                newitem.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                # 为每个表格内添加数据
                self.table.setItem(i, j, newitem)
                self.table.setRowHeight(i, 35)

            # 成交时间
            newitem = QTableWidgetItem(
                '{}'.format((data_list[i][hedge_list[8]].replace("T", "-").replace("-", "/")[0:16])))
            newitem.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.table.setItem(i, len(hedge_list), newitem)
            self.table.setRowHeight(i, 35)

            if data_list[i]['direction'] == '1':
                purchaseNum += float(data_list[i]['orderamount'])
            elif data_list[i]['direction'] == '2':
                saleNum += float(data_list[i]['orderamount'])
        self.purchaseNumLabel.setText('{}'.format(purchaseNum))
        self.saleNumLabel.setText('{}'.format(saleNum))

    def TransformData(self, k, v, tradetype):
        """根据数据状态转换格式"""
        directionMap = {1: '采购', 2: '销售'}
        hedgestatusMap = {-1: '未发送', 0: '委托中', 1: '全部撤单', 2: '部分成交', 3: '全部成交', 4: '废单', 5: '过期', 6: '部分撤单'}
        # todo 点价寻货orderstatus状态码需要区分
        if tradetype == "1":
            orderStatusMap = {1: '请求挂单', 2: '同意挂单', 3: '拒绝挂单', 4: '已撤单', 5: '已成交', 6: '交易中', 7: '部分撤单', 8: '过期'}
        elif tradetype == "2":
            orderStatusMap = {1: '待处理', 2: '撤单', 3: '已成交', 4: '部分成交', 5: '过期', 6: '部分撤单'}

        if k == 'hedgestatus':
            return hedgestatusMap[int(v)]
        elif k == 'orderstatus':
            return orderStatusMap[int(v)]
        elif k == 'direction':
            return directionMap[int(v)]
        elif k == 'serialid':
            return '--'
        else:
            return v

    @property
    def autoHedge(self):
        return self.autoHedgStatus

    @autoHedge.setter
    def autoHedge(self, status):
        self.autoHedgStatus = status

    def setStartDate(self):
        self.startDateEdit.setDate(QDate.currentDate().addDays(-90))
        return self.startDateEdit

    def getDateRange(self):
        """
        :function: get the current range of date
        :return: list: [startDate, endDate]
        """
        return [self.startDateEdit.text(), self.endDateEdit.text()]

    def getRights(self):
        """
       :function: get the current rights
       :return: str: rights
       """
        return self.categCombox.currentText()

    def getSellSum(self):
        return float(self.saleNumLabel.text())

    def getPurchaseSum(self):
        return float(self.purchaseNumLabel.text())

    def onResetBtnClicked(self):
        self.resetClicked.emit()

    def onQueryBtnClicked(self):
        self.queryClicked.emit()

    def onOrderBtnClicked(self):
        self.orderClicked.emit()

    def onPageBtnClicked(self):
        self.pageBtnClicked.emit()


class HedgeTreeWidget(QWidget):
    resetClicked = pyqtSignal()
    queryClicked = pyqtSignal()
    orderClicked = pyqtSignal()
    pageBtnClicked = pyqtSignal()
    clicked = pyqtSignal()

    def __init__(self):
        super(HedgeTreeWidget, self).__init__()
        self.initUi()

    def initUi(self):
        self.tableSign = '已套保'

        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.width = self.screenRect.width()
        self.width = self.screenRect.width()
        # self.setMinimumWidth(self.width)
        self.resize(1200, 600)
        '''100%的缩放'''
        self.font5 = QFont("微软雅黑")
        pointsize5 = self.font5.pointSize()
        self.font5.setPixelSize(pointsize5 * 90 / 72)
        self.setStyleSheet(Qss.mainWindowStyle)

        self.tree_menu = QTreeWidget()
        self.tree_menu.header().hide()  # 隐藏表头
        self.tree_menu.setStyleSheet(Qss.treeMenuStyle)

        self.root_collect_sale = QTreeWidgetItem(self.tree_menu)
        self.root_collect_sale.setFont(0, self.font5)
        self.root_collect_sale.setText(0, '采销记录')
        self.root_collect_sale.setExpanded(1)

        # 设置已套保子目录
        self.subcatalog_hedge = QTreeWidgetItem(self.root_collect_sale)
        self.subcatalog_hedge.setFont(0, self.font5)
        self.subcatalog_hedge.setText(0, '已套保')
        self.subcatalog_hedge = HedgeRecordWidget()
        self.subcatalog_hedge.autoHedge = 1
        self.subcatalog_hedge.resetClicked.connect(self.onResetBtnClicked)
        self.subcatalog_hedge.queryClicked.connect(self.onQueryBtnClicked)
        self.subcatalog_hedge.orderClicked.connect(self.onOrderBtnClicked)
        self.subcatalog_hedge.pageBtnClicked.connect(self.onPageBtnClicked)

        # 设置未套保子目录
        self.subcatalog_not_hedge = QTreeWidgetItem(self.root_collect_sale)
        self.subcatalog_not_hedge.setFont(0, self.font5)
        self.subcatalog_not_hedge.setText(0, '未套保')
        self.subcatalog_not_hedge = HedgeRecordWidget()
        self.subcatalog_not_hedge.setHidden(1)
        self.subcatalog_not_hedge.autoHedge = 2
        self.subcatalog_not_hedge.resetClicked.connect(self.onResetBtnClicked)
        self.subcatalog_not_hedge.queryClicked.connect(self.onQueryBtnClicked)
        self.subcatalog_not_hedge.orderClicked.connect(self.onOrderBtnClicked)
        self.subcatalog_not_hedge.pageBtnClicked.connect(self.onPageBtnClicked)

        hb1 = QHBoxLayout()
        hb1.addWidget(self.tree_menu)
        hb1.setContentsMargins(0, 0, 0, 0)
        hb1.setSpacing(0)
        self.frame12 = QFrame()
        self.frame12.setObjectName("frame123213")
        self.frame12.setStyleSheet("border:0px solid red;border-right:1px solid #828790;")
        self.frame12.setLayout(hb1)

        hbox_all = QHBoxLayout()
        hbox_all.addWidget(self.frame12, 1)
        hbox_all.addWidget(self.subcatalog_hedge, 8)
        hbox_all.addWidget(self.subcatalog_not_hedge, 8)
        hbox_all.setContentsMargins(0, 0, 0, 0)

        self.setLayout(hbox_all)

        self.tree_menu.clicked.connect(self.onTreeMenuClicked)
        self.ordersingle = None

    def setStartDate(self):
        return self.subcatalog_hedge.setStartDate() if self.tableSign == '已套保' else self.subcatalog_not_hedge.setStartDate()

    def getRights(self):
        return self.subcatalog_hedge.getRights() if self.tableSign == '已套保' else self.subcatalog_not_hedge.getRights()

    def getDataRange(self):
        return self.subcatalog_hedge.getDateRange() if self.tableSign == '已套保' else self.subcatalog_not_hedge.getDateRange()

    def getTableObject(self):
        return self.subcatalog_hedge.table if self.tableSign == '已套保' else self.subcatalog_not_hedge.table

    def getCurrentHedgeStatus(self):
        return self.subcatalog_hedge.autoHedge if self.tableSign == '已套保' else self.subcatalog_not_hedge.autoHedge

    def getCurrentTableObject(self):
        return self.subcatalog_hedge if self.tableSign == '已套保' else self.subcatalog_not_hedge

    def onTreeMenuClicked(self):
        item = self.tree_menu.currentItem()
        if item.text(0) == '采销记录':
            self.clicked.emit()
            return 0

        if item.text(0) == '已套保':
            if item.parent().text(0) == '采销记录':
                self.tableSign = '已套保'
                self.subcatalog_not_hedge.setHidden(1)
                self.subcatalog_hedge.setHidden(0)
                self.clicked.emit()

        elif item.text(0) == '未套保':
            if item.parent().text(0) == '采销记录':
                self.tableSign = '未套保'
                self.subcatalog_hedge.setHidden(1)
                self.subcatalog_not_hedge.setHidden(0)
                self.clicked.emit()

    def onResetBtnClicked(self):
        self.resetClicked.emit()

    def onQueryBtnClicked(self):
        self.queryClicked.emit()

    def onOrderBtnClicked(self):
        try:
            if self.ordersingle == None:
                self.order = Order()
                self.ordersingle = 1
            self.order.show()
            self.order.getriskmsg()
        except Exception as e:
            print(e)

    def onPageBtnClicked(self):
        self.pageBtnClicked.emit()


class HedgeTableWidget(QTableWidget):
    def __init__(self):
        super(HedgeTableWidget, self).__init__()
        self.initUi()

    def initUi(self):
        self.font5 = QFont("微软雅黑")
        pointsize5 = self.font5.pointSize()
        self.font5.setPixelSize(pointsize5 * 90 / 72)
        self.setAlternatingRowColors(True)
        self.setStyleSheet(
            "QTableWidget{alternate-background-color:#DDE4EB;background:#f1f8ff;color:#000;border:1px solid #828790;border-left:0px;gridline-color:#f0f0f0;}"
            "QTableCornerButton::section{background-color:white;}"
            "QTableView::item:selected{background:#9ECEE7;}")
        self.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background:#e2e2e2;color:#000;border:0px solid black;font:15px '微软雅黑'}")
        self.verticalHeader().setStyleSheet("QHeaderView::section{background:white;color:black}")
        self.verticalScrollBar().setStyleSheet("QScrollBar{background:transparent; width: 10px;}"
                                               "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px;}"
                                               "QScrollBar::handle:hover{background:gray;}"
                                               "QScrollBar::sub-line{background:transparent;}"
                                               "QScrollBar::add-line{background:transparent;}")
        self.horizontalHeader().setSectionsClickable(False)  # 水平方向表头不可点击
        self.verticalHeader().setSectionsClickable(False)  # 垂直反向表头不可点击
        self.horizontalHeader().setDefaultAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.horizontalHeader().setMinimumHeight(30)  # 设置表头高度
        self.setShowGrid(1)  # 去表格线
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁止对表格编辑
        self.setFocusPolicy(Qt.NoFocus)  # 去除选中虚线
        self.setSelectionBehavior(QAbstractItemView.SelectRows)  # 整行选择
        self.setSelectionMode(QAbstractItemView.SingleSelection)  # 单选
        self.verticalHeader().setVisible(0)  # 隐藏列表头
        self.horizontalHeader().setVisible(1)  # 隐藏行表头
        self.setColumnCount(11)  # 设置列数
        self.hedge_row_name = ['序号', '订单编号', '订单状态', '品种', '品牌', '采销', '数量', '报单编号', '套保状态', '时间', '']
        self.setHorizontalHeaderLabels(self.hedge_row_name)
        self.horizontalHeader().setSectionResizeMode(1)  # 设置适应屏幕
        self.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.setFont(self.font5)
        # 滚动条以像素滚动
        self.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        # 获取屏幕的缩放比例
        hDC = win32gui.GetDC(0)
        dpi = win32print.GetDeviceCaps(hDC, win32con.LOGPIXELSX)
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()

        widthList = [77, 80, 80, 110, 110, 71, 110, 110, 75, 75, 75]
        for i in range(widthList.__len__()):
            self.setColumnWidth(i, widthList[i])

        if self.width >= 2560 and self.height >= 1400:
            self.horizontalHeader().setMinimumHeight(40)  # 设置表头高度
            self.verticalScrollBar().setStyleSheet("QScrollBar{background:#fff; width: 10px;}"
                                                   "QScrollBar::handle{background:lightgray; border:0px solid transparent; border-radius:5px;}"
                                                   "QScrollBar::handle:hover{background:gray;}"
                                                   "QScrollBar::sub-line{background:transparent;}"
                                                   "QScrollBar::add-line{background:transparent;}")

            self.horizontalScrollBar().setStyleSheet("QScrollBar{background:#FFF; height: 15px;}"
                                                     "QScrollBar::handle{background:gray; border:0px solid transparent; border-radius:7px;}"
                                                     "QScrollBar::handle:hover{background:gray;}"
                                                     "QScrollBar::sub-line{background:transparent;}"
                                                     "QScrollBar::add-line{background:transparent;}")
        elif self.width >= 1920 and self.height >= 1080 and dpi == 96:  # 100%的缩放
            self.horizontalHeader().setMinimumHeight(25)  # 设置表头高度
            self.verticalScrollBar().setStyleSheet("QScrollBar{background:#fff; width: 10px;}"
                                                   "QScrollBar::handle{background:lightgray; border:0px solid transparent; border-radius:5px;}"
                                                   "QScrollBar::handle:hover{background:gray;}"
                                                   "QScrollBar::sub-line{background:transparent;}"
                                                   "QScrollBar::add-line{background:transparent;}")

            self.horizontalScrollBar().setStyleSheet("QScrollBar{background:#FFF; height: 10px;}"
                                                     "QScrollBar::handle{background:gray; border:0px solid transparent; border-radius:5px;}"
                                                     "QScrollBar::handle:hover{background:gray;}"
                                                     "QScrollBar::sub-line{background:transparent;}"
                                                     "QScrollBar::add-line{background:transparent;}")
        elif self.width >= 1920 and self.height >= 1080 and dpi == 120:  # 125%的缩放
            self.horizontalHeader().setMinimumHeight(25)  # 设置表头高度
            self.verticalScrollBar().setStyleSheet("QScrollBar{background:#fff; width: 10px;}"
                                                   "QScrollBar::handle{background:lightgray; border:0px solid transparent; border-radius:5px;}"
                                                   "QScrollBar::handle:hover{background:gray;}"
                                                   "QScrollBar::sub-line{background:transparent;}"
                                                   "QScrollBar::add-line{background:transparent;}")

            self.horizontalScrollBar().setStyleSheet("QScrollBar{background:#FFF; height: 10px;}"
                                                     "QScrollBar::handle{background:gray; border:0px solid transparent; border-radius:5px;}"
                                                     "QScrollBar::handle:hover{background:gray;}"
                                                     "QScrollBar::sub-line{background:transparent;}"
                                                     "QScrollBar::add-line{background:transparent;}")
        elif self.width >= 1920 and self.height >= 1080 and dpi == 144:  # 100%的缩放
            self.horizontalHeader().setMinimumHeight(25)  # 设置表头高度
            self.verticalScrollBar().setStyleSheet("QScrollBar{background:#fff; width: 10px;}"
                                                   "QScrollBar::handle{background:lightgray; border:0px solid transparent; border-radius:5px;}"
                                                   "QScrollBar::handle:hover{background:gray;}"
                                                   "QScrollBar::sub-line{background:transparent;}"
                                                   "QScrollBar::add-line{background:transparent;}")

            self.horizontalScrollBar().setStyleSheet("QScrollBar{background:#FFF; height: 10px;}"
                                                     "QScrollBar::handle{background:gray; border:0px solid transparent; border-radius:5px;}"
                                                     "QScrollBar::handle:hover{background:gray;}"
                                                     "QScrollBar::sub-line{background:transparent;}"
                                                     "QScrollBar::add-line{background:transparent;}")
        elif self.width >= 1600 and self.height >= 1200:
            self.horizontalHeader().setMinimumHeight(25)  # 设置表头高度
            self.verticalScrollBar().setStyleSheet("QScrollBar{background:#fff; width: 10px;}"
                                                   "QScrollBar::handle{background:lightgray; border:0px solid transparent; border-radius:5px;}"
                                                   "QScrollBar::handle:hover{background:gray;}"
                                                   "QScrollBar::sub-line{background:transparent;}"
                                                   "QScrollBar::add-line{background:transparent;}")

            self.horizontalScrollBar().setStyleSheet("QScrollBar{background:#FFF; height: 10px;}"
                                                     "QScrollBar::handle{background:gray; border:0px solid transparent; border-radius:5px;}"
                                                     "QScrollBar::handle:hover{background:gray;}"
                                                     "QScrollBar::sub-line{background:transparent;}"
                                                     "QScrollBar::add-line{background:transparent;}")
        elif self.width >= 1600 and self.height >= 900:
            self.horizontalHeader().setMinimumHeight(25)  # 设置表头高度
            self.verticalScrollBar().setStyleSheet("QScrollBar{background:#fff; width: 7px;}"
                                                   "QScrollBar::handle{background:lightgray; border:0px solid transparent; border-radius:3px;}"
                                                   "QScrollBar::handle:hover{background:gray;}"
                                                   "QScrollBar::sub-line{background:transparent;}"
                                                   "QScrollBar::add-line{background:transparent;}")

            self.horizontalScrollBar().setStyleSheet("QScrollBar{background:#FFF; height: 10px;}"
                                                     "QScrollBar::handle{background:gray; border:0px solid transparent; border-radius:5px;}"
                                                     "QScrollBar::handle:hover{background:gray;}"
                                                     "QScrollBar::sub-line{background:transparent;}"
                                                     "QScrollBar::add-line{background:transparent;}")
        elif self.width >= 1366 and self.height >= 768:
            self.horizontalHeader().setMinimumHeight(25)  # 设置表头高度
            self.verticalScrollBar().setStyleSheet("QScrollBar{background:#fff; width: 5px;}"
                                                   "QScrollBar::handle{background:lightgray; border:0px solid transparent; border-radius:2px;}"
                                                   "QScrollBar::handle:hover{background:gray;}"
                                                   "QScrollBar::sub-line{background:transparent;}"
                                                   "QScrollBar::add-line{background:transparent;}")

            self.horizontalScrollBar().setStyleSheet("QScrollBar{background:#FFF; height: 7px;}"
                                                     "QScrollBar::handle{background:gray; border:0px solid transparent; border-radius:3px;}"
                                                     "QScrollBar::handle:hover{background:gray;}"
                                                     "QScrollBar::sub-line{background:transparent;}"
                                                     "QScrollBar::add-line{background:transparent;}")
        elif self.width <= 1400 and self.height <= 900:
            self.horizontalHeader().setMinimumHeight(25)  # 设置表头高度
            self.verticalScrollBar().setStyleSheet("QScrollBar{background:#fff; width: 7px;}"
                                                   "QScrollBar::handle{background:lightgray; border:0px solid transparent; border-radius:3px;}"
                                                   "QScrollBar::handle:hover{background:gray;}"
                                                   "QScrollBar::sub-line{background:transparent;}"
                                                   "QScrollBar::add-line{background:transparent;}")

            self.horizontalScrollBar().setStyleSheet("QScrollBar{background:#FFF; height: 10px;}"
                                                     "QScrollBar::handle{background:gray; border:0px solid transparent; border-radius:5px;}"
                                                     "QScrollBar::handle:hover{background:gray;}"
                                                     "QScrollBar::sub-line{background:transparent;}"
                                                     "QScrollBar::add-line{background:transparent;}")


class CustomizeComboBoxWidget(QComboBox):
    def __init__(self):
        super(CustomizeComboBoxWidget, self).__init__()
        self.initUi()

    def initUi(self):
        self.line = QLineEdit()
        self.line.setReadOnly(1)
        self.setLineEdit(self.line)
        self.line.setText('')
        self.line.setPlaceholderText('请选择')
        self.setStyleSheet("min-width:120px;max-width:120px;height:30px")


class TransferData:
    indexOfKeyMap = {'ordernumber': 1, 'orderstasus': 2, 'categname': 3, 'brandname': 4, 'direction': 5,
                     'orderamount': 6, 'hedgestatus': 8, 'updatetime': 9}
    orderStatusMap = {1: '请求挂单', 2: '同意挂单', 3: '拒绝挂单', 4: '已撤单', 5: '已成交', 6: '交易中', 7: '部分撤单', 8: '过期'}
    directionMap = {1: '采购', 2: '销售'}
    hedgestatusMap = {1: '已套保', 2: '未套保'}

    # todo 点价寻货orderstatus状态码需要区分

    @staticmethod
    def transferData(k, v):
        if k == 'orderstatus':
            return TransferData.orderStatusMap[v]
        elif k == 'direction':
            return TransferData.directionMap[v]
        elif k == 'hedgestatus':
            return TransferData.hedgestatusMap[v]
        else:
            return v


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = HedgeRecordWidget()
    ex.show()
    sys.exit(app.exec_())
