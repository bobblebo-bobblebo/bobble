import turtle as t
t.shape("turtle")
t.speed(100)

def oleh(color):
    t.begin_fill()
    t.color(color)
    for j in range(4):

        t.forward(50)
        t.right(90)
    t.end_fill()
    t.forward(50)
oleh2=0
for i in range(4):
    for j in range(4):
        oleh("black")
        oleh("yellow")
    t.penup()
    oleh2+=50
    t.goto(0, oleh2)
    t.pendown()
    for j in range(4):
        oleh("yellow")
        oleh("black")
    t.penup()
    oleh2 += 50
    t.goto(0, oleh2)
    t.pendown()
t.done()