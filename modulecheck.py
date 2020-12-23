from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
import os

try:
	import pyautogu
	import PyQt5
except:
    check = QtWidgets.QApplication([])
    form = QtWidgets.QWidget()
    form.setWindowTitle("flame module hecker")
    yes = QtWidgets.QPushButton("yes", parent=form)
    no = QtWidgets.QPushButton("no", parent=form)
    install = QtWidgets.QLabel("wants install", parent=form)

    
    install.setStyleSheet("QLabel"
                   "{"
                   "color: blue;"
                   "}"
                 )

    yes.setStyleSheet("QPushButton"
                   "{"
                   "background-color: lightgray;"
                   "}"
                 )

    no.setStyleSheet("QPushButton"
                   "{"
                   "background-color: lightgray;"
                   "}"
                 )

    def checkfunct():
     os.system("pip3 install pyautogui")
     


    form.setGeometry(500, 500, 500, 500)
    form.show()

    no.move(150, 100)
    yes.move(150, 180)
    no.resize(190, 70)
    yes.resize(190, 70)

    install.move(90, 40)
    install.setFont(QFont("Italic", 11))

    check.exec_()