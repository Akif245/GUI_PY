from tkinter import *
root=Tk()
root.geometry("644x900")
root.title("Calculator")

def click(e):
    globals=strvar
    text=e.widget.cget("text")
    print(text)
    if text=="=":
        if strvar.get().isdigit():
            value=int(strvar.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                value="Error"
        strvar.set(value)
        strvar.update()
    elif text=="C":
        strvar.set("")
        screen.update()
    else:
        strvar.set(strvar.get()+text)
        screen.update()

Label(root,text="Welcome to my Calculator",font="lucida 25 bold").pack()
strvar=StringVar()
strvar.set("")

screen=Entry(root,textvariable=strvar,font="lucida 25 bold")
screen.pack(fill=X,ipady=10,padx=10,pady=5)

f1=Frame(root,bg="grey")
btn=Button(f1,text="9",font="lucida 25 bold",padx=20,pady=10)
btn.pack(side=LEFT,padx=10,pady=10)
btn.bind("<Button-1>",click)

btn=Button(f1,text="8",font="lucida 25 bold",padx=20,pady=10)
btn.pack(side=LEFT,padx=10,pady=10)
btn.bind("<Button-1>",click)


btn=Button(f1,text="7",font="lucida 25 bold",padx=20,pady=10)
btn.pack(side=LEFT,padx=10,pady=10)
btn.bind("<Button-1>",click)
f1.pack()


f1=Frame(root,bg="grey")
btn=Button(f1,text="6",font="lucida 25 bold",padx=20,pady=10)
btn.pack(side=LEFT,padx=10,pady=10)
btn.bind("<Button-1>",click)

btn=Button(f1,text="5",font="lucida 25 bold",padx=20,pady=10)
btn.pack(side=LEFT,padx=10,pady=10)
btn.bind("<Button-1>",click)

btn=Button(f1,text="4",font="lucida 25 bold",padx=20,pady=10)
btn.pack(side=LEFT,padx=10,pady=10)
btn.bind("<Button-1>",click)
f1.pack()

f1=Frame(root,bg="grey")
btn=Button(f1,text="3",font="lucida 25 bold",padx=20,pady=10)
btn.pack(side=LEFT,padx=10,pady=10)
btn.bind("<Button-1>",click)

btn=Button(f1,text="2",font="lucida 25 bold",padx=20,pady=10)
btn.pack(side=LEFT,padx=10,pady=10)
btn.bind("<Button-1>",click)

btn=Button(f1,text="1",font="lucida 25 bold",padx=20,pady=10)
btn.pack(side=LEFT,padx=10,pady=10)
btn.bind("<Button-1>",click)
f1.pack()

f1=Frame(root,bg="grey")
btn=Button(f1,text="0",font="lucida 25 bold",padx=23,pady=10)
btn.pack(side=LEFT,padx=10,pady=10)
btn.bind("<Button-1>",click)

btn=Button(f1,text="+",font="lucida 25 bold",padx=20,pady=10)
btn.pack(side=LEFT,padx=10,pady=10)
btn.bind("<Button-1>",click)

btn=Button(f1,text="-",font="lucida 25 bold",padx=20,pady=10)
btn.pack(side=LEFT,padx=10,pady=10)
btn.bind("<Button-1>",click)

f1.pack()

f1=Frame(root,bg="grey")
btn=Button(f1,text="*",font="lucida 25 bold",padx=20,pady=10)
btn.pack(side=LEFT,padx=10,pady=10)
btn.bind("<Button-1>",click)

btn=Button(f1,text="/",font="lucida 25 bold",padx=20,pady=10)
btn.pack(side=LEFT,padx=10,pady=10)
btn.bind("<Button-1>",click)

btn=Button(f1,text="=",font="lucida 25 bold",padx=20,pady=10)
btn.pack(side=LEFT,padx=10,pady=10)
btn.bind("<Button-1>",click)
f1.pack()

f1=Frame(root,bg="grey")
btn=Button(f1,text=".",font="lucida 25 bold",padx=20,pady=10)
btn.pack(side=LEFT,padx=10,pady=10)
btn.bind("<Button-1>",click)

btn=Button(f1,text="%",font="lucida 25 bold",padx=20,pady=10)
btn.pack(side=LEFT,padx=10,pady=10)
btn.bind("<Button-1>",click)

btn=Button(f1,text="C",font="lucida 25 bold",padx=16,pady=10)
btn.pack(side=LEFT,padx=10,pady=10)
btn.bind("<Button-1>",click)
f1.pack()







root.mainloop()