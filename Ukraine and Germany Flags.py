# Program Filename: 24ypran395i.py
# My Full Name: Pranav Tumminkatti
# My Class: 2L

import turtle

#Ukraine Flag
tim = turtle.Turtle()
tim.color('royalblue','royalblue')
tim.width(5)

tim.pu()
tim.setpos(-300,100)
tim.pd()

tim.begin_fill()
tim.fd(180)
tim.right(90)
tim.fd(60)
tim.right(90)
tim.fd(180)
tim.right(90)
tim.fd(60)
tim.end_fill()

tim.right(180)
tim.fd(60)

tim.color('yellow','yellow')
tim.begin_fill()
tim.fd(60)
tim.left(90)
tim.fd(180)
tim.left(90)
tim.fd(60)
tim.left(90)
tim.fd(180)
tim.end_fill()


tim.pu()
tim.setpos(220,100)
tim.pd()


#Germany Flag
tim.color('black','black')
tim.begin_fill()
tim.fd(180)
tim.left(90)
tim.fd(40)
tim.left(90)
tim.fd(180)
tim.left(90)
tim.fd(40)
tim.end_fill()

tim.backward(40)
tim.left(90)
tim.color('red','red')
tim.begin_fill()
tim.fd(180)
tim.left(90)
tim.fd(40)
tim.left(90)
tim.fd(180)
tim.left(90)
tim.fd(40)
tim.end_fill()

tim.backward(40)
tim.left(90)
tim.color('yellow','yellow')
tim.begin_fill()
tim.fd(180)
tim.left(90)
tim.fd(40)
tim.left(90)
tim.fd(180)
tim.left(90)
tim.fd(40)
tim.end_fill()

