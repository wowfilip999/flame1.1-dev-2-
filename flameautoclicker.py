from tkinter import *
from tkinter import messagebox
import pyautogui
import os
import time
import platform
operatingsystem = platform.system()
#import start


import flameconfig as cs  #if your have for python other command than python or python3
if cs.customcmd == "true":
  pycmd = input("enter command to launch python on your machine:")
  print("added command as " +  pycmd + ".." )

class thm:
  x = 100
  fnt = ("Arial", 15)



import thm_tk as tkinterthm

class classic:
  c = "black"
  b = "gray"
  bc = "black"

class d:
  if tkinterthm.theme == "experimental":
    c = "red"
    b = "black"
    bc = "black"

  if tkinterthm.theme == "classic":
    class classic:
      c = "black"
      b = "gray"
      bc = "black"

  try:
     if tkinterthm.theme == "custom":
       c = tkinterthm.custom.c 
       b = tkinterthm.custom.b 
       bc = tkinterthm.custom.bc

  except:
      pass


a = 0

class look:
  wid = 50


flametext = "FLAMEAUTOCLICKER"


root = Tk()
root.iconphoto(False, PhotoImage(file='fire_1f525.png')) 
root.geometry(cs.screen)
root.resizable(0, 0)


bg = PhotoImage(file = "fire_1f525.png")


messagebox.showinfo("lets start!", "thanks for downloading flame ")
root.configure(background="black")
root.resizable(0, 0)
root.title("flame1.1 >> tkinter gui")

def minecraft():
 pass

def click():

 def warn():
  print("test")



 #text = Label(set,text="Flame 1.0",bg="black",fg="red",height=5)
 timed = Button(set,text=show,bg="gray")
 click = Button(set,text="slow",bg="gray",command=slow,fg="black",borderwidth=3,width=45,height=3)
 slowinfo = Label(set,text="slow",bg="gray",command=slow,fg="red")
 faster = Button(set,text="faster",bg="gray",fg="black",command=faster,borderwidth=3,width=45,height=3)
 fast = Button(set,text="fast",bg="gray",fg="black",command=fast,borderwidth=3,width=45,height=3)
 super = Button(set,text="super",bg="gray",fg="black", command=super,borderwidth=3,width=45,height=3)
 mega = Button(set,text="mega",bg="gray",fg="black", command=mega,borderwidth=3,width=45,height=3)
 legit = Button(set,text="legit",bg="gray",fg="black",command=legit,borderwidth=3,width=45,height=3)
 timed = Button(set,text="timed",bg="gray",fg="black",command=timed,borderwidth=3,width=45,height=3)
 slowmore = Button(set,bg="gray",command=slowmore,height=3,width=0,borderwidth=1)

 text.pack()
 click.pack()
 #faster.pack()
 #fast.pack()
 #super.pack()
 #mega.pack()
 #legit.pack()
 #timed.pack()
 timed.place(x=200,y=100)

 slowmore.place(y=90,x=844)

 set.mainloop()



def style():
 style = Tk()
 style.attributes("-zoomed", True)
 style.title("flame1.1 >> select theme")
 style.configure(background="black")

 flametext = Label(style,bg="black",fg="red",text="FLAME THEMES")

 default = Button(style,width=50,height=2,text="default",borderwidth=2,bg="black",fg="red")

 flametext.config(font=("Italic", 20))
 default.place(x=400,y=200)
 flametext.place(x=500,y=0)
 style.mainloop()


def info():
 try:
   os.system("clear")
 except:
     sys = 2

 try:
    os.system("cls")
 except:
      p = 1

 if operatingsystem == "Windows":
   system = " your os : windows"

 if operatingsystem == "Linux":
   system = "your os : linux"

 else:
     system = "sorry can't detect your system :/" 

 a = ("35")
 info = Tk()
 info.configure(background="black")
 info.geometry("1500x1500")
 info.title("flame1.1 << informations")
 n = ("purple")
 inf = Label(info, text="INFORMATIONS:", bg="black", fg="red",width=a,font="italic")
 version = Button(info, text="version 1.1 development",fg=n,bg="black",width=a,font="italic")
 dev = Button(info, text="dev Filip Šiller",fg=n,bg="black",width=a,font="italic")
 module = Button(info, text="module pyautogui",fg=n,bg="black",width=a,font="italic")
 contact = Button(info, text="Discord : filip988#3501",fg=n,bg="black",width=a,font="italic")
 os = Button(info, text=system,fg=n,bg="black",width=a,font="italic")
 

 class p:
   t = "450"

 inf.place(x=300,y=50)
 version.place(x=p.t,y=150)
 dev.place(x=p.t,y=200)
 module.place(x=p.t,y=250)
 contact.place(x=p.t,y=300)
 os.place(x=p.t,y=350) 

 inf.config(font="Italic, 25")

 info.mainloop()

