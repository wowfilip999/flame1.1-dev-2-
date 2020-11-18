from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
z = QtWidgets.QApplication([])
u = QtWidgets.QWidget()
u.setGeometry(500, 500, 500, 500)
u.setWindowTitle("flame1.1 extesion manager")
disable = QtWidgets.QPushButton("disable on start", parent=u)


def disablefunct():
 print("t")



u.show()


disable.clicked.connect(lambda: disablefunct())

disable.resize(50 ,50)
disable.setFont(QFont("Arial", 20))
disable.move(500, 60)



z.exec_()


