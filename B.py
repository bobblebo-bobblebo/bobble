import html
from statistics import geometric_mean
from tkinter import *
abc=1
win = Tk()
c=0
farm=1
farmclick=0
shop=0
clickcolor="#004704"
def clickcolor_func(button):
     global clickcolor,c
     if c>50:
          c=c-50
          lab1["text"] = c
          clickcolor = button["bg"]
          btn["bg"] = clickcolor
     if c>100:
          c=c-100
          lab1["text"]=c
          clickcolor=button["bg"]
          btn["bg"]=clickcolor
     if c>200:
          c=c-200
          lab1["text"]=c
          clickcolor=button["bg"]
          btn["bg"]=clickcolor
     if c>500:
          c=c-500
          lab1["text"]=c
          clickcolor=button["bg"]
          btn["bg"]=clickcolor
     if c>1000:
          c=c-1000
          lab1["text"]=c
          clickcolor=button["bg"]
          btn["bg"]=clickcolor
     if c > 2000:
          c = c - 2000
          lab1["text"] = c
          clickcolor = button["bg"]
          btn["bg"] = clickcolor
def abg(btn):
    global c
    win["bg"]=btn["bg"]
    if c > 50:
         c = c - 50
         lab1["text"] = c
         win["bg"] = btn["bg"]
    if c > 100:
         c = c - 100
         lab1["text"] = c
         win["bg"] = btn["bg"]
    if c > 200:
         c = c - 200
         lab1["text"] = c
         win["bg"] = btn["bg"]
    if c > 500:
         c = c - 500
         lab1["text"] = c
         win["bg"]=btn["bg"]
    if c > 1000:
         c = c - 1000
         lab1["text"] = c
         win["bg"]=btn["bg"]
    if c > 2000:
         c = c - 2000
         lab1["text"] = c
         win["bg"]=btn["bg"]
