import os
import looksettings as look
# import extesionload #launch the run.py 
class fla:
  a = ("600")
  b = ("600x600")


import platform

operatingsystem = platform.system()

if operatingsystem == "Linux":
  os.system("python3 modulecheck.py")

if operatingsystem == "Windows":
  os.system("python modulecheck.py")



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
  msg = "wowfilip999 is big pp programmer"
if message == 2:
  msg = "filip have 15 years"
else:
    msg = "by wowfilip999"
    

a = random.randint(4, 6)
b = random.randint(4, 6)
easteregG = QtWidgets.QPushButton("click me!", parent=fl)
manual = QtWidgets.QPushButton("?", parent=fl)
creator = QtWidgets.QLabel(msg, parent=fl)
click = QtWidgets.QPushButton("click", parent=fl)
info = QtWidgets.QPushButton("info", parent=fl)
github = QtWidgets.QPushButton("", parent=fl)
settings = QtWidgets.QPushButton("settings", parent=fl)
system = QtWidgets.QLabel(operatingsystem, parent=fl)
on = QtWidgets.QLabel("on", parent=fl)
minecraft = QtWidgets.QPushButton("minecraft", parent=fl)
exit = QtWidgets.QPushButton("exit", parent=fl)
name = QtWidgets.QLabel("Flame Autoclicker v 1.1", parent=fl)
oImage = QImage("pexels-rafael-guajardo-604671.jpg")
oImage = oImage.scaled(QSize(200,200))
name.setStyleSheet("QLabel"
                  "{"
                  "color: darkred;"
                  "}"

                )


manual.setStyleSheet("QPushButton"
                     "{"
                     "background-color:" + look.manualbutton + ";"
                     "}"
                     "QPushButton::pressed"
                     "{"
                     "background-color:" + look.manualbuttonpressed + ";"
                     "}"

                    )

minecraft.setStyleSheet("QPushButton"
                       "{"
                        "background-color:" + look.minecraftbutton + ";"
                        "}"
                         "QPushButton::pressed"
                        "{"
                        "background-color :" + look.minecraftbuttonpressed + ";"
                        "}"

                    )




settings.setStyleSheet("QPushButton"
                       "{"
                        "background-color:" + look.settingsbutton + ";"
                        "}"
                         "QPushButton::pressed"
                        "{"
                        "background-color :" + look.settingsbuttonpressed + ";"
                        "}"

                    )

exit.setStyleSheet("QPushButton"
                       "{"
                        "background-color:" + look.exitbutton + ";"
                        "}"
                         "QPushButton::pressed"
                        "{"
                        "background-color :" + look.exitbuttonpressed + ";"
                        "}"

                    )

click.setStyleSheet("QPushButton"
                "{"
                "background-color:" + look.clickbutton + ";"
                "}"
                "QPushButton::pressed"
                "{"
                "background-color :" + look.clickbuttonpressed + ";"
                "}"

               )



info.setStyleSheet("QPushButton"
                "{"
                "background-color:" + look.infobutton + ";"
                "width: 20px;"
                "}"
                "QPushButton::pressed"
                "{"
                "background-color : red;"
                "}"
             )


system.setStyleSheet("QLabel"
                "{"
                "color: darkred;"
                "}"
             )

on.setStyleSheet("QLabel"
                "{"
                "color: darkred;"
                "}"
             )

creator.setStyleSheet("QLabel"
                "{"
                "color: darkred;"
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
 try:
    os.system("python3 click-qt.py")
 except:
    os.system("python click-qt.py")


def appexit():
 quit()


def githubfunct():
 import webbrowser
 webbrowser.open("www.github.com/wowfilip999")


def man():
 manual = QtWidgets.QApplication([])
 f = QtWidgets.QWidget()

 c = QtWidgets.QLabel("test", parent=f)
 f.setGeometry(400, 400, 400, 400)
 f.setWindowTitle("test")

 f.show()

 manual.exec_()


def mc():
 os.system("python3 mc.py")

#font

try:
   f = open("bigfont-true.txt", "r")
   f.close()
   sz = "15"
except:
    sz = "13"


click.clicked.connect(lambda: clickf())
info.clicked.connect(lambda: infofunct())
settings.clicked.connect(lambda: set())
exit.clicked.connect(lambda: appexit())
github.clicked.connect(lambda: githubfunct())
manual.clicked.connect(lambda: man())
minecraft.clicked.connect(lambda: mc())

click.setFont(QFont("Arial", 13))
settings.setFont(QFont("Arial",13))
info.setFont(QFont("Arial", 13))
minecraft.setFont(QFont("Arial", 13))
exit.setFont(QFont("Arial", 13))
creator.setFont(QFont("italic", 11))
manual.setFont(QFont("italic", 15))
name.setFont(QFont("Arial", 20))
system.setFont(QFont("Italic", 15))
on.setFont(QFont("Italic", 15))



manual.move(1230, 650)
manual.resize(50, 50)
click.move(420, 140)
click.resize(500, 90)
minecraft.move(420, 230)
minecraft.resize(500 ,90)

name.move(530, 30)
settings.move(420, 320)
settings.resize(500, 90)
info.move(420, 410)
info.resize(500 ,90)
exit.resize(500 ,90)
exit.move(420, 500)
creator.move(70 ,670)
github.move(0, 650)
github.resize(50 ,50)
system.move(1145, 660)
on.move(1110, 660)
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