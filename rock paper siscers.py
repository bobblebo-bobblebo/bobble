import html
import tkinter.messagebox
from statistics import geometric_mean
import random
from tkinter import *
win = Tk()
win.title("rock paper siscorses")
def click(btn,):
    print(btn["text"])
    computer=random.choice(["rock","paper","scissors"])
    print(computer)
    btn6["text"] = "computer answer " + computer
    if computer=="rock" and btn["text"]=="paper":
        btn4["text"] = ("you win")
    if computer=="rock" and btn["text"]=="rock":
        btn4["text"] = ("nobody win")
    if computer=="rock" and btn["text"]=="siscors":
        btn4["text"] = ("computer win")
    if computer == "rock" and btn["text"] == "paper":
        btn4["text"] = ("you win")
    if computer == "siscors" and btn["text"] == "rock":
        btn4["text"] = ("you win")
    if computer == "scissors" and btn["text"] == "paper":
        btn4["text"] = ("computer win")
    if computer=="siscors" and btn["text"]=="siscors":
        btn4["text"] = ("nobody win")
    if computer == "paper" and btn["text"] == "paper":
        btn4["text"] = ("nobody win")
    if computer == "paper" and btn["text"] == "rock":
        btn4["text"] = ("computer win")
    if computer == "paper" and btn["text"] == "siscors":
        btn4["text"] = ("you win")
    if btn4["text"] == "computer win":
        win["bg"]="#1C1C1C"
    if btn4["text"] == "you win":
        win["bg"] = "#FFFFFF"
    if btn4["text"] == "nobody win":
        win["bg"] = "#787878"
win["bg"]="#000000"
btn1=Button(text="paper",bg="#1F1C1B",width=30,height=10,fg="#FFFFFF",command=lambda:click(btn1))
btn1.place(x=230,y=600)
btn2=Button(text="rock",bg="#616161",width=30,height=10,fg="#FFFFFF",command=lambda:click(btn2))
btn2.place(x=700,y=600)
btn3=Button(text="siscors",bg="#FF0000",width=30,height=10,fg="#FFFFFF",command=lambda:click(btn3))
btn3.place(x=1130,y=600)
btn4=Label(text="who wins????",bg="#FFFFFF",width=20,height=10,fg="#0D0D0D")
btn4.place(x=730,y=300)
btn5=Label(text="robot",bg="#0C6E20",width=30,height=10,fg="#0d0d0d")
btn5.place(x=700,y=20)
btn6=Label(text="computer answer",bg="#181818",width=20,height=10,fg="#FFFFFF")
btn6.place(x=260,y=30)
win.mainloop()
