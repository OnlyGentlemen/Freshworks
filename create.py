#BLL
from tkinter import *
import json
import os
import sys
from tkinter import messagebox, simpledialog


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


def create():
    em=entere1.get()
    na=entern1.get()

    if (len(em.strip()) == 0):
        messagebox.showinfo('Invalid','Kindly enter valid email id.',icon='warning')

    elif (len(na.strip()) == 0):
        messagebox.showinfo('Invalid','Kindly enter valid name.',icon='warning')

    else:
        dic={}

        loc = str(find('datastore.json','F:\\'))

        if (os.path.exists(loc)):
            pass

        else:

            MsgBox = messagebox.askquestion('Enter path of file','Do you want to manually enter the path of the datastore file?')
            if MsgBox == 'yes':
                pathvar = simpledialog.askstring(title="Path of DataStore",prompt=f"Enter the path in F:\\ where you want the file to be created at :")
                filepath = os.path.join(pathvar,'datastore.json')
                if not os.path.exists(pathvar):
                    os.makedirs(pathvar)

            else:
                messagebox.showinfo('Path of file', 'The file will be created at F:\ by default.')
                filepath=os.path.join('F:\\','datastore.json')
            f=open(filepath, 'w')
            brac={}
            json.dump(brac, f)

        loc=find('datastore.json','F:\\')
        f = open(loc)
        dic = json.load(f)

        if em in dic.keys():
            messagebox.showinfo("Warning!", "Data with the same email address already exists. Kindly re-enter data.")
            vare1.set("")
            varn1.set("")
        else:
            json_dump = json.dumps(na)
            dic[em] = json_dump

            ff = open(loc, 'w')
            json.dump(dic, ff)

            vare1.set("")
            varn1.set("")
            messagebox.showinfo("Success!", "Data Created Successfully.")

def close():
    root1.destroy()


#PL

root1=Tk()
root1.geometry("500x500")

w1=Label(root1, text="")
w1.grid(row=0, column=0)
w2=Label(root1, text="___DATASTORE___", bg="violet", fg="black", font=1)
w2.grid(row=1, column=1)
w3=Label(root1, text="")
w3.grid(row=2, column=0)

e1 = Label(root1,text="Enter Email ID : ",font=1)
e1.grid(row=3,column=0)
vare1 = StringVar()
entere1 = Entry(root1,font=1,textvariable=vare1)
entere1.grid(row=3,column=1)

n1 = Label(root1,text="Enter Name : ",font=1)
n1.grid(row=4,column=0)
varn1 = StringVar()
entern1 = Entry(root1,font=1,textvariable=varn1)
entern1.grid(row=4,column=1)

w4=Label(root1, text="")
w4.grid(row=5, column=0)

bcreate = Button(root1,text="CREATE",command=create,bg="light blue",width=20)
bcreate.grid(row=6,column=1,pady=3)

bclose = Button(root1,text="CLOSE",command=close,bg="light blue",width=20)
bclose.grid(row=7,column=1,pady=3)


root1.mainloop()