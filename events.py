from tkinter import *
root=Tk()
def fcn(event):
    print(f"clicked !{event.x},{event.y}")
root.title("Events")
root.geometry("600x300")
btn=Button(root,text="Click Here")

# pack automatically place the item according to the space available
# btn.pack()

# grid works according to number of ows and column
btn.grid()
root.bind('<Button-1>',fcn)
root.bind('<Double-1>',quit)



root.mainloop()

