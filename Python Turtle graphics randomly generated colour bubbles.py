import random
import turtle

tim = turtle.Turtle()
colors = ['blue','red','green','yellow','purple','orange']
tim.speed(100)

tim.pu()
while True:
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    circle_size = random.randint(1,300)
    circle_color = random.choice(colors)

    tim.setpos(x,y)
    tim.pd()
    tim.color(circle_color)
    tim.begin_fill()
    tim.circle(circle_size)
    tim.end_fill()
    tim.pu()
    

