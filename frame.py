from tkinter import *
root=Tk()
root.geometry("400x400")
a=10
b=20
def hello():
    print("Button pressed")

f1=Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,fill="y")
l=Label(f1,text="hiii")
l.pack(pady=20)
f2=Frame(root,bg="grey",borderwidth=8,relief=SUNKEN)
f2.pack(side=TOP,fill="x")
l1=Label(f2,text="Welcome to my GUI",fg="red")
l1.pack()
f3=Frame(root,borderwidth=1,relief=SUNKEN,bg="grey")
f3.pack(side=LEFT,anchor=NW)
btn=Button(f3,fg="red",text="Click here")
btn.pack(padx=20)
f4=Frame(root,borderwidth=1,relief=SUNKEN,bg="grey")
f4.pack(side=LEFT,anchor=NW)
btn=Button(f4,fg="red",text="Click here")
btn.pack(padx=20)
f5=Frame(root,borderwidth=1,relief=SUNKEN,bg="grey")
f5.pack(side=LEFT,anchor=NW)
btn=Button(f5,fg="red",text="Click here",command=hello)
btn.pack(padx=20)
# to give command to button line 22

root.mainloop()