from tkinter import *

root = Tk()
root.title("calci")
first=StringVar()
second=StringVar()
rt=StringVar()



n1Label = Label (root,text="enter number")
n1Label.place(x=20,y=10)
n1Box = Entry(root,textvar=first)
n1Box.place(x=100,y=10)


n2Label = Label (root,text="enter number")
n2Label.place(x=20,y=40)
n2Box = Entry(root,textvar=second)
n2Box.place(x=100,y=40)

n7Label = Label (root,text="Result:")
n7Label.place(x=20,y=120)
n7Box = Entry(root,textvar=rt)
n7Box.place(x=100,y=100)


def addNo():
    no1 = int(n1Box.get())
    no2 = int(n2Box.get())
    n10 =no1+no2
    rt.set(n10)

def subNo():
    no1 = int(n1Box.get())
    no2 = int(n2Box.get())
    n11 =no1-no2
    rt.set(n11)

def mulNo():
    no1 = int(n1Box.get())
    no2 = int(n2Box.get())
    n12 =no1*no2
    rt.set(n12)

def divNo():
    no1 = int(n1Box.get())
    no2 = int(n2Box.get())
    n13 =no1/no2
    rt.set(n13)

but = Button(text="+", command= addNo)
but.place(x=100,y=150)
but = Button(text="-", command=subNo)
but.place(x=150,y=150)
but = Button(text="*", command=mulNo)
but.place(x=200,y=150)
but = Button(text="/", command=divNo)
but.place(x=250,y=150)
root.mainloop()
