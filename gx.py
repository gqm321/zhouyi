from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText
import sgcode
def gxf(name,want) :
    gxw = Tk()
    gxw.title('《周易》算卦-卦象')
    gxw.geometry('500x400')

    labxm = Label(gxw,text='姓名：'+name)
    labthing = Label(gxw,text='占卜之事：'+want)

    textgx = ScrolledText(gxw)
    ans = sgcode.sg()
    textgx.insert('1.0',ans)
    textgx['state'] = 'disabled'

    labxm.place(x=20,y=10,width=80,height=30)
    labthing.place(x=20,y=40,width=300,height=30)
    textgx.place(x=20,y=70,width=300,height=300)

    gxw.mainloop()