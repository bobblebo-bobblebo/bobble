import html
import tkinter.messagebox
from statistics import geometric_mean
from tkinter import *
win = Tk()
win.title("tic-tac-toe")
color=0
result=[2,2,2,2,2,2,2,2,2]
colors=[]
q=""
def click(btn,n):
    global color,q
    if n not in colors:
        colors.append(n)
        result[n] = color
        print(result)
        if color==0:
            color=1
            btn["bg"] = "#0A00FF"
        else:
            color=0
            btn["bg"] = "#FF0000"
    if  result[0]==result[1]==result[2]!=2:
        print("win",result[1])
        q=result[1]
    if result[0]==result[4]==result[8]!=2:
        print("win",result[4])
        q=result[4]
    if result[3]==result[4]==result[5]!=2:
        print("win",result[3])
        q=result[3]
    if result[6]==result[7]==result[8]!=2:
        print("win",result[6])
        q=result[6]
    if result[0]==result[3]==result[6]!=2:
        print("win",result[6])
        q=result[6]
    if result[1]==result[4]==result[7]!=2:
        print("win",result[7])
        q=result[7]
    if result[2]==result[5]==result[8]!=2:
        print("win",result[8])
        q=result[8]
    if result[2] ==result[4]==result[6]!=2:
        print("win",result[2])
        q=result[2]
    if 2 not in result:
        tkinter.messagebox.showinfo("Winner", "NOBODY WON")

        restart()
    if q==0 or q==1 or q==3:
        if q==0:
             tkinter.messagebox.showinfo("Winner", "Blue win")
             restart()

        elif q==1:
            tkinter.messagebox.showinfo("Winner", "Red win")
            restart()



def restart():
    global color ,result,colors,q
    btn1['bg']="#1F1C1B"
    btn2['bg']="#1F1C1B"
    btn3['bg']="#1F1C1B"
    btn4['bg']="#1F1C1B"
    btn5['bg']="#1F1C1B"
    btn6['bg']="#1F1C1B"
    btn7['bg']="#1F1C1B"
    btn8['bg']="#1F1C1B"
    btn9['bg']="#1F1C1B"
    color = 0
    result = [2, 2, 2, 2, 2, 2, 2, 2, 2]
    colors = []
    q = ""

win["bg"]="#000000"
btn1=Button(text="1",bg="#1F1C1B",width=20,height=10,fg="#FFFFFF",command=lambda: click(btn1,0))
btn2=Button(text="2",bg="#1F1C1B",width=20,height=10,fg="#FFFFFF",command=lambda: click(btn2,1))
btn3=Button(text="3",bg="#1F1C1B",width=20,height=10,fg="#FFFFFF",command=lambda: click(btn3,2))
btn4=Button(text="4",bg="#1F1C1B",width=20,height=10,fg="#FFFFFF",command=lambda: click(btn4,3))
btn5=Button(text="5",bg="#1F1C1B",width=20,height=10,fg="#FFFFFF",command=lambda: click(btn5,4))
btn6=Button(text="6",bg="#1F1C1B",width=20,height=10,fg="#FFFFFF",command=lambda: click(btn6,5))
btn7=Button(text="7",bg="#1F1C1B",width=20,height=10,fg="#FFFFFF",command=lambda: click(btn7,6))
btn8=Button(text="8",bg="#1F1C1B",width=20,height=10,fg="#FFFFFF",command=lambda: click(btn8,7))
btn9=Button(text="9",bg="#1F1C1B",width=20,height=10,fg="#FFFFFF",command=lambda: click(btn9,8))
btn5.place(x=700,y=350)
btn8.place(x=400,y=350)
btn7.place(x=400,y=50)
btn9.place(x=400,y=650)
btn6.place(x=700,y=650)
btn3.place(x=1000,y=650)
btn4.place(x=700,y=50)
btn1.place(x=1000,y=50)
btn2.place(x=1000,y=350)
win.bind('1',lambda e:click(btn1,0))
win.bind('2',lambda e:click(btn2,1))
win.bind('3',lambda e:click(btn3,2))
win.bind('4',lambda e:click(btn4,3))
win.bind('5',lambda e:click(btn5,4))
win.bind('6',lambda e:click(btn6,5))
win.bind('7',lambda e:click(btn7,6))
win.bind('8',lambda e:click(btn8,7))
win.bind('9',lambda e:click(btn9,8))
win.mainloop()
