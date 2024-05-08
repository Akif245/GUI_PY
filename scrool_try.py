from tkinter import *
root=Tk()
root.geometry("444x555")
root.title("Scrool try")
scrool=Scrollbar(root)
scrool.pack(side=RIGHT,fill=Y)
# lst=Listbox(root,yscrollcommand=scrool.set)
# for i in range (1,301):    
#     lst.insert(END,f"{i}")
text=Text(root,yscrollcommand=scrool.set)
text.pack(fill=BOTH)
# lst.pack(fill=BOTH)
scrool.config(command=text.yview)
    
root.mainloop()