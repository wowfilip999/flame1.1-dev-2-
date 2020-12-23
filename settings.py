from PyQt5 import QtWidgets
z = QtWidgets.QApplication([])
forr = QtWidgets.QWidget()
t = QtWidgets.QPushButton("bigger font", parent=forr)
forr.setGeometry(700, 700, 700, 700)

def fontfunct():
 f = open("bigfont-true.txt")
 f.close()


t.resize(30, 30)
t.move(50, 50)
t.clicked.connect(lambda: fontfunct())
forr.show()

z.exec_()