def settings():
 settings = Tk()
 if operatingsystem == "Linux":
  settings.attributes("-zoomed", True)
 if operatingsystem == "Windows":
   try:
      settings.state("zoomed")
   except:
       settings.attributes("-zoomed", True)

 settings.title("flame1.1 >> settings")
 settings.config(background="black")

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
  if cs.customcmd == "true":
    os.system(pycmd + " legitset.py")

  else:
      if operatingsystem == "Linux":
        os.system("python3 legitset.py")
      if operatingsystem == "windows":
        os.system("python legitset.py")

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
  timed.title("flame1.1")
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


 if tkinterthm.custom == "no":
   class classic:
     c = "black"
     b = "gray"
     bc = "black"

  # manage = Button(settings,text="enable extesion manager on start",width=45,height=3,borderwidth=3,command=legitset,fg=classic.c,bg=classic.b)
   #timed = Button(settings,text="timed",width=45,height=3,borderwidth=3,command=timed,fg=classic.c,bg=classic.b)
   #legit = Button(settings,text="legitset",width=45,height=3,borderwidth=3,command=legitset,fg=thm.c,bg=classic.b)
   #clear = Button(settings,text="clear",width=45,height=3,borderwidth=3,command=clear,fg=classic.c,bg=classic.b)


 #legit.pack()
 #manage.pack()
 #timed.pack()
 #clear.pack()
 #settings.mainloop()


