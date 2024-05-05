from tkinter import *
root=Tk()





def getvals():
    print("Submitting form")

    print(f"{nameval.get(), mobileval.get(), genderval.get(), payval.get(), foodserviceval.get()} ")



    with open("records.txt", "a") as f:
        f.write(f"{nameval.get(), mobileval.get(), genderval.get(),payval.get(), foodserviceval.get()}\n ")

root.geometry("644x344")
Label(root,text="Welcome", font="Arial 13 bold",pady=15).grid(row=0,column=3)
name=Label(root,text="Enter your name")
mobile=Label(root,text="Enter mobile number")
gender=Label(root,text="Enter your gender")
pay=Label(root,text="payment mode")



    

name.grid(row=1,column=2)
mobile.grid(row=2,column=2)
gender.grid(row=3,column=2)
pay.grid(row=4,column=2)

nameval=StringVar()
genderval=StringVar()
mobileval=StringVar()
payval=StringVar()
#*********************  this is a check box **************************
foodserviceval=IntVar()


namevalentry=Entry(root,textvariable=nameval)
genderentry=Entry(root,textvariable=genderval)
mobilevalentry=Entry(root,textvariable=mobileval)
payvalentry=Entry(root,textvariable=payval)

namevalentry.grid(row=1,column=3)
genderentry.grid(row=2,column=3)
mobilevalentry.grid(row=3,column=3)
payvalentry.grid(row=4,column=3)

# creating a check box
foodservice=Checkbutton(text="Want to prebook your meals ?",variable=foodserviceval)
foodservice.grid(row=6,column=3)
# Button
Button(text="Submit",command=getvals).grid(row=7,column=3)











root.mainloop()