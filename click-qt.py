from PyQt5 import QtWidgets
import customclick as clickspeed
import os
import time
import pyautogui
from PyQt5.QtGui import QFont
t = "slow"
class style:
  o = "lightgray"

click = QtWidgets.QApplication([])
form = QtWidgets.QWidget()
info = QtWidgets.QRadioButton("test", parent=form)
slow = QtWidgets.QPushButton(t, parent=form)
fast = QtWidgets.QPushButton("fast", parent=form)
custom = QtWidgets.QPushButton("custom", parent=form)
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
                   "background-color : red;"
                   "}"
               )

fast.setStyleSheet("QPushButton"
                   "{"
                   "background-color: lightgray;"
                   "width: 20px;"
                   "}"
                   "QPushButton::pressed"
                   "{"
                   "background-color : red;"
                   "}"
               )

custom.setStyleSheet("QPushButton"
                   "{"
                   "background-color: lightgray;"
                   "width: 20px;"
                   "}"
                   "QPushButton::pressed"
                   "{"
                   "background-color : red;"
                   "}"
               )

def customclick():
 if clickspeed.click == "click1":
   pyautogui.clicks()

 if clickspeed.click == "click2":
   pyautogui.clicks()
   pyautogui.clicks()

 if clickspeed.click == "click3":
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
  
 if clickspeed.click == "click4":
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()

 if clickspeed.click == "click5":
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()

 if clickspeed.click == "click6":
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()

 
 if clickspeed.click == "click7":
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
 
 if clickspeed.click == "click8":
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()

 if clickspeed.click == "click9":
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()

 if clickspeed.click == "click10":
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()

 if clickspeed.click == "click11":
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()

 if clickspeed.click == "click12":
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()

 if clickspeed.click == "click13":
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()

 if clickspeed.click == "click14":
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()

 if clickspeed.click == "click15":
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()

 if clickspeed.click == "click16":
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()


 if clickspeed.click == "click17":
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()

 if clickspeed.click == "click18":
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()


 if clickspeed.click == "click19":
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()

 if clickspeed.click == "click20":
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()

 if clickspeed.click == "click21":
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()
   pyautogui.click()








def c():
 pyautogui.click()
 time.sleep(0.1)
 pyautogui.click()
 time.sleep(0.1)
 pyautogui.click(clicks=2)
 time.sleep(0.1)
 pyautogui.click()
 time.sleep(0.1)
 pyautogui.click()
 time.sleep(0.1)
 pyautogui.click()



def slowmode():
 time.sleep(2)
 c()
 c()
 c()
 c()
 c()



def fastfunct():
 def f():
  pyautogui.click()
  time.sleep(0.2)
  pyautogui.click()
  pyautogui(clicks=2)
  pyautogui.click()
  pyautogui.click()
  pyautogui.click()


 f()
 f()




def infofunct():
 print("test")



slow.clicked.connect(lambda: slowmode())
fast.clicked.connect(lambda: fastfunct())
info.clicked.connect(lambda: infofunct())
custom.clicked.connect(lambda: customclick())


info.move(1, 10)
slow.resize(500, 90)
fast.resize(500, 90)
custom.resize(500, 90)
slow.move(400, 100)
fast.move(400, 190)
custom.move(400, 280)
text.setFont(QFont("Arial", 16))
slow.setFont(QFont("Arial", 13))
fast.setFont(QFont("Arial", 13))
custom.setFont(QFont("Arial", 13))
text.move(550, 40)
info.move(720, 55)
form.show() 

click.exec_()