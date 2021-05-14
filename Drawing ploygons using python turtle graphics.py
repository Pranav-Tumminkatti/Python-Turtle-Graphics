import turtle

tim = turtle.Turtle()

tim.speed(0)

def shape(size,sides):
    for i in range(sides):
        tim.fd(size)
        tim.left(360/sides)

for i in range(25):
    shape(5*i,4)
    tim.left(i)
