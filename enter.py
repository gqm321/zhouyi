from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText
import gx
win = Tk()
win.title('《周易》算卦-开始')
win.geometry('500x150')

var_Name = StringVar()
var_Name.set('')
var_Want = StringVar()
var_Want.set('')
def login() :
    global name,want
    name = var_Name.get()
    want = var_Want.get()
    _quit()
    gx.gxf(name,want)
def cancel() :
    name = var_Name.set('')
    want = var_Want.set('')
def _quit() :
    win.quit()
    win.destroy()

labname = Label(win,text='姓名：',width=80)
labwant = Label(win,text='您想要占卜的事物：',width=120)

entname = Entry(win,width=100,textvariable=var_Name)
entwant = Entry(win,width=100,textvariable=var_Want)

but_Ok = Button(win,text='占卜',command=login)
but_Cancel = Button(win,text='取消',command=cancel)
but_quit = Button(win,text='退出',command=_quit)

labname.place(x=20,y=10,width=80,height=30)
labwant.place(x=20,y=50,width=120,height=30)
entname.place(x=150,y=10,width=80,height=30)
entwant.place(x=150,y=50,width=300,height=30)
but_Ok.place(x=50,y=100,width=50,height=30)
but_Cancel.place(x=150,y=100,width=50,height=30)
but_quit.place(x=440,y=100,width=50,height=30)

win.mainloop()