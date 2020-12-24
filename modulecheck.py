from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
import os

try:
	import pyautogui
	import PyQt5
except:
    check = QtWidgets.QApplication([])
    form = QtWidgets.QWidget()
    form.setWindowTitle("flame module hecker")
    yes = QtWidgets.QPushButton("yes", parent=form)
    no = QtWidgets.QPushButton("no", parent=form)
    install = QtWidgets.QLabel("your not have needed modules wants install ?", parent=form)

    
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

    def installfunct():
     try:
       os.system("pip3 install pyautogui")
     except:
         os.system("pip install pyautogui")
     

    def abort():
     check.quit()

    form.setGeometry(500, 500, 500, 500)
    form.show()
    
    yes.clicked.connect(lambda: installfunct())
    no.clicked.connect(lambda: abort())
    no.move(150, 100)
    yes.move(150, 180)
    no.resize(190, 70)
    yes.resize(190, 70)

    install.move(90, 40)
    install.setFont(QFont("Italic", 10))

    check.exec_()