# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_win.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(891, 607)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(130, 60, 600, 400))
        self.widget.setMinimumSize(QSize(600, 400))
        self.widget.setMaximumSize(QSize(600, 400))
        self.widget.setStyleSheet(u"#widget{\n"
"	border-radius:30px;\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setStyleSheet(u"#widget_2{\n"
"	border-top-left-radius:30px;\n"
"border-bottom-left-radius:30px;\n"
"\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"#label{\n"
"	border-top-left-radius:30px;\n"
"border-bottom-left-radius:30px;\n"
"	border-image: url(:/images/images/10001.jpg);\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy2)
        self.widget_3.setMaximumSize(QSize(300, 16777215))
        self.widget_3.setStyleSheet(u"#widget_3{\n"
"\n"
"	border-top-right-radius:30px;\n"
"border-bottom-right-radius:30px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.widget_3)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy3)
        self.frame_4.setStyleSheet(u"border-top-right-radius:30px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_11 = QSpacerItem(201, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_11)

        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(20, 20))
        self.pushButton_2.setMaximumSize(QSize(20, 20))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(4, 180, 0);\n"
"border:1px solid rgba(113, 17, 15,50);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(139, 29, 31)\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(232, 59, 35);\n"
"}\n"
"")

        self.horizontalLayout_8.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(20, 20))
        self.pushButton_3.setMaximumSize(QSize(20, 20))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(227, 199, 0);\n"
"border:1px solid rgba(113, 17, 15,50);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(139, 29, 31)\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(232, 59, 35);\n"
"}\n"
"")

        self.horizontalLayout_8.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(20, 20))
        self.pushButton.setMaximumSize(QSize(20, 20))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(240, 108, 96);\n"
