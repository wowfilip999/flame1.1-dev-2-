import os
# import extesionload #launch the run.py 
class fla:
  a = ("600")
  b = ("600x600")


from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QFont, QIcon
flame = QtWidgets.QApplication([])
fl = QtWidgets.QWidget()
fl.setGeometry(600, 600 ,600 ,600)
manual = QtWidgets.QPushButton("?", parent=fl)
creator = QtWidgets.QLabel("by wowfilip999", parent=fl)
click = QtWidgets.QPushButton("click", parent=fl)
info = QtWidgets.QPushButton("info", parent=fl)
github = QtWidgets.QPushButton("", parent=fl)
settings = QtWidgets.QPushButton("settings", parent=fl)
minecraft = QtWidgets.QPushButton("minecraft", parent=fl)
exit = QtWidgets.QPushButton("exit", parent=fl)
name = QtWidgets.QLabel("Flame Autoclicker v 1.1", parent=fl)
oImage = QImage("pexels-rafael-guajardo-604671.jpg")
oImage = oImage.scaled(QSize(0,200))            
name.setFont(QFont("Arial", 20))
name.setStyleSheet("QLabel"
                  "{"
                  "color: darkred;"
                  "}"

                )


manual.setStyleSheet("QPushButton"
                     "{"
                     "background-color: lightgray;"
                     "}"
                     "QPushButton::pressed"
                     "{"
                     "background-color: red;"
                     "}"

                    )

minecraft.setStyleSheet("QPushButton"
                       "{"
                        "background-color: lightgray;"
                        "}"
                         "QPushButton::pressed"
                        "{"
                        "background-color : red;"
                        "}"

                    )




settings.setStyleSheet("QPushButton"
                       "{"
                        "background-color: lightgray;"
                        "}"
                         "QPushButton::pressed"
                        "{"
                        "background-color : red;"
                        "}"

                    )

exit.setStyleSheet("QPushButton"
                       "{"
                        "background-color: lightgray;"
                        "}"
                         "QPushButton::pressed"
                        "{"
                        "background-color : red;"
                        "}"

                    )

click.setStyleSheet("QPushButton"
                "{"
                "background-color: lightgray;"
                "}"
                "QPushButton::pressed"
                "{"
                "background-color : red;"
                "}"

               )



info.setStyleSheet("QPushButton"
                "{"
                "background-color: lightgray;"
                "width: 20px;"
                "}"
                "QPushButton::pressed"
                "{"
                "background-color : red;"
                "}"
             )


def infofunct():
 os.system("python3 click-qt.py")

def set():
 flame.quit()
 try:
    os.system("python3 settings.py")
 except:
     os.system("python settings.py")


def appexit():
 quit()


def githubfunct():
 import webbrowser
 webbrowser.open("www.github.com/wowfilip999")


def man():
 print("t")


click.clicked.connect(lambda: print("warn"))
info.clicked.connect(lambda: infofunct())
settings.clicked.connect(lambda: set())
exit.clicked.connect(lambda: appexit())
github.clicked.connect(lambda: githubfunct())
manual.clicked.connect(lambda: man())

manual.setFont(QFont("italic", 15))



manual.move(1230, 650)
manual.resize(50, 50)
click.move(420, 140)
click.resize(500, 90)
minecraft.move(420, 230)
minecraft.resize(500 ,90)

name.move(530, 0)
settings.move(420, 320)
settings.resize(500, 90)
info.move(420, 410)
info.resize(500 ,90)
exit.resize(500 ,90)
exit.move(420, 500)
creator.move(70 ,670)
github.move(0, 650)
github.resize(50 ,50)
github.setIcon(QIcon('githubb.png')) 
fl.show()

flame.exec_()

