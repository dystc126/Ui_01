from PySide6.QtWidgets import QApplication,QMainWindow
from PySide6.QtWidgets import *

from PySide6.QtCore import Signal


import sys
from ui.Ui_addWin import Ui_MainWindow

class AddWin(QMainWindow):
    info_signal = Signal(list)
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.init_slot()
    def init_slot(self):
        self.ui.add_info.clicked.connect(self.addinfo)
        self.ui.cancel_info.clicked.connect(self.exit)
    def addinfo(self):
        info_1 = self.ui.lineEdit.text()
        info_2 = self.ui.lineEdit_2.text()
        self.info_signal.emit([info_1,info_2])
        #发送完后应该关闭窗口
        #根据实际情况调整
        self.exit()


    def exit(self):
        self.close()




if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = AddWin()
    sys.exit(app.exec())