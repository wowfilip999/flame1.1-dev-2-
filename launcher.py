from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
import os

app = QtWidgets.QApplication([])
formular = QtWidgets.QWidget()
formular.setWindowTitle("flame launcher")
p = QtWidgets.QLabel("select", parent=formular)
tk = QtWidgets.QPushButton("flame1.1(Tk)" ,parent=formular)
qt = QtWidgets.QPushButton("flame1.1(Qt)", parent=formular)
formular.setGeometry(400 ,400 ,400 ,400)
def cmdtk():
 os.system("python3 flameautoclicker.py")

def cmd():
 os.system("python3 flameautoclicker-qt.py")


p.setFont(QFont("italic",20))
p.move(150, 10)

#tkinter
tk.resize(100 ,30)
tk.move(150 ,235)
tk.clicked.connect(lambda: cmdtk())

#tkinter

#PyQt5
qt.move(150, 200)
qt.resize(100 ,30)
qt.clicked.connect(lambda: cmd())
#PyQt5
p.setStyleSheet("QLabel"
	           "{"
	           "color: blue;"
	           "}"

	          )

formular.show()


app.exec_()
