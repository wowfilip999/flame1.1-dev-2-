from PyQt5 import QtWidgets
print("hej hej")
z = QtWidgets.QApplication([])
forr = QtWidgets.QWidget()
t = QtWidgets.QPushButton("extesions settings", parent=forr)
forr.setGeometry(700, 700, 700, 700)

forr.show()

z.exec_()