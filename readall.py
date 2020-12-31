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


def close():
    root1.destroy()


#PL

root1 = Tk()
root1.geometry("500x500")

le1=Label(root1, text="EMAIL ID", bg="orange", font=1, width=15)
le1.grid(row=0, column=0)
ln1 = Label(root1,text="NAME",bg="orange",font=1,width=15)
ln1.grid(row=0,column=1)


dic={}

loc = str(find('datastore.json','F:\\'))

if os.path.exists(loc):
    loc = find('datastore.json','F:\\')
    f = open(loc)
    dic = json.load(f)
    i = 1

    for k,v in dic.items():
        le2 = Label(root1,text=f"{k}",bg="yellow",font=1,width=15)
        le2.grid(row=i,column=0)
        ln2 = Label(root1,text=f"{v}",bg="yellow",font=1,width=15)
        ln2.grid(row=i,column=1)

        i += 1

else:
    messagebox.showinfo('Does not exist','The datastore does not exist.')


w4=Label(root1, text="")
w4.grid(column=0)
bclose = Button(root1,text="CLOSE",command=close,bg="light blue",width=20)
bclose.grid(column=1,pady=3)

root1.mainloop()