def abf():
     window=Toplevel()
     window.geometry("480x320+500+100")
     window["bg"] = "#000000"
     lbl = Label(window,text="Red color", font="Arial",bg="#B6B6B6",)
     lbl.place(x=400,y=40)
     lbl1 = Label(window, text="Orange color", font="Arial", bg="#B6B6B6", )
     lbl1.place(x=400,y=200)
     lbl2 = Label(window, text="Yellow color", font="Arial", bg="#B6B6B6", )
     lbl2.place(x=400,y=400)
     lbl3 = Label(window, text="Green color", font="Arial", bg="#B6B6B6", )
     lbl3.place(x=400,y=600)
     lbl3 = Label(window, text="Blue color", font="Arial", bg="#B6B6B6", )
     lbl3.place(x=800, y=40)
     lbl3 = Label(window, text="Purple color", font="Arial", bg="#B6B6B6", )
     lbl3.place(x=800, y=200)
     btn4 = Button(window,text="RED need 50 clickers",bg="#FF0000",width=20,height=5,fg="#000000",command=lambda : clickcolor_func(btn4))
     btn4.place(x=200,y=40)
     btn5 = Button(window,text="ORANGE need 100 clickers",bg="#FF9000",width=20,height=5,fg="#000000",command=lambda : clickcolor_func(btn5))
     btn5.place(x=200,y=200)
     btn6 = Button(window,text="YELLOW need 200 clickers",bg="#FFF700",width=20,height=5,fg="#000000",command=lambda : clickcolor_func(btn6))
     btn6.place(x=200,y=400)
     btn7 = Button(window, text="GREEN need 500 clickers", bg="#21FF00", width=20, height=5, fg="#000000",command=lambda: clickcolor_func(btn7))
     btn7.place(x=200, y=600)
     btn8 = Button(window, text="BLUE need 1000 clickers", bg="#0000FF", width=20, height=5, fg="#000000",command=lambda: clickcolor_func(btn8))
     btn8.place(x=600, y=40)
     btn9 = Button(window, text="PURPLE need 2000 clickers", bg="#C300FF", width=20, height=5, fg="#000000",command=lambda: clickcolor_func(btn9))
     btn9.place(x=600, y=200)
     lbl = Label(window, text="Brown color bg)", font="Arial", bg="#B6B6B6", )
     lbl.place(x=1200, y=40)
     lbl1 = Label(window, text="lights brown color bg)", font="Arial", bg="#B6B6B6", )
     lbl1.place(x=1200, y=200)
     lbl2 = Label(window, text="gray color bg)", font="Arial", bg="#B6B6B6", )
     lbl2.place(x=1200, y=400)
     lbl3 = Label(window, text="lights gray color bg)", font="Arial", bg="#B6B6B6", )
     lbl3.place(x=1200, y=600)
     lbl3 = Label(window, text="dark brown color bg)", font="Arial", bg="#B6B6B6", )
     lbl3.place(x=1600, y=40)
     lbl3 = Label(window, text="Lights lights brown color bg)", font="Arial", bg="#B6B6B6", )
     lbl3.place(x=1600, y=200)
     btn4 = Button(window, text="BROWN need 50 clickers", bg="#8A5319", width=20, height=5, fg="#000000",command=lambda: abg(btn4))
     btn4.place(x=1000, y=40)
     btn5 = Button(window, text="LIGHTS BROWN need 100 clickers", bg="#B56818", width=20, height=5, fg="#000000",command=lambda: abg(btn5))
     btn5.place(x=1000, y=200)
     btn6 = Button(window, text="GRAY need 200 clickers", bg="#42403F", width=20, height=5, fg="#000000",command=lambda: abg(btn6))
     btn6.place(x=1000, y=400)
     btn7 = Button(window, text="LIGHTS GRAY need 500 clickers", bg="#AFADAC", width=20, height=5, fg="#000000",command=lambda: abg(btn7))
     btn7.place(x=1000, y=600)
     btn8 = Button(window, text="DARK BROWN need 1000 clickers", bg="#69290C", width=20, height=5, fg="#000000",command=lambda: abg(btn8))
     btn8.place(x=1400, y=40)
     btn9 = Button(window, text="LIGHTS LIGHTS BROWN need 2000 clickers", bg="#B06948", width=20, height=5, fg="#000000",command=lambda: abg(btn9))
     btn9.place(x=1400, y=200)
def abd():
     global farm,c,farmclick
     farm=10
     farmclick=5
     c=c-200
     if c<200:
          btn2["state"] = "disabled"
     lab1["text"] = c
def ab():
     global abc,c
     if c>49:

          c=c-50
          abc=abc+1
     lab1["text"] = c
     btn1["state"] = "disabled"
def b():
     global c,farmclick,farm
     c=c+(abc*farm)
     lab1["text"] = c
     farmclick=farmclick-1
     if farmclick==0:
          farm=1
     if c>49:
          btn1["state"] = "normal"
     else:
          btn1["state"] = "disabled"
     if c>200:
          btn2["state"] = "normal"
     else:
          btn2["state"] = "disabled"
     if c>100:
          btn3["state"] = "normal"
win.geometry("480x320+500+100")
win["bg"] = "#004704"
btn = Button(text = "click",bg=clickcolor,width=20,height=10,fg="#006B51",command=b,)
btn.place(x=700,y=300)
lab1 = Label(text="clickers", font="Arial",bg="#004704",)
lab1.place(x=700,y=100)
btn1 = Button(text = "SUSLIK CLICK need 50 clicks",bg="#96968F",width=20,height=5,fg="#F5F500",command=ab,)
lab2 = Label(text="afto clickers", font="Arial",bg="#E027F5",)
btn1["state"] = "disabled"
btn1.place(x=1000,y=40)
btn2=Button(text = "SUSLIK FARM need 200 clicks",bg="#96968F",width=20,height=5,fg="#F5F500",command=abd,)
btn3=Button(text = "SHOP", bg="#96968F",width=20,height=5,fg="#F5F500",command=abf)
btn3.place(x=300,y=40)
btn3["state"] = "disabled"
btn2.place(x=1000,y=140)
btn2["state"] = "disabled"
win.mainloop()