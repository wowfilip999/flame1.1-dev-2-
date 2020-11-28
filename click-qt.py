from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
class style:
  o = "lightgray"

click = QtWidgets.QApplication([])
form = QtWidgets.QWidget()
slow = QtWidgets.QPushButton("slow", parent=form)
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

 
def slowmode():
 print("test")


slow.clicked.connect(lambda: slowmode())
slow.resize(500, 100)
slow.move(400 ,100)
text.setFont(QFont("Arial", 20))
slow.setFont(QFont("Arial", 17))
text.move(550, 40)
form.show() 

click.exec_()