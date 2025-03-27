from PySide6.QtWidgets import QApplication,QMainWindow,QMessageBox
from PySide6 import QtWidgets,QtCore
from PySide6.QtGui import QImage,QPixmap,QCursor
from PySide6.QtCore import Qt
#from ui.Ui_mainwin import Ui_MainWindow
from ui.Ui_demo import Ui_MainWindow
from UIFunctions import *

import copy
import sys
import cv2
import warnings
import base64
import numpy as np


warnings.filterwarnings('ignore')

from utils.share import shareInfo

from  addWin import AddWin



class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #隐藏窗口边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.show()

        self.cap = cv2.VideoCapture()
        self.timer  = QtCore.QTimer(self)
        #摄像头编号，默认为0，电脑内置摄像头
        self.camera_id = 0
        self.init_slot()

    def init_slot(self):
        #开始绑定信号和槽
        self.ui.Hide.clicked.connect(lambda:UIFuncitons.toggleMenu(self.ui,True))
        self.ui.img.clicked.connect(lambda:self.gotostack(2))
        self.ui.video.clicked.connect(lambda:self.gotostack(3))
        self.ui.add.clicked.connect(lambda:self.gotostack(1))
        self.ui.about.clicked.connect(lambda:self.gotostack(0))

        ###########################
        self.ui.add_info.clicked.connect(self.addwin_show)
        self.ui.clear_info.clicked.connect(self.clear_info)
    def addwin_show(self):
        self.addwin = AddWin()
        self.addwin.show()
        #接受信息，并传给处理函数
        self.addwin.info_signal.connect(lambda info_list:self.show_info(info_list))
    def show_info(self, info_list):
        info1 = info_list[0]
        info_2 = info_list[1]

        self.ui.info_1.setText(info1)
        self.ui.info_2.setText(info_2)
    def clear_info(self):
        self.ui.info_1.clear()
        self.ui.info_2.clear()

    def gotostack(self,index):
        self.ui.stackedWidget.setCurrentIndex(index)
        pass
    # def open_camera(self):
    #     #摄像头未打开，打开摄像头，定时器开始倒计时
    #     if self.timer.isActive() == False:
    #         flag = self.cap.open(self.camera_id,cv2.CAP_DSHOW)
    #         #读取失败报错
    #         if flag == False:
    #             QMessageBox.warning(self,'warning','请检查摄像头是否连接正确',
    #             QMessageBox.Ok)
    #         #否则显示
    #         else:
    #             self.timer.start(30)
    #             self.ui.open.setText("关闭摄像头")
    #     #摄像头打开，计时器停止，释放资源
    #     else:
    #         self.timer.stop()
    #         self.cap.release()
    #         self.clear()
    #         self.ui.open.setText("打开摄像头")
    #     pass
    # def show_camera(self):
    #     ret,frame = self.cap.read()
    #     if ret:
    #         #读取成功
    #         frame = cv2.flip(frame,1)
    #         self.show_img(frame,self.ui.label)
    #     #否则报错
    #     else:
    #         QMessageBox.information(self,"警告","摄像头读取错误",QMessageBox.Ok)
    def show_img(self,im,label):
        try:
            #获取高和宽
            ih,iw ,_ = im.shape
            #获取标签的长和高
            w = label.geometry().width()
            h = label.geometry().height()
            #上述的目的是为了保持原始的纵横比
            if iw/w >ih/h:
                scal = w/iw
                nw = w
                nh = int(scal * ih)
                im_new = cv2.resize(im,(nw,nh))
            else:
                scal = w/iw
                nw = int(scal*iw)
                nh = h
                im_new = cv2.resize(im,(nw,nh))
            frame = cv2.cvtColor(im_new,cv2.COLOR_BGR2RGB)
            im = QImage(frame.data,frame.shape[1],frame.shape[0],frame.shape[2] * frame.shape[1],
                        QImage.Format_RGB888)
            label.setPixmap(QPixmap.fromImage(im))
        except Exception as e:
            print(repr(e))
    def clear(self):
        self.ui.label.clear()
        self.timer.stop()
        self.cap.release()
        self.ui.open.setText("打开摄像头")
        pass
    #窗口拖动
    ##############################################################################
    def mousePressEvent(self,event):
        if event.button() == Qt.LeftButton and self.isMaximized() == False:
            self.mm_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
    def mouseMoveEvent(self,mouseMove):
        if Qt.LeftButton and self.mm_flag:
            self.move(mouseMove.globalPos()-self.m_Position)
            mouseMove.accept()
    def mouseReleaseEvent(self,mouse_event):
        self.mm_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))
    ##############################################################################

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWin()
    sys.exit(app.exec())