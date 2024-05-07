from tkinter import *
from tkinter import messagebox as msg
root=Tk()
root.geometry("444x555")
root.title("List in Tkinter")
def add ():
    global i
    lst.insert(ACTIVE,f"{i}")
    i+=1
i=0
lst=Listbox(root)
lst.insert(END,"First item of this list ")
lst.pack()
Button(root,text="Add item",command=add).pack()








root.mainloop()