"border:1px solid rgba(113, 17, 15,50);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(139, 29, 31)\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(232, 59, 35);\n"
"}\n"
"")

        self.horizontalLayout_8.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.widget_3)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy3.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy3)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.login_2 = QPushButton(self.frame_5)
        self.login_2.setObjectName(u"login_2")
        self.login_2.setStyleSheet(u"#login_2{\n"
"	border:none;\n"
"	font: 700 24pt \"Microsoft YaHei UI\";\n"
"}\n"
"#login_2:focus{\n"
"	color:rgb(221, 221, 221)\n"
"	}")
        self.login_2.setCheckable(True)
        self.login_2.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.login_2)

        self.line = QFrame(self.frame_5)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.register_2 = QPushButton(self.frame_5)
        self.register_2.setObjectName(u"register_2")
        self.register_2.setStyleSheet(u"#register_2{\n"
"	border:none;\n"
"	font: 700 24pt \"Microsoft YaHei UI\";\n"
"}\n"
"#register_2:focus{\n"
"	color:rgb(221, 221, 221)\n"
"	}")

        self.horizontalLayout_3.addWidget(self.register_2)

        self.horizontalSpacer_3 = QSpacerItem(101, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.widget_3)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(6)
        sizePolicy4.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy4)
        self.frame_6.setStyleSheet(u"frame_6{\n"
"	border-bottom-right-radius:30px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_6)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"border-bottom-right-radius:30px;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_7 = QFrame(self.page)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_8 = QSpacerItem(1, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)

        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy5)
        self.label_2.setStyleSheet(u"font: 700 18pt \"Microsoft YaHei UI\";")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.horizontalSpacer_9 = QSpacerItem(21, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.lineEdit = QLineEdit(self.frame_7)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(180, 0))
        self.lineEdit.setMaximumSize(QSize(180, 16777215))
        self.lineEdit.setStyleSheet(u"\n"
"QLineEdit{\n"
"	font-size: 23px;\n"
"	font-family: \"Microsoft YaHei\";\n"
"	background:rgba(253,253,253,1);\n"
"	border:3px solid rgb(0, 0, 0);\n"
"	/*\u5706\u89d25\u4e2a\u50cf\u7d20*/\n"
"	border-radius:5px;\n"
"}\n"
"/*\u7126\u70b9\u6837\u5f0f*/\n"
"QLineEdit:focus\n"
"{\n"
"	border:3px solid rgb(44,169,225);\n"
"	\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.lineEdit)

        self.horizontalSpacer_10 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.page)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(19, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 700 18pt \"Microsoft YaHei UI\";")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.horizontalSpacer_6 = QSpacerItem(27, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.lineEdit_2 = QLineEdit(self.frame_8)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(180, 0))
        self.lineEdit_2.setMaximumSize(QSize(180, 16777215))
        self.lineEdit_2.setStyleSheet(u"\n"
"QLineEdit{\n"
"	font-size: 23px;\n"
"	font-family: \"Microsoft YaHei\";\n"
"	background:rgba(253,253,253,1);\n"
"	border:3px solid rgb(0, 0, 0);\n"
"	/*\u5706\u89d25\u4e2a\u50cf\u7d20*/\n"
"	border-radius:5px;\n"
"}\n"
"/*\u7126\u70b9\u6837\u5f0f*/\n"
"QLineEdit:focus\n"
"{\n"
"	border:3px solid rgb(44,169,225);\n"
"	\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.lineEdit_2)

        self.horizontalSpacer_7 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.page)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_2 = QSpacerItem(19, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.login = QPushButton(self.frame_9)
        self.login.setObjectName(u"login")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.login.sizePolicy().hasHeightForWidth())
        self.login.setSizePolicy(sizePolicy6)
        self.login.setMinimumSize(QSize(250, 0))
        self.login.setMaximumSize(QSize(250, 16777215))
        self.login.setStyleSheet(u"#login{\n"
"\n"
"	background-color:rgb(0,0,0);\n"
"	color: rgb(255,255,255);\n"
"	border-radius:8px;\n"
"	border: 3px solid rgb(0,0,0);\n"
"	font: 700 20pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}\n"
"#login:hover{\n"
"	background-color:rgb(255,255,255);\n"
"	color: rgb(0,0,0);\n"
"}\n"
"#login:pressed{\n"
"	padding-top:8px;\n"
"	padding-left:8px;\n"
"}")

        self.horizontalLayout_7.addWidget(self.login)

        self.horizontalSpacer_4 = QSpacerItem(19, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addWidget(self.frame_9)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_3 = QVBoxLayout(self.page_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.frame_10 = QFrame(self.page_2)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy7)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_12 = QSpacerItem(9, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_12)

        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 700 16pt \"Microsoft YaHei UI\";")

        self.horizontalLayout_12.addWidget(self.label_4)

        self.horizontalSpacer_13 = QSpacerItem(11, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_13)

        self.lineEdit_3 = QLineEdit(self.frame_10)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(180, 0))
        self.lineEdit_3.setMaximumSize(QSize(180, 16777215))
        self.lineEdit_3.setStyleSheet(u"\n"
"QLineEdit{\n"
"	font-size: 23px;\n"
"	font-family: \"Microsoft YaHei\";\n"
"	background:rgba(253,253,253,1);\n"
"	border:3px solid rgb(0, 0, 0);\n"
"	/*\u5706\u89d25\u4e2a\u50cf\u7d20*/\n"
"	border-radius:5px;\n"
"}\n"
"/*\u7126\u70b9\u6837\u5f0f*/\n"
"QLineEdit:focus\n"
"{\n"
"	border:3px solid rgb(44,169,225);\n"
"	\n"
"}\n"
"")

        self.horizontalLayout_12.addWidget(self.lineEdit_3)

        self.horizontalSpacer_14 = QSpacerItem(8, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_14)


        self.verticalLayout_3.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.page_2)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy7.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy7)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_15 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_15)

        self.label_5 = QLabel(self.frame_11)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 700 16pt \"Microsoft YaHei UI\";")

        self.horizontalLayout_11.addWidget(self.label_5)

        self.horizontalSpacer_16 = QSpacerItem(23, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_16)

        self.lineEdit_4 = QLineEdit(self.frame_11)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(180, 0))
        self.lineEdit_4.setMaximumSize(QSize(180, 16777215))
        self.lineEdit_4.setStyleSheet(u"\n"
"QLineEdit{\n"
"	font-size: 23px;\n"
"	font-family: \"Microsoft YaHei\";\n"
"	background:rgba(253,253,253,1);\n"
"	border:3px solid rgb(0, 0, 0);\n"
"	/*\u5706\u89d25\u4e2a\u50cf\u7d20*/\n"
"	border-radius:5px;\n"
"}\n"
"/*\u7126\u70b9\u6837\u5f0f*/\n"
"QLineEdit:focus\n"
"{\n"
"	border:3px solid rgb(44,169,225);\n"
"	\n"
"}\n"
"")

        self.horizontalLayout_11.addWidget(self.lineEdit_4)

        self.horizontalSpacer_17 = QSpacerItem(6, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_17)


        self.verticalLayout_3.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.page_2)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy7.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy7)
        self.frame_12.setMinimumSize(QSize(200, 0))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_18 = QSpacerItem(9, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_18)

        self.label_6 = QLabel(self.frame_12)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 700 16pt \"Microsoft YaHei UI\";")

        self.horizontalLayout_10.addWidget(self.label_6)

        self.horizontalSpacer_19 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_19)

        self.lineEdit_5 = QLineEdit(self.frame_12)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(180, 0))
        self.lineEdit_5.setMaximumSize(QSize(180, 16777215))
        self.lineEdit_5.setStyleSheet(u"\n"
"QLineEdit{\n"
"	font-size: 23px;\n"
"	font-family: \"Microsoft YaHei\";\n"
"	background:rgba(253,253,253,1);\n"
"	border:3px solid rgb(0, 0, 0);\n"
"	/*\u5706\u89d25\u4e2a\u50cf\u7d20*/\n"
"	border-radius:5px;\n"
"}\n"
"/*\u7126\u70b9\u6837\u5f0f*/\n"
"QLineEdit:focus\n"
"{\n"
"	border:3px solid rgb(44,169,225);\n"
"	\n"
"}\n"
"")

        self.horizontalLayout_10.addWidget(self.lineEdit_5)

        self.horizontalSpacer_20 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_20)


        self.verticalLayout_3.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.page_2)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy7.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy7)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_21 = QSpacerItem(2, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_21)

        self.register_4 = QPushButton(self.frame_13)
        self.register_4.setObjectName(u"register_4")
        self.register_4.setMinimumSize(QSize(120, 0))
        self.register_4.setMaximumSize(QSize(120, 16777215))
        self.register_4.setStyleSheet(u"#register_4{\n"
"\n"
"	background-color:rgb(0,0,0);\n"
"	color: rgb(255,255,255);\n"
"	border-radius:8px;\n"
"	border: 3px solid rgb(0,0,0);\n"
"	font: 700 20pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}\n"
"#register_4:hover{\n"
"	background-color:rgb(255,255,255);\n"
"	color: rgb(0,0,0);\n"
"}\n"
"#register_4:pressed{\n"
"	padding-top:8px;\n"
"	padding-left:8px;\n"
"}")

        self.horizontalLayout_9.addWidget(self.register_4)

        self.horizontalSpacer_22 = QSpacerItem(3, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_22)

        self.cancel = QPushButton(self.frame_13)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setMinimumSize(QSize(120, 0))
        self.cancel.setMaximumSize(QSize(120, 16777215))
        self.cancel.setStyleSheet(u"#cancel{\n"
"\n"
"	background-color:rgb(0,0,0);\n"
"	color: rgb(255,255,255);\n"
"	border-radius:8px;\n"
"	border: 3px solid rgb(0,0,0);\n"
"	font: 700 20pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}\n"
"#cancel:hover{\n"
"	background-color:rgb(255,255,255);\n"
"	color: rgb(0,0,0);\n"
"}\n"
"#cancel:pressed{\n"
"	padding-top:8px;\n"
"	padding-left:8px;\n"
"}")

        self.horizontalLayout_9.addWidget(self.cancel)

        self.horizontalSpacer_23 = QSpacerItem(2, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_23)


        self.verticalLayout_3.addWidget(self.frame_13)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_4.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame_6)


        self.horizontalLayout.addWidget(self.widget_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton.setText("")
        self.login_2.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55", None))
        self.register_2.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u518c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None))
        self.login.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u518d\u6b21\u8f93\u5165", None))
        self.register_4.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u518c", None))
        self.cancel.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6d88", None))
    # retranslateUi