def help():
 help = Tk()
 help.geometry("1500x1500")
 help.configure(background="black")
 help.title("flame1.1 >> help")


 def close():
  help.destroy()



 close = Button(help, text="close",command=close,borderwidth=2,height=2,width=7)
 click = Label(help, text="working on this..",bg="black",fg="red",font="italic")
 click.place(x=5,y=40)
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
  import time
  from pynput import keyboard

  def on_press(key):
     try:
         print('alphanumeric key {0} pressed'.format(
            key.char))
     except AttributeError:
         print('special key {0} pressed'.format(
            key))

  def on_release(key):
    print('{0} released'.format(
      key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

    if key == keyboard.Key.up:
      pyautogui.click()
      time.sleep(0.2)
      pyautogui.click()
      time.sleep(0.2)
      pyautogui.click()
      time.sleep(0.2)
      pyautogui.click()
      time.sleep(0.2)
      pyautogui.click()
      time.sleep(0.2)
      pyautogui.click()
      time.sleep(0.2)

   # Collect events until released
  with keyboard.Listener(
      on_press=on_press,
      on_release=on_release) as listener:
     listener.join()

# ...or, in a non-blocking fashion:
  listener = keyboard.Listener(
     on_press=on_press,
     on_release=on_release)
  listener.start()


 def custom():
  import time
  from pynput import keyboard

  def on_press(key):
     try:
         print('alphanumeric key {0} pressed'.format(
            key.char))
     except AttributeError:
         print('special key {0} pressed'.format(
            key))

  def on_release(key):
    print('{0} released'.format(
      key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

    if key == keyboard.Key.down:
      optiongui = Tk()
      optiongui.title("flame1.1 >> click >> custom settings")
      optiongui.config(background="black")
      optiongui.geometry("500x500")

      class k:
        i = "black"
        r = "red"
        p = "300"
      
      def spd():
       spde = Tk()
       spde.title("speed options")
       spde.geometry("500x500")
       
       
       spdenter = Entry(spde,value)
       spdenter.insert(END, 'You email here')


       spdenter.place(x=300,y=100)

       spde.mainloop()

      def bind():
       pass

      tx = Label(optiongui,text="settings",bg=k.i,fg=k.r)
      bind = Button(optiongui,text="bind",bg=k.i,fg=k.r,width=12,height=3,command=bind)
      speed = Button(optiongui,text="speed",bg=k.i,fg=k.r,width=12,height=3,command=spd)
      
      tx.place(x=20,y=10)
      tfnt = ("Times", 16)
      tx.config(font=tfnt)
      speed.place(x=k.p,y=90)
      bind.place(x=k.p,y=20)
      optiongui.mainloop()

    if key == keyboard.Key.up:
      pyautogui.click()
      time.sleep(00.10)
      pyautogui.click()
      pyautogui.click()
      time.sleep(00.10)
      pyautogui.click()
      time.sleep(0.1)

   # Collect events until released
  with keyboard.Listener(
      on_press=on_press,
      on_release=on_release) as listener:
     listener.join()


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
 set.title("flame1.1 >> click")
 set.geometry("1500x1500")
 set.configure(background="black")

 #import option as opti
 
 class pl2:
   p = "410"
   w = 55

 text = Label(set,text="CLICK MODES",bg="black",fg="red")
 slow = Button(set,text="slow",bg="black",command=slow,fg="red",width=pl2.w,height=4)
 custom = Button(set,text="custom",width=pl2.w,height=4,bg="black",fg="red",command=custom)
 fast = Button(set,text="fast",bg="black",fg="red",borderwidth=3,width=pl2.w,height=4)
 
 justconfig = ("Italic", 17)
 text.config(font=justconfig)
 #customsettings.place(x=500,y=100)
 text.place(x=550,y=40)
 custom.place(x=410,y=200)
 slow.place(x=pl2.p,y=285)
 #faster.pack()
 fast.place(x=pl2.p,y=370)
 #super.pack()
 #mega.pack()
 #legit.pack()
 #mcaim.pack()


 set.mainloop()


def warn():
 print("test")


import tk_theme as theme
try:
   stylebtn = classic.b
except:
    stylebtn = classic.b


try:
  colortext = tkinterthm.custom.c
except:
    colortext = classic.c

if tkinterthm.custom == "yes":
  if tkinterthm.custom.useinmenu == "no":
    del colortext
    del stylebtn
    colortext = "black"
    stylebtn = "gray"
  
if tkinterthm.custom.useinmenu == "yes":
  pass

else:
  del stylebtn
  stylebtn = "gray"


label1 = Label(root, image=bg,bg="black")
text = Label(root, text=flametext,fg="red",bg="black",height=5,font="italic",cursor="cross")
click = Button(root, text="click",command=click,fg="black",width=theme.wid,height=3,bg="gray",borderwidth=3,cursor="cross")
warn = Button(root, text="warn",command=warn,bg="gray",fg="black",width=theme.wid,height=3,borderwidth=3,cursor="cross")
minecraft = Button(root, text="minecraft",command=minecraft,bg="gray",fg="black",width=theme.wid,height=3,borderwidth=3,cursor="cross")
info = Button(root, text="info",command=info,bg="gray",fg="black",width=theme.wid,height=3,borderwidth=3,cursor="cross")
style = Button(root, text="theme",command=style,bg=stylebtn,fg=colortext ,width=theme.wid,height=3,borderwidth=3,cursor="cross")
exit = Button(root, text="exit",command=exit,bg="gray",fg="black",width=theme.wid,height=3,borderwidth=3,cursor="cross")
creator  = Label(root, text="by wowfilip999",bg="black",fg="red")
settings = Button(root,text="settings",bg="gray",fg="black",command=settings,borderwidth=3,width=theme.wid,height=3,cursor="cross")
system = Label(root,text=operatingsystem,bg="black",fg="red")

help  = Button(root, text="?",command=help,bg="white",fg="black",width=1,height=1,borderwidth=2)



#font 
textconf = ("Times", 25)
helpconf = ("Arial", 14)
creatorconf= ("Sans", 13)
systemconf = ("Sans", 14)
infoconf = ("Times", 12)
settingsconf = ("Times", 12)
exitconf = ("Times", 12)
styleconf = ("Times", 12)
minecraftconf = ("Times", 12)
fontconf = (theme.font, theme.size)

settings.config(font=fontconf)
minecraft.config(font=fontconf)
style.config(font=fontconf)
warn.config(font=fontconf)
exit.config(font=fontconf)
help.config(font=helpconf)
system.config(font=systemconf)
info.config(font=fontconf)
click.config(font=fontconf)
creator.config(font=creatorconf)
text.config(font=theme.textconf)

#---------------

text.pack()
click.pack()
warn.pack()
minecraft.pack()
info.pack()
style.pack()
settings.pack()
exit.pack()
label1.place(y=10, x=810)
system.place(y=666,x= 1150)
help.place(x=1245,y=660)
creator.place(x=5,y=670)


root.mainloop()
