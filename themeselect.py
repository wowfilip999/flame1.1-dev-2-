from tkinter import *
themeselect = Tk()
themeselect.geometry("600x600")

class main:
  fnt = ("Arial", 16)
  wfnt = ("Italic", 13)
  pl = "200"
  plw = "190"

def white():
 os.patch("themes")

def default():
 themeselect.quit()

text = Label(themeselect,text="select theme")
white = Button(themeselect,text="white",command=white,width=17,height=3)
default = Button(themeselect,text="default",command=default,width=17,height=3)


text.config(font=main.fnt)
white.config(font=main.wfnt)
default.config(font=main.wfnt)

text.place(x=main.pl,y=20)
white.place(x=main.plw,y=70)
default.place(x=180,y=150)

themeselect.mainloop()

