import tkinter
root = tkinter.Tk()
root.title("Prachi Calculator")

ws=root.winfo_screenwidth()
hs=root.winfo_screenheight()

w = 500
h = 400
x = int(ws/2 - w/2)
y = int(hs/2 - h/2)
#root.geometry(500x400+433+184)
data=str(w)+"x"+str(h)+"+"+str(x)+"+"+str(y)
root.geometry(data)

root.configure(background="#000000")
root.mainloop()