import turtle as t
import colorsys as cs

t.setup(800, 800)
t.speed(0)
t.tracer(10)
t.width(2)
t.bgcolor('black')

for j in range(25):
    for i in range(15):
        hue = (i / 15) % 1.0  # Ensure hue is within the range [0, 1]
        saturation = (j / 50) + 0.5  # Adjust saturation to be within [0.5, 1.0]
        t.color(cs.hsv_to_rgb(hue, saturation, 1))
        t.right(90)
        t.circle(200 - j * 4, 90)
        t.left(90)
        t.circle(200 - j * 4, 90)
        t.right(180)
        t.circle(50, 24)

t.hideturtle()
t.done()
