from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
t = "slow"
class style:
  o = "lightgray"

click = QtWidgets.QApplication([])
form = QtWidgets.QWidget()
info = QtWidgets.QRadioButton("", parent=form)
slow = QtWidgets.QPushButton(t, parent=form)
fast = QtWidgets.QPushButton("fast", parent=form)
text = QtWidgets.QLabel("select modes", parent=form)
form.setGeometry(700, 700, 700, 700)
form.setWindowTitle("flame > click modes")

text.setStyleSheet("QLabel"
                 "{"
                 "color: darkred;"
                 "}"

               )

slow.setStyleSheet("QPushButton"
                   "{"
                   "background-color: lightgray;"
                   "width: 20px;"
                   "}"
                   "QPushButton::pressed"
                   "{"
                   "background-color : blue;"
                   "}"
               )

fast.setStyleSheet("QPushButton"
                   "{"
                   "background-color: lightgray;"
                   "width: 20px;"
                   "}"
                   "QPushButton::pressed"
                   "{"
                   "background-color : blue;"
                   "}"
               )

 
def slowmode():
 t = "test"
 click.update()

def fastfunct():
 print("test")


def infofunct():
 print("test")



slow.clicked.connect(lambda: slowmode())
fast.clicked.connect(lambda: fast())
info.clicked.connect(lambda: infofunct())

slow.resize(500, 100)
fast.resize(500, 100)
slow.move(400, 100)
fast.move(400, 200)
text.setFont(QFont("Arial", 20))
slow.setFont(QFont("Arial", 17))
fast.setFont(QFont("Arial", 17))
text.move(550, 40)
info.move(720, 55)
form.show() 

click.exec_()