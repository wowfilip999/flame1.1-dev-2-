from tkinter import *
import datetime 
import os
import random
import time
import start
a = 0

flametext = "flameautoclicker"

x = datetime.datetime.now()
ran = random.randint(2, 20)
if ran == 6:
  class secret:
    g=("1500x1500")
   

  e = Tk()
  e.geometry(secret.g)
  e.title("secret")

  msg = Label(e,text="your found secret!",font="bold")
  o = Label(e,text="send this dev and get speacial flame version(and send screenshot) --> 47227f")
  msg.place(x=400,y=300)
  o.place(x=500,y=500)
  e.mainloop()
  


os.system("python3 conf7.py")
import pyautogui
f = open("log.txt", "a")
f.write((str)(x))
f.write("start\n")
f.close()

root = Tk()
root.geometry("1500x1500")
root.title("Flame 1.0")
root.configure(background="black")

def minecraft():
 mc = Tk()
 mc.geometry("1500x1500")
 mc.configure(background="black")
 mc.title("Flame")
 
 def mcserver():
  confing = Tk()
  confing.configure(background="black")


 def server1config():
  os.system("dir")


 mc = Button(mc,text="mc confing",command=mcserver,width=45,height=3)
 mc.pack()

 mc.mainloop()

def click():

 def warn():
  print("test")


 text = Label(set,text="Flame 1.0",bg="black",fg="red",height=5)
 slow = Button(set,text="slow",bg="gray",command=slow,fg="black",borderwidth=3,width=45,height=3)
 slowinfo = Label(set,text="slow",bg="gray",command=slow,fg="red")
 faster = Button(set,text="faster",bg="gray",fg="black",command=faster,borderwidth=3,width=45,height=3)
 fast = Button(set,text="fast",bg="gray",fg="black",command=fast,borderwidth=3,width=45,height=3)
 super = Button(set,text="super",bg="gray",fg="black", command=super,borderwidth=3,width=45,height=3)
 mega = Button(set,text="mega",bg="gray",fg="black", command=mega,borderwidth=3,width=45,height=3)
 legit = Button(set,text="legit",bg="gray",fg="black",command=legit,borderwidth=3,width=45,height=3)
 timed = Button(set,text="timed",bg="gray",fg="black",command=timed,borderwidth=3,width=45,height=3)
 slowmore = Button(set,bg="gray",command=slowmore,height=3,width=0,borderwidth=1)

 text.pack()
 slow.pack()
 faster.pack()
 fast.pack()
 super.pack()
 mega.pack()
 legit.pack()
 timed.pack()
 slowmore.place(y=90,x=844)

 set.mainloop()



def style():
 import os
 os.system("python3 style.py")



def info():
 try:
   os.system("clear")
 except:
     sys = 2

 try:
    os.system("cls")
 except:
      p = 1

 if sys == 1:
   system = " your os : windows"

 if sys == 2:
   system = "your os : linux"

 a = ("20")
 info = Tk()
 info.configure(background="black")
 info.geometry("1500x1500")
 info.title("Flame")
 n = ("purple")
 inf = Label(info, text="INFORMATIONS:", bg="black", fg="red",width=a,font="italic")
 version = Label(info, text="version 1.0 beta",fg=n,bg="black",width=a,font="italic")
 dev = Label(info, text="dev Filip Šiller",fg=n,bg="black",width=a,font="italic")
 module = Label(info, text="module pyautogui",fg=n,bg="black",width=a,font="italic")
 contact = Label(info, text="Discord : filip999#2904",fg=n,bg="black",width=a,font="italic")
 os = Label(info, text=system,fg=n,bg="black",width=a,font="italic")

 inf.pack()
 version.pack()
 dev.pack()
 module.pack()
 contact.pack()
 os.pack()

