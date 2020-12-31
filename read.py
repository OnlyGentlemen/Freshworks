#BLL
from tkinter import *
import json
import os
import sys
from tkinter import messagebox


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


def read():
    em=entere1.get()

    if(len(em.strip())==0):
        messagebox.showinfo('Invalid','Kindly enter valid email id.',icon='warning')
    else:
        dic={}

        loc = str(find('datastore.json','F:\\'))

        if (os.path.exists(loc)):
            loc = find('datastore.json','F:\\')
            f = open(loc)
            dic = json.load(f)

            if em in dic.keys():
                varn1.set(dic[em])
            else:
                messagebox.showinfo('Does not exist','The data with this email id does not exist.')
                mbask=messagebox.askquestion("Create new data", "Do you want to create new data field?")
                if mbask=='yes':
                    # os.system('python create.py')
                    cr()

        else:
            messagebox.showinfo('Does not exist','The datastore does not exist.')

def cr():
    os.system('python create.py')

def readall():
    os.system('python readall.py')

def close():
    root1.destroy()


#PL

root1 = Tk()
root1.geometry("500x500")

w1=Label(root1, text="")
w1.grid(row=0, column=0)
w2=Label(root1, text="___DATASTORE___", bg="violet", fg="black", font=1)
w2.grid(row=1, column=1)
w3=Label(root1, text="")
w3.grid(row=2, column=0)

e1 = Label(root1,text="Enter Email ID : ", font=1)
e1.grid(row=3,column=0)
vare1 = StringVar()
entere1 = Entry(root1,font=1,textvariable=vare1)
entere1.grid(row=3,column=1)

n1 = Label(root1,text="The Name is: ",font=1)
n1.grid(row=4,column=0)
varn1 = StringVar()
entern1 = Entry(root1,font=1,textvariable=varn1)
entern1.grid(row=4,column=1)
# n2=Label(root1,text="",font=1)
# n2.grid(row=1,column=1)

w4=Label(root1, text="")
w4.grid(row=5, column=0)

bread = Button(root1,text="READ",command=read,bg="light blue",width=20)
bread.grid(row=6,column=1,pady=3)

breadall = Button(root1,text="READ ENTIRE DATASTORE",command=readall,bg="light blue",width=20)
breadall.grid(row=7,column=1,pady=3)

bclose = Button(root1,text="CLOSE",command=close,bg="light blue",width=20)
bclose.grid(row=8,column=1,pady=3)

root1.mainloop()