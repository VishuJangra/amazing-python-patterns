import turtle
colors = ['red', 'yellow', 'green']
colors2 = ['yellow', 'green', 'red']
draw = turtle.Pen()
turtle.bgcolor('black')
draw.speed(10000)

for i in range(360):
    draw.pencolor(colors[i % 3])
    draw.width(i/100*2)
    draw.forward(i)
    draw.left(-180)
    draw.right(30)

draw.hideturtle()