def settings():
 settings = Tk()
 settings.geometry("1500x1500")
 settings.title("settings")

 def manage():
  f = open("conf7.py", "w")
  f.write("import os")
  f.write("os.chdir('extesions\n')")
  f.write("os.system('python3 manage.py')")
  f.close()
  confirm = Tk()
  confirm.title("restart flameautoclicker")

  def ok():
   os.system("python3 flameautoclicker.py")
   root.destroy()

  m = Button(confirm,text="ok",command=ok)
  m.pack()
  confirm.mainloop()

 def legitset():
  os.system("python3 legitset.py")

 def timed():
  def op1():
   f = open("timed.py", "w")
   f.write("import time\ntime.sleep(3)")

  def  op2():
   f = open("timed.py", "w")
   f.write("import time\ntime.sleep(4)")

  def op3():
   f = open("timed.py", "w")
   f.write("import time\ntime.sleep(5)")
  def op4():
   f = open("timed.py", "w")
   f.write("import time\ntime.sleep(5)")
  
  def test():
   a + 1
   print(a)


  def default():
   f = open("timed.py", "w")
   f.write("import time\ntime.sleep(2)")


  import time
  try:
      f = open("timed.py")
  except IOError:
        f = open("timed.py", "w")
        f.close()
  time.sleep(1)
  timed = Tk()
  timed.title("Flame")
  timed.configure(background="black")
  timed.geometry("1500x1500")

  jay = Label(timed, text="Flame 1.0",fg="red",bg="black",width=45,height=5)
  default = Button(timed, bg="gray",text="reset",command=default,width=45,borderwidth=3,height=3)
  option1 = Button(timed, bg="gray",text="3 sec",command=op1,width=45,borderwidth=3,height=3)
  option2 = Button(timed, bg="gray", text="4 sec",command=op2,width=45,borderwidth=3,height=3)
  option3 = Button(timed, bg="gray", text="5 sec",command=op3,width=45,borderwidth=3,height=3)
  test = Button(timed, bg="gray", text="test",command=test,width=45,borderwidth=3,height=3)

  jay.pack()
  default.pack()
  option1.pack()
  option2.pack()
  option3.pack()
  test.pack()
  timed.mainloop()


 def clear():
  os.remove("log.txt")
  f = open("log.txt", "w")
  f.close()


 manage = Button(settings,text="enable extesion manager on start",width=45,height=3,borderwidth=3,command=legitset)
 timed = Button(settings,text="timed",width=45,height=3,borderwidth=3,command=timed)
 legit = Button(settings,text="legitset",width=45,height=3,borderwidth=3,command=legitset)
 clear = Button(settings,text="clear",width=45,height=3,borderwidth=3,command=clear)

 legit.pack()
 manage.pack()
 timed.pack()
 clear.pack()
 settings.mainloop()


def help():
 help = Tk()
 help.geometry("1500x1500")
 help.configure(background="black")
 help.title("flame >> help")


 def close():
  help.destroy()



 close = Button(help, text="close",command=close,borderwidth=2,height=2,width=7)
 click = Label(help, text="CLICK",bg="black",fg="red",font="italic")
 clickinfo = Label(help, text="when press this button wiew click modes",bg="black",fg="red",font="arial")
 clickinfo2 = Label(help, text="modes:",bg="black",fg="red",font="arial")
 clickinfo3 = Label(help, text="click slow unknow cps",bg="black",fg="red",font="arial")
 click.place(x=5,y=40)
 clickinfo.place(x=5,y=70)
 clickinfo2.place(x=5,y=100)
 clickinfo3.place(x=5,y=130)
 close.place(x=1205,y=0)
 help.mainloop()



