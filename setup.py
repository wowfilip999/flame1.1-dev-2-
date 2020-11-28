from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QProcces
import os

app = QtWidgets.QApplication([])
formular = QtWidgets.QWidget()
formular.setGeometry(400, 400 ,400, 400)
welcome = QtWidgets.QLabel("welcome flame1.1 setup", parent=formular)
t = QtWidgets.QRadioButton("select os",parent=formular)


def select():
 
 

t.clicked.connect(lambda: select())

welcome.move(100, 20)
t.move(100, 100)
welcome.setFont(QFont("Italic", 15))

formular.show()	

app.exec_()
