# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demo.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 676)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 20, 900, 600))
        self.widget.setMinimumSize(QSize(900, 600))
        self.widget.setMaximumSize(QSize(900, 600))
        self.widget.setStyleSheet(u"#widget{\n"
"background-color: rgb(46,56,96);\n"
"border-radius:20px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setStyleSheet(u"#widget_2{\n"
"background-color: rgb(17,30,70);\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:15px;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(270, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 24pt \"Microsoft YaHei UI\";")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(198, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.frame = QFrame(self.widget_2)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.setting = QPushButton(self.frame)
        self.setting.setObjectName(u"setting")
        self.setting.setStyleSheet(u"#setting{\n"
"	color: rgb(255,255,255);\n"
"	\n"
"\n"
"}\n"
"QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-bottom:5px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/set.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setting.setIcon(icon)
        self.setting.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.setting)

        self.hiding = QPushButton(self.frame)
        self.hiding.setObjectName(u"hiding")
        self.hiding.setStyleSheet(u"#hiding{\n"
"	color: rgb(255,255,255);\n"
"	\n"
"\n"
"}\n"
"QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-bottom:5px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/\u4e00.png", QSize(), QIcon.Normal, QIcon.Off)
        self.hiding.setIcon(icon1)
        self.hiding.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.hiding)

        self.enlarge = QPushButton(self.frame)
        self.enlarge.setObjectName(u"enlarge")
        self.enlarge.setStyleSheet(u"#enlarge{\n"
"	color: rgb(255,255,255);\n"
"	\n"
"\n"
"}\n"
"QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-bottom:5px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/enlarge.png", QSize(), QIcon.Normal, QIcon.Off)
        self.enlarge.setIcon(icon2)
        self.enlarge.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.enlarge)

        self.close = QPushButton(self.frame)
        self.close.setObjectName(u"close")
        self.close.setStyleSheet(u"#close{\n"
"	color: rgb(255,255,255);\n"
"\n"
"}\n"
"QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-bottom:5px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close.setIcon(icon3)
        self.close.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.close)


        self.horizontalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(10)
        sizePolicy2.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy2)
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftBar = QWidget(self.widget_3)
        self.LeftBar.setObjectName(u"LeftBar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.LeftBar.sizePolicy().hasHeightForWidth())
        self.LeftBar.setSizePolicy(sizePolicy3)
        self.LeftBar.setMinimumSize(QSize(68, 0))
        self.LeftBar.setMaximumSize(QSize(68, 16777215))
        self.LeftBar.setStyleSheet(u"#LeftBar{\n"
"background-color:rgb(17,30,70);\n"
"border-bottom-left-radius:15px;\n"
"\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.LeftBar)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 0, 0, 0)
        self.widget_4 = QWidget(self.LeftBar)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy3.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy3)
        self.widget_4.setMinimumSize(QSize(160, 68))
        self.widget_4.setMaximumSize(QSize(160, 68))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.widget_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(55, 55))
        self.frame_2.setMaximumSize(QSize(55, 55))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 14, 1)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(55, 55))
        self.label_3.setMaximumSize(QSize(55, 55))
        self.label_3.setStyleSheet(u"border-image: url(:/icons/icons/conan.png);")

        self.horizontalLayout_5.addWidget(self.label_3)


        self.horizontalLayout_4.addWidget(self.frame_2)

        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 18pt \"Microsoft YaHei UI\";")

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_6 = QWidget(self.LeftBar)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(2)
        sizePolicy4.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy4)
        self.widget_6.setMinimumSize(QSize(160, 0))
        self.widget_6.setMaximumSize(QSize(160, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Hide = QPushButton(self.widget_6)
        self.Hide.setObjectName(u"Hide")
        self.Hide.setMinimumSize(QSize(60, 0))
        self.Hide.setMaximumSize(QSize(160, 16777215))
        self.Hide.setStyleSheet(u"#Hide{\n"
"	color: rgb(255,255,255);\n"
"	\n"
"	font: 26pt \"Microsoft YaHei UI\";\n"
"}\n"
"QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-bottom:5px;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Hide.setIcon(icon4)
        self.Hide.setIconSize(QSize(64, 64))

        self.verticalLayout_3.addWidget(self.Hide)

        self.img = QPushButton(self.widget_6)
        self.img.setObjectName(u"img")
        self.img.setMinimumSize(QSize(60, 0))
        self.img.setMaximumSize(QSize(160, 16777215))
        self.img.setStyleSheet(u"#img{\n"
"	color: rgb(255,255,255);\n"
"	\n"
"	font: 26pt \"Microsoft YaHei UI\";\n"
"}\n"
"QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-bottom:5px;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/img.png", QSize(), QIcon.Normal, QIcon.Off)
        self.img.setIcon(icon5)
        self.img.setIconSize(QSize(60, 60))

        self.verticalLayout_3.addWidget(self.img)

        self.video = QPushButton(self.widget_6)
        self.video.setObjectName(u"video")
        self.video.setMinimumSize(QSize(60, 0))
        self.video.setMaximumSize(QSize(160, 16777215))
        self.video.setStyleSheet(u"#video{\n"
"	color: rgb(255,255,255);\n"
"	\n"
"	font: 26pt \"Microsoft YaHei UI\";\n"
"}\n"
"QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-bottom:5px;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/camera.png", QSize(), QIcon.Normal, QIcon.Off)
        self.video.setIcon(icon6)
        self.video.setIconSize(QSize(64, 64))

        self.verticalLayout_3.addWidget(self.video)

        self.add = QPushButton(self.widget_6)
        self.add.setObjectName(u"add")
        self.add.setMinimumSize(QSize(60, 0))
        self.add.setMaximumSize(QSize(160, 16777215))
        self.add.setStyleSheet(u"#add{\n"
"	color: rgb(255,255,255);\n"
"	\n"
"	font: 26pt \"Microsoft YaHei UI\";\n"
"}\n"
"QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-bottom:5px;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add.setIcon(icon7)
        self.add.setIconSize(QSize(64, 64))

        self.verticalLayout_3.addWidget(self.add)

        self.about = QPushButton(self.widget_6)
        self.about.setObjectName(u"about")
        self.about.setMinimumSize(QSize(60, 0))
        self.about.setMaximumSize(QSize(160, 16777215))
        self.about.setStyleSheet(u"#about{\n"
"	color: rgb(255,255,255);\n"
"	\n"
"	font: 26pt \"Microsoft YaHei UI\";\n"
"}\n"
"QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-bottom:5px;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.about.setIcon(icon8)
        self.about.setIconSize(QSize(64, 64))

        self.verticalLayout_3.addWidget(self.about)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.LeftBar)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setMinimumSize(QSize(160, 0))
        self.widget_7.setMaximumSize(QSize(160, 16777215))

        self.verticalLayout_2.addWidget(self.widget_7)


        self.horizontalLayout.addWidget(self.LeftBar)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.la = QLabel(self.widget_5)
        self.la.setObjectName(u"la")

        self.horizontalLayout_6.addWidget(self.la)

        self.stackedWidget = QStackedWidget(self.widget_5)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(17,30,70);")
        self.about_ = QWidget()
        self.about_.setObjectName(u"about_")
        self.label_4 = QLabel(self.about_)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(270, 160, 211, 81))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 24pt \"Microsoft YaHei UI\";")
        self.stackedWidget.addWidget(self.about_)
        self.add_ = QWidget()
        self.add_.setObjectName(u"add_")
        self.label_5 = QLabel(self.add_)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(290, 30, 141, 71))
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 24pt \"Microsoft YaHei UI\";")
        self.info_1 = QLabel(self.add_)
        self.info_1.setObjectName(u"info_1")
        self.info_1.setGeometry(QRect(120, 140, 211, 101))
        self.info_1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 24pt \"Microsoft YaHei UI\";")
        self.info_2 = QLabel(self.add_)
        self.info_2.setObjectName(u"info_2")
        self.info_2.setGeometry(QRect(430, 150, 211, 101))
        self.info_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 24pt \"Microsoft YaHei UI\";")
        self.add_info = QPushButton(self.add_)
        self.add_info.setObjectName(u"add_info")
        self.add_info.setGeometry(QRect(110, 400, 161, 51))
        self.add_info.setStyleSheet(u"font: 18pt \"Microsoft YaHei UI\";\n"
"color: white;\n"
"background-color: rgb(170, 85, 255);")
        self.clear_info = QPushButton(self.add_)
        self.clear_info.setObjectName(u"clear_info")
        self.clear_info.setGeometry(QRect(490, 390, 161, 51))
        self.clear_info.setStyleSheet(u"font: 18pt \"Microsoft YaHei UI\";\n"
"color: white;\n"
"background-color: rgb(170, 85, 255);")
        self.stackedWidget.addWidget(self.add_)
        self.img_ = QWidget()
        self.img_.setObjectName(u"img_")
        self.label_6 = QLabel(self.img_)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(260, 160, 211, 81))
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 24pt \"Microsoft YaHei UI\";")
        self.stackedWidget.addWidget(self.img_)
        self.video_ = QWidget()
        self.video_.setObjectName(u"video_")
        self.label_7 = QLabel(self.video_)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(250, 130, 211, 81))
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 24pt \"Microsoft YaHei UI\";")
        self.stackedWidget.addWidget(self.video_)

        self.horizontalLayout_6.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.widget_5)


        self.verticalLayout.addWidget(self.widget_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.close.clicked.connect(MainWindow.close)
        self.hiding.clicked.connect(MainWindow.showMinimized)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TopBar", None))
        self.setting.setText("")
        self.hiding.setText("")
        self.enlarge.setText("")
        self.close.setText("")
        self.label_3.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u" @\u9cb8\u53ef\u843d", None))
        self.Hide.setText(QCoreApplication.translate("MainWindow", u"  Hide", None))
        self.img.setText(QCoreApplication.translate("MainWindow", u"    img", None))
        self.video.setText(QCoreApplication.translate("MainWindow", u" video", None))
        self.add.setText(QCoreApplication.translate("MainWindow", u"   Add", None))
        self.about.setText(QCoreApplication.translate("MainWindow", u" about", None))
        self.la.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u6211\u662fabout", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u6211\u662fadd", None))
        self.info_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.info_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.add_info.setText(QCoreApplication.translate("MainWindow", u"add", None))
        self.clear_info.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u6211\u662fimg", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u6211\u662fvideo", None))
    # retranslateUi

