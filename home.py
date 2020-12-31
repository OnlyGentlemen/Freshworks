#BLL
from tkinter import *
import os
import sys
def cr():
    os.system('python create.py')

def re():
    os.system('python read.py')


def de():
    os.system('python delete.py')


#PL

root=Tk()
root.geometry("500x500")

w1=Label(root, text="")
w1.grid(row=0, column=0)
w2=Label(root, text="___DATASTORE___", bg="violet", fg="black", font=1)
w2.grid(row=1, column=0)
w3=Label(root, text="")
w3.grid(row=2, column=0)
l1=Label(root, text="Welcome to the portal for handling data store.",bg="yellow", fg="purple", font=1)
l1.grid(row=3, column=0)

l2=Label(root, text="Kindly choose one of the below operations to proceed.", bg="yellow", fg="purple", font=1)
l2.grid(row=4, column=0)

w4=Label(root, text="")
w4.grid(row=5, column=0)

bc=Button(root, text="CREATE", command=cr, bg="light blue", width=20)
bc.grid(row=6, column=0, pady=3)

br=Button(root, text="READ", command=re, bg="light blue", width=20)
br.grid(row=7, column=0, pady=3)

bd=Button(root, text="DELETE", command=de, bg="light blue", width=20)
bd.grid(row=8, column=0, pady=3)

root.mainloop()
