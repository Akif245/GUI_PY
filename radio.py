from tkinter import *
from tkinter import messagebox as msg

root=Tk()
root.geometry("444x555")
root.title("Radio button")

var=IntVar()
def order():
    msg.showinfo("Order have receaved",f"you have ordered {var.get()}")
# var.set(1)
Label(root,text="what would you like to have ?",justify=LEFT,pady=15,font="lucida 19 bold").pack()

radio=Radiobutton(root,text="Dosa",variable=var,value=1,padx=15).pack(anchor="w")

radio=Radiobutton(root,text="jkjkj",variable=var,value=1,padx=15).pack(anchor="w")

radio=Radiobutton(root,text="wada",variable=var,value=3,padx=15).pack(anchor="w")

radio=Radiobutton(root,text="Idli",variable=var,value=4,padx=15).pack(anchor="w")

Button(root,text="Order Now",command=order).pack()


root.mainloop()