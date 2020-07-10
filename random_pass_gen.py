import random
from tkinter import *
from tkinter.ttk import *
import tkinter as tk


def fle():
    f = open("mypass.txt", "a")
    m = t.get()
    f.write(m + "\n")

def low():
    entry.delete(0,END)

    length = var1.get()
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    spl = "!@#$%^&*()~"
    password = ""
     

    #if password cotains uppercase and lowercase letters
    if var.get()==1:
        for i in range(0,length):
            password = password + random.choice(lower + upper + digits)
        return password
    
    elif var.get()==2:
        for i in range(0,length):
            password += random.choice(lower + upper + digits + spl)
        return password
    else:
        for i in range(0,length):
            password += random.choice(lower + upper)
        return password
    
    # function for generation of password
def generate():
    password1 = low()
    entry.insert(15,password1)

    # Main Function

    # GUI window 
root=Tk()
var=IntVar()
var1=IntVar()
t = tk.StringVar()
# Title of GUI Window
root.title("Random Password Generator")

# create entry and label to show generated password
password=Label(root,text="Password")
password.grid(row=0)
entry=Entry(root, textvariable=t)

entry.grid(row=0,column=1)

# Creating Label for lenght of password
clabel=Label(root,text="Length")
clabel.grid(row=1)

# Generate Button
generate_btn=Button(root,text="Generate",command=generate)
generate_btn.grid(row=0,column=2)

# Radio Button for deciding type of password, default none
radio_dig=Radiobutton(root,text="Include Digits",variable=var,value=1)
radio_dig.grid(row=1,column=2,sticky="E")

radio_spl=Radiobutton(root,text="Include Symbols",variable=var,value=2)
radio_spl.grid(row=1,column=3,sticky="E")

combo=Combobox(root,textvariable=var1)

combo['values']=(8,9,10,11,12,13,14,15,16,17,18,19,20,22,24,26,28,30,"Length")

combo.current(0)

combo.bind('<<ComboboxSelected>>')
combo.grid(row=1,column=1)

Savefile=Button(root, text = 'Save as a file', command = fle)
Savefile.grid(row=0,column=3)

root.mainloop()