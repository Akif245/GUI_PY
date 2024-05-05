from tkinter import *
root=Tk()
def myfunc():
    print("Hiihihihi")

root.title("Menu")
root.geometry("600x300")

yourmenubar=Menu(root)
m1=Menu(yourmenubar,tearoff=0)
m1.add_command(label="file",command=myfunc)
m1.add_separator()
m1.add_command(label="save",command=myfunc)
m1.add_command(label="save as",command=myfunc)
m1.add_command(label="Help",command=myfunc)
m1.add_command(label="Exit",command=quit)

yourmenubar.add_cascade(label="file",menu=m1)

m2=Menu(yourmenubar)
m2.add_command(label="file",command=myfunc)
m2.add_separator()
m2.add_command(label="save",command=myfunc)
m2.add_command(label="save as",command=myfunc)
m2.add_command(label="Help",command=myfunc)
m2.add_command(label="Exit",command=quit)
yourmenubar.add_cascade(label="Edit",menu=m2)
# seperator adds a underline

root.config(menu=yourmenubar)
root.mainloop()