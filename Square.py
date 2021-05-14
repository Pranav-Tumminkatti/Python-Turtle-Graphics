import turtle

tim = turtle.Turtle()
tim.color('pink')
tim.pensize(5)

colours = ['red','brown','yellow','green','blue']

tim.pu()
tim.setpos(-150,-150)
tim.pd()

for i in range(4):
    tim.fd(360)
    tim.left(90)

tim.pu()
tim.left(90)
tim.fd(360)
tim.right(90)
tim.pd()

for i in range(5):
    tim.color(colours[i])
    tim.pu()
    tim.fd((i+1)*60)
    tim.right(90)
    tim.pd()

    tim.fd((i+1)*60)
    tim.right(90)
    tim.fd((i+1)*60)

    tim.right(90)
    tim.pu()
    tim.fd((i+1)*60)
    tim.right(90)
    tim.pd()
    
    
    
    
