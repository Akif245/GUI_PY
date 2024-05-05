from tkinter import *
from tkinter import messagebox as msg

root=Tk()
def myfunc():
    print("Hiihihihi")
def help():
    print("i Will help u")
    msg.showinfo("Help","I wil help u")
    
# showinfo is likely an an alert  

root.title("Menu")
root.geometry("600x300")

yourmenubar=Menu(root)
m1=Menu(yourmenubar,tearoff=0)
m1.add_command(label="file",command=myfunc)
m1.add_command(label="Exit",command=quit)

yourmenubar.add_cascade(label="file",menu=m1)
root.config(menu=yourmenubar)
def rateus():
    a=msg.askquestion("How was ur experience ?","Was ur experience good ?")
    print(a)
m2=Menu(yourmenubar,tearoff=0)
m2.add_command(label="Help",command=help)
m2.add_command(label="rate",command=rateus)
m2.add_command(label="Exit",command=quit)
yourmenubar.add_cascade(label="Help",menu=m2)
root.mainloop()
