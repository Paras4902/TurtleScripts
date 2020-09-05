import turtle

mm = turtle.Turtle()
mm.speed(10)
kk = 250
while kk > 0:
    mm.forward(kk)
    mm.right(90)
    mm.forward(kk)
    mm.right(90)
    mm.forward(kk)
    mm.right(90)
    kk -= 1.2
mm.hideturtle()
turtle.done()
