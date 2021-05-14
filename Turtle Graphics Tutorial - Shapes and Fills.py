#Python Turtle Graphics Tutorial 2 - Shapes and Fills

import turtle
import random

tim = turtle.Turtle()
colors = ['red' , 'blue' , 'green' , 'purple' , 'yellow' , 'orange' , 'black']

#setting colours
# format - (outline colour , fill colour)
tim.color('red' , 'blue')

#set pen width
tim.width(5)

#Filling in a circle with colour
tim.begin_fill()
tim.circle(50)  #circle of radius 50 pixels
tim.end_fill()

tim.penup()
tim.forward(150)
tim.pendown()

#Filling a square with colour
tim.color('yellow' , 'black')

tim.begin_fill()  #start filling
for x in range(4):
    tim.forward(100)
    tim.right(90)
tim.end_fill()  #finish filling

#Drawing circles at 5 random positions on the canvas
for i in range(5):
    randomColour = random.randrange(0, len(colors))
    tim.color(colors[randomColour], colors[random.randrange(0, len(colors))])
    random1 = random.randrange(-300,300)
    random2 = random.randrange(-300,300)
    tim.penup()
    tim.setpos(random1,random2)
    tim.pendown()
    tim.begin_fill()
    tim.circle(random.randrange(0,80))
    tim.end_fill()
