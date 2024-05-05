from tkinter import *
root=Tk()
def myfunc():
    print("Hiihihihi")



root.title("Menu")
root.geometry("600x300")
mymenu=Menu(root)
mymenu.add_command(label="file",command=myfunc)
mymenu.add_command(label="Exit",command=quit)

root.config(menu=mymenu)
root.mainloop()