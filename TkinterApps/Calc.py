import tkinter
from tkinter import *

root=tkinter.Tk()
root.geometry("250x400+500+150")
root.resizable(0,0)
root.title("CALCULATOR")

btnrow1 = Frame(root,bg="#000000")
btnrow1.pack(expand = True, fill = "both",)

btnrow2 =  Frame(root)
btnrow2.pack(expand = True, fill = "both")

btnrow3 =  Frame(root,bg="#000000")
btnrow3.pack(expand = True, fill = "both")

btnrow4 =  Frame(root)
btnrow4.pack(expand = True, fill = "both")

btn1 = Button(
    btnrow1,
    text = 1,
    font = ("Verdana", 33),
)
btn1.pack(side = LEFT, expand = True, fill = "both")

root.mainloop()