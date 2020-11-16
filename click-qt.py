from PyQt5 import QtWidgets
information = QtWidgets.QApplication([])
form = QtWidgets.QWidget()
slow = QtWidgets.QPushButton("test", parent=form)
text = QtWidgets.QLabel("test", parent=form)
form.setGeometry(700, 700, 700, 700)
form.setWindowTitle("test")

slow.setStyleSheet("QPushButton"
                  "{"
                  "background-color: lightgray;"
                  "}"
                  "color: red;"
                  "}"
               )

 
def slowmode():
 print("test")


slow.clicked.connect(lambda: slowmode())
slow.resize(500, 100)
slow.move(400 ,100) 
form.show() 

information.exec_()