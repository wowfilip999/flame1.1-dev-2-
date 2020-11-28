import os
# import extesionload #launch the run.py 
class fla:
  a = ("600")
  b = ("600x600")


from tkinter import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize, QProcess
from PyQt5.QtGui import QImage, QFont, QIcon
flame = QtWidgets.QApplication([])
fl = QtWidgets.QWidget()
fl.setGeometry(600, 600 ,600 ,600)
import random
message = random.randint(2, 4)
msg = "by wowfilip999"

if message == 3:
  msg = "test"
if message == 2:
  msg = "filip have 15 years"
else:
    msg = "by wowfilip999"
    

a = random.randint(4, 5)
b = random.randint(4, 5)
easteregG = QtWidgets.QPushButton("click me!", parent=fl)
manual = QtWidgets.QPushButton("?", parent=fl)
creator = QtWidgets.QLabel(msg, parent=fl)
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



def clickf():
 os.system("python3 click-qt.py")


def appexit():
 quit()


def githubfunct():
 import webbrowser
 webbrowser.open("www.github.com/wowfilip999")


def man():
 man = Tk()
 man.option_add('*Font', 'Times')
 man.geometry("500x500")
 t = Label(text="test",font="italic")
 t.place(x=50,y=50)

 man.mainloop()



click.clicked.connect(lambda: clickf())
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
j = 0
jj = 0 
n = 0
nn = 0
if a == 5:
  n = 20
  j = 20
  jj = 50
  nn = 20


easteregG.resize(j, n)


github.setIcon(QIcon('githubb.png')) 

def easter():
 creator.hide()
 github.hide()
 exit.hide()
 info.hide()
 manual.hide()
 click.hide()
 minecraft.hide()
 settings.hide()
 easteregG.hide()
 creator.show()

                    

if a == 5:
  easteregG.move(10 ,10)
  easteregG.resize(100, 100)
  easteregG.clicked.connect(lambda: easter())


fl.show()

flame.exec_()

