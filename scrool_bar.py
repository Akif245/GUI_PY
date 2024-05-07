from tkinter import *
from tkinter import messagebox as msg
root=Tk()
root.geometry("444x555")
root.title("Scrool Bar")
scroolbar=Scrollbar(root)

scroolbar.pack(side=RIGHT,fill=Y)
lst=Listbox(root,yscrollcommand=scroolbar.set)
global i
for i in range (1,301):    
    lst.insert(END,f"{i}")
lst.pack(fill=BOTH)

scroolbar.config(command=lst.yview)




root.mainloop()