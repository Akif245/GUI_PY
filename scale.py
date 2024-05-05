from tkinter import *
from tkinter import messagebox as msg
root=Tk()
root.geometry("444x444")
# myscale=Scale(root,from_=0,to=5550)
# myscale.pack()
def num():
    print(f"The number you have selected is {myscale2.get()} ?")
    msg.showinfo("The number is ",f"The number you have selected is {myscale2.get()}")
    
Label(root,text="select the number\n").pack()

myscale2=Scale(root,from_=0,to=100,orient=HORIZONTAL)
myscale2.pack()
Button(root,text="Done",command=num).pack()

# for default value
myscale2.set(10)
root.mainloop()