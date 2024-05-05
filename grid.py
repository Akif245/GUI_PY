from tkinter import *
root=Tk()
root.geometry("655x333")
def getval():
    print(userval.get())
    print(passval.get())
# grid use 

user=Label(root,text="User Name")
password=Label(root,text="Password")
user.grid()
password.grid()
#  Variable Classes in tkinter

#************************ BooleanVar,IntVar,StringVar,DoubleVar*********************
userval=StringVar()
passval=StringVar()
userentry=Entry(root,textvariable=userval)
passentry=Entry(root,textvariable=passval,show="*")
userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)
Button(text="Submit",command=getval).grid()








root.mainloop()



