from tkinter import *
root=Tk()
root.geometry("444x555")
root.title("image")
root.configure(background="blue")
root.wm_iconbitmap("2.ico")
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
print(f"{width}x{height}")
root.mainloop()