def click():
 def legit():
  os.system("python3 timed.py")
  while True:
    os.system("python3 conf3.py")


 def mcserver():
  try:
     os.system("python3 minecraftconfig.py") 
  except:
      messagebox.showinfo("test", "test")

 def mega():
  import pyautogui
  os.system("python3 timed.py")
  while True:
    pyautogui.click(clicks=13)
    time.sleep(0.2)

 def legit():
  while True:
    os.system("python3 conf3.py")

 def super():
  import pyautogui
  os.system("python3 timed.py")
  while True:
    pyautogui.click(clicks=14)


 def faster():
  os.system("python3 timed.py")
  while True:
    pyautogui.click(clicks=7)
    time.sleep(0.1)
    pyautogui.click(clicks=2)


 def fast():
  os.system("python3 timed.py")
  while True:
    pyautogui.click(clicks=9)
    time.sleep(0.1)



 def exit():
  root.destroy()

 def mcaim():
  while True:
    pyautogui.move(7,25)
    pyautogui.click(clicks=1)
    pyautogui.move(0,25)
    pyautogui.click(clicks=1)
    pyautogui.move(7,25)
    pyautogui.click(clicks=1)
    pyautogui.move(0,25)
    pyautogui.click(clicks=1)
    pyautogui.move(7,25)
    time.sleep(1)


 
 def slow():
  os.system("python3 timed.py")
  while True:
    pyautogui.click()
    time.sleep(0.8)
    pyautogui.click()
    pyautogui.click()

 def test():
  import time
  os.system("python3 timed.py")
  while True:
    pyautogui.click()
    time.sleep(2)
    pyautogui.click()



 def moresettings():
  class set:
    a  = ("50x100")



  more = Tk()
  more.geometry("1500x1500")
  more.title("Flame")
  t = Button(more, text="legit")
  t.pack()

 def slowmore():
  print("test")


 set = Tk()
 set.title("settings")
 set.geometry("1500x1500")
 set.configure(background="black")

 text = Label(set,text="Flame 1.0",bg="black",fg="red",height=5)
 slo = Button(set,text="slow",bg="gray",command=slow,fg="black",borderwidth=3,width=45,height=3)
 faster = Button(set,text="faster",bg="gray",fg="black",command=faster,borderwidth=3,width=45,height=3)
 fast = Button(set,text="fast",bg="gray",fg="black",command=fast,borderwidth=3,width=45,height=3)
 super = Button(set,text="super",bg="gray",fg="black", command=super,borderwidth=3,width=45,height=3)
 mega = Button(set,text="mega",bg="gray",fg="black", command=mega,borderwidth=3,width=45,height=3)
 legit = Button(set,text="legit",bg="gray",fg="black",command=legit,borderwidth=3,width=45,height=3)
 mcaim = Button(set,text="mcaim",bg="gray",fg="black",command=mcaim,borderwidth=3,width=45,height=3)
 slowmore = Button(set,bg="gray",command=slowmore,height=3,width=0,borderwidth=1)

 text.pack()
 slo.pack()
 faster.pack()
 fast.pack()
 super.pack()
 mega.pack()
 legit.pack()
 mcaim.pack()


 set.mainloop()


def warn():
 print("test")

x = datetime.datetime.now()
datum = Label(root,text=x)
text = Label(root, text=flametext,fg="red",bg="black",height=5,font="italic",cursor="cross")
click = Button(root, text="click",command=click,fg="black",width=45,height=3,bg="gray",borderwidth=3,cursor="cross")
warn = Button(root, text="warn",command=warn,bg="gray",fg="black",width=45,height=3,borderwidth=3,cursor="cross")
minecraft = Button(root, text="minecraft",command=minecraft,bg="gray",fg="black",width=45,height=3,borderwidth=3,cursor="cross")
info = Button(root, text="info",command=info,bg="gray",fg="black",width=45,height=3,borderwidth=3,cursor="cross")
style = Button(root, text="style",command=style,bg="gray",fg="black",width=45,height=3,borderwidth=3,cursor="cross")
exit = Button(root, text="exit",command=exit,bg="gray",fg="black",width=45,height=3,borderwidth=3,cursor="cross")
creator  = Label(root, text="by wowfilip999",bg="black",fg="red")
settings = Button(root,text="settings",bg="gray",fg="black",command=settings,borderwidth=3,width=45,height=3,cursor="cross")
help  = Button(root, text="?",command=help,bg="white",fg="black",width=1,height=1,borderwidth=2)

text.pack()
click.pack()
warn.pack()
minecraft.pack()
info.pack()
style.pack()
settings.pack()
exit.pack()
help.place(x=1250,y=670)
creator.place(x=5,y=670)

import os
os.chdir("extesions")
try:
    os.system("python3 run.py")
    f = open("extesion1.py")
except IOError:
    warning = Label(root,text="no extesions loaded",fg="red",bg="black")
    warning.place(x=1100,y=675)



root.mainloop()
