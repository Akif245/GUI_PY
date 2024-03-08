from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.geometry("700x600")
# image = Image.open("1.jpg")
# photo = ImageTk.PhotoImage(image)
# label = Label(image=photo)
root.title("My GUI")
text=Label(text='''In literary theory, a text is any object that can be "read", 
           \nwhether this object is a work of literature, a street sign, \nan 
           arrangement of buildings on a city block, or styles of clothing. I
           t is a coherent set of signs \nthat transmits some kind of informat
           ive message.''',fg="black",pady=200,font="Arial 19 bold")
# label.pack()
text.pack(side="top",anchor="sw",fill="x")
text.pack()
f1 =Frame(root,bg="red")
f1.pack()
root.mainloop()