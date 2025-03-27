from main_win import *
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class UIFuncitons(QMainWindow):
    # Expand left menu
    def toggleMenu(self, enable):
        if enable:
            standard = 68
            maxExtend = 200
            width = self.LeftBar.width()

            if width == 200:
                widthExtended = standard
                
            else:
                widthExtended = maxExtend

            # animation
            self.animation = QPropertyAnimation(self.LeftBar, b"minimumWidth")
            self.animation.setDuration(500) # ms
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuint)
            self.animation.start()

