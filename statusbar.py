from tkinter import *
import time as tm
root=Tk()
root.geometry("444x555")
root.title("Status Bar")

def upload():
    strg.set("Busy")
    sbar.update()
    tm.sleep(2)
    strg.set("Ready now")

    
strg=StringVar()
strg.set("Ready")
sbar=Label(root,textvariable=strg,relief=SUNKEN,anchor=W)
sbar.pack(side=BOTTOM,fill=X)
Button(root,text=" Click to Upload",command=upload).pack()

# print(tm.ctime()) 
root.mainloop()