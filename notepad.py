from tkinter import *
from tkinter import messagebox as msg
root=Tk()
root.geometry("444x555")
root.title("Note Pad")
scroolbar=Scrollbar(root)
scroolbar.pack(side=RIGHT,fill=Y)

text=Text(root,yscrollcommand=scroolbar.set)
text.pack(fill=BOTH)
scroolbar.config(command=text.yview)











root.mainloop()
