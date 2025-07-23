from tkinter import *
import random


root=Tk()

root.title("Password generator")
root.geometry("600x500")
root.config(bg="#1e1e1e")
root.resizable(False,False)

f=("Segoe UI", 18, "bold")

def pass_gen():
    lett="abcdefghijklmnopqrstuvwxyz"
    num="0123456789"
    sym="!@#$%^&*()_-"

    combine=lett+num+sym
    len=int(ent.get())
    
    password=""

    for i in range(len):
        ran=random.choice(combine)
        password=password+ran
    if len<=8:
        output.configure(text="Generated password is:  "+password)
    else:
        output.configure(text="Password will be too long..!!")
    



lab=Label(root,text="Enter length of password:", font=f,fg="white", bg="#1e1e1e")
ent=Entry(root,font=f,justify="center", bg="#2c2c2c", fg="white", insertbackground="white")
butt=Button(root,text="GENERATE..!!",font=f, bg="#00b894", fg="white", activebackground="#00cec9",command=pass_gen)
output=Label(root,font=f, fg="cyan", bg="#1e1e1e")

lab.place(x=130,y=100)
ent.place(x=145,y=200)
butt.place(x=205,y=300)
output.place(x=110,y=410)

root.mainloop()


            
