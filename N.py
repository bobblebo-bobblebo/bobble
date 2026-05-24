import html
from statistics import geometric_mean
from tkinter import *
win = Tk()
acd=0
win["bg"] = "#000000"
lblx = 0
lbly = 0
nul = 0
zeronul = 0
def q(number):
    global nul
    global zeronul
    global lblx
    global lbly
    if nul == 0:
        nul = 1
        lab1["text"] = str(number)
    else:
        lab1["text"] += str(number)
    if zeronul == 0:
        lblx = int(lab1["text"])
    else:
        lbly = int(lab1["text"])
def q1():
    q(1)
def q2():
    q(2)
def q3():
    q(3)
def q4():
    q(4)
def q5():
    q(5)
def q6():
    q(6)
def q7():
    q(7)
def q8():
    q(8)
def q9():
    q(9)
def q0():
    q(0)
znak = "n"

def btnznak(z):
        global nul
        global zeronul
        global znak
        global lblx
        global lbly
        lab1["text"] = lab1["text"] + z
        nul = 0
        zeronul = 1
        znak = z
def plus():
    btnznak("+")
def minus():
    btnznak("-")
def umnochitj():
    btnznak("*")
def delenie():
    btnznak("/")
def btrv():
    global znak
    global num
    global num2
    global lblx
    global lbly
    global nul
    global zeronul
    if znak == "+":
        lab1["text"] = str(lblx + lbly)
    elif znak == "-":
        lab1["text"] = str(lblx - lbly)
    elif znak == "*":
        lab1["text"] = str(lblx * lbly)
    elif znak == "÷":
        if lbly == 0:
            lab1["text"] = "На нуль ділити неможна"
        else:
            lab1["text"] = str(lblx / lbly)
    if lab1["text"].isdigit() == True:
        lblx = float(lab1["text"])
        lbly = 0
        nul = 0
        zeronul = 0
        num = 0
        num2 = 0
        znak = "n"
def reset():
    global lblx,lbly,nul,zeronul,znak
    lab1["text"] = ""
    lblx = 0
    lbly = 0
    nul = 0
    zeronul = 0
    znak="n"
lab1 = Label(text="...", font="Arial",bg="#000000",fg="#FFFFFF",borderwidth=2,relief="solid",highlightbackground="#363434",highlightthickness=2,width=58,height=5)
lab1.place(x=550,y=50)
btn = Button(text="+",bg="#000000",width=10,height=5,fg="#FFFFFF",command=plus)
btn.place(x=1000,y=200)
btn = Button(text="-",bg="#000000",width=10,height=5,fg="#FFFFFF",command=minus)
btn.place(x=1000,y=350)
btn = Button(text="*",bg="#000000",width=10,height=5,fg="#FFFFFF",command=umnochitj)
btn.place(x=1000,y=500)
btn = Button(text="/",bg="#000000",width=10,height=5,fg="#FFFFFF",command=delenie)
btn.place(x=1000,y=650)
btn = Button(text="=",bg="#000000",width=10,height=5,fg="#FFFFFF",command=btrv)
btn.place(x=850,y=650)
btn = Button(text="res",bg="#000000",width=10,height=5,fg="#FFFFFF",command=reset)
btn.place(x=700,y=650)
btn = Button(text="0",bg="#000000",width=10,height=5,fg="#FFFFFF",command=q0)
btn.place(x=550,y=650)
btn = Button(text="1",bg="#000000",width=10,height=5,fg="#FFFFFF",command=q1)
btn.place(x=850,y=500)
btn = Button(text="2",bg="#000000",width=10,height=5,fg="#FFFFFF",command=q2)
btn.place(x=700,y=500)
btn = Button(text="3",bg="#000000",width=10,height=5,fg="#FFFFFF",command=q3)
btn.place(x=550,y=500)
btn = Button(text="4",bg="#000000",width=10,height=5,fg="#FFFFFF",command=q4)
btn.place(x=850,y=350)
btn = Button(text="5",bg="#000000",width=10,height=5,fg="#FFFFFF",command=q5)
btn.place(x=700,y=350)
btn = Button(text="6",bg="#000000",width=10,height=5,fg="#FFFFFF",command=q6)
btn.place(x=550,y=350)
btn = Button(text="7",bg="#000000",width=10,height=5,fg="#FFFFFF",command=q7)
btn.place(x=850,y=200)
btn = Button(text="8",bg="#000000",width=10,height=5,fg="#FFFFFF",command=q8)
btn.place(x=700,y=200)
btn = Button(text="9",bg="#000000",width=10,height=5,fg="#FFFFFF",command=q9)
btn.place(x=550,y=200)
win.mainloop()