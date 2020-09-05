import turtle

root = turtle.Turtle()
root.pensize(5)
root.speed(4)
root.shape("turtle")
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black", "cyan", "grey"]
for each_color in colors:
    angle = 360 / len(colors)
    root.color(each_color)
    root.circle(40)
    root.right(angle)
    root.forward(30)

turtle.done()
