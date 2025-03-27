from PySide6.QtWidgets import QApplication,QMainWindow,QWidget,QGridLayout,QFileDialog,QMessageBox
from PySide6.QtCore import Qt,QThread,Signal
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QEvent, QTimer,QTime
from PySide6.QtGui import QIcon,QPainter,QBrush,QColor,QCursor,QPixmap,QImage,QConicalGradient,QPen,QFont
from PySide6 import QtCore,QtWidgets
from PySide6.QtWidgets import *


import sys
import warnings


from ui.Ui_login_win import Ui_MainWindow
from main_win import MainWin

from utils.utils import save_user_info,get_user_info
from utils.share import shareInfo



warnings.filterwarnings("ignore")






class LoginMainWin(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #隐藏窗口边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.show()
        self.init_slot()
    #初始化信号槽
    def init_slot(self):
        #初始显示界面标号0
        self.gotoStack(0)
        #登录界面按钮绑定界面0
        self.ui.login_2.clicked.connect(lambda: self.gotoStack(0))
        #注册界面按钮绑定界面1
        self.ui.register_2.clicked.connect(lambda: self.gotoStack(1))
        #取消按钮绑定界面0
        self.ui.cancel.clicked.connect(lambda: self.gotoStack(0))

        #绑定注册功能
        self.ui.register_4.clicked.connect(self.new_account)

        #绑定登录功能
        self.ui.login.clicked.connect(self.signIn)
        #隐藏输入密码
        self.ui.lineEdit_2.setEchoMode(QLineEdit.Password)


    def signIn(self):
        #获取用户名和密码
        username = self.ui.lineEdit.text().strip()
        password = self.ui.lineEdit_2.text().strip()
        shareInfo.username = username
        shareInfo.password = password
        #获取已注册用户信息
        USERS = get_user_info()
        if username not in USERS.keys():
            replay = QMessageBox.warning(self,'!','用户不存在',QMessageBox.Yes)
            self.gotoStack(0)
        else:
            #判断密码是否正确
            if USERS.get(username) == password:
                #编写跳转逻辑
                shareInfo.mainwin = MainWin()
                shareInfo.mainwin.show()
                #同时关闭登录界面
                self.close()
            else:
                replay = QMessageBox.warning(self,'!','密码输入错误',QMessageBox.Yes)
                self.gotoStack(0)
    def new_account(self):
        #获取已存在用户
        USERS = get_user_info()

        #获取用户名和密码
        new_username = self.ui.lineEdit_3.text().strip()
        new_userpwd = self.ui.lineEdit_4.text().strip()
        new_userpwd_2 = self.ui.lineEdit_5.text().strip()

        #如果用户名为空，则显示报错信息
        if new_username == "":
            replay = QMessageBox.warning(self,'!','账号名不许为空',QMessageBox.Yes)
        else:
            #若用户名存在，报错
            if new_username in USERS.keys():
                replay = QMessageBox.warning(self,'!','账号已存在',QMessageBox.Yes)
                self.gotoStack(1)
            else:
                #若密码不一致则报错
                if new_userpwd != new_userpwd_2:
                    replay = QMessageBox.warning(self,'!','密码不一致',QMessageBox.Yes)
                    self.gotoStack(1)
                else:
                    #注册成功
                    replay = QMessageBox.warning(self,'!','注册成功',QMessageBox.Yes)
                    #保存注册信息
                    save_user_info(new_username,new_userpwd)
                    #跳转登录界面
                    self.gotoStack(0)

    #stackwidget 切换
    def gotoStack(self, index: int):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.clear()
        self.ui.stackedWidget.setCurrentIndex(index)
    def add_shadow(self):
        # 添加阴影
        self.effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.effect_shadow.setOffset(0,0) # 偏移
        self.effect_shadow.setBlurRadius(100) # 阴影半径
        self.effect_shadow.setColor(QtCore.Qt.gray) # 阴影颜色
        self.ui.widget_2.setGraphicsEffect(self.effect_shadow) # 将设置套用到widget窗口中

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #app.setWindowIcon(QIcon(".\images\icon.ico"))
    window = LoginMainWin()
    sys.exit(app.exec())