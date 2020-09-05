import turtle
kk = turtle.Turtle()
kk.pensize(2)


def curve():
    for i in range(200):
        kk.right(1)
        kk.forward(1)


kk.speed(0.1)
kk.color("black", "red")
kk.begin_fill()
kk.left(140)
kk.forward(111.65)
curve()
kk.left(120)
curve()
kk.forward(111.65)
kk.end_fill()
kk.hideturtle()


turtle.done()
