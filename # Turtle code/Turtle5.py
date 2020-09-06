import turtle
import math
import colorsys
phi = 360 * (3 - math.sqrt(5))
t = turtle.Pen()
t.speed(0)
window = turtle.Screen()
window.setup(width=1.0, height=1.0, startx=None, starty=None)
num = 170
for x in reversed(range(0, num)):
    t.fillcolor(colorsys.hsv_to_rgb(x/num, 1.0, 1.0))
    t.begin_fill()
    t.circle(5 + x, None, 11)
    t.end_fill()
    t.right(phi)
    t.right(0.8)
turtle.done()
