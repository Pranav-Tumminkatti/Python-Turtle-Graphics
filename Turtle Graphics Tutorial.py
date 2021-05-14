#Turtle Graphics in Pygame
#Reference: https://docs.python.org/2/library/turtle.html
#Reference: https://michael0x2a.com/blog/turtle-examples
#Very Important Reference: https://realpython.com/beginners-guide-python-turtle/

import turtle

tim = turtle.Turtle()  #set item type
tim.color('red')  #set colour
tim.pensize(5)  #set thickness of line
tim.shape('turtle')

tim.forward(100)  #turtle moves 100 pixels forward
tim.left(90)  #turtle turns left 90 degrees
tim.forward(100)
tim.right(90)

tim.forward(100)
tim.penup() #lifts the pen up - turtle is moving but line is not drawn
tim.left(90)
tim.forward(100)
tim.right(90)
tim.pendown()  #puts the pen back down
tim.forward(100)

tim.left(90)
tim.penup()
tim.forward(50)
tim.left(90)
tim.pendown()

tim.color('green')  #changes the colour of the line to green
tim.forward(100)

#Making a new object named dave
dave = turtle.Turtle() 
dave.color('blue')
dave.pensize(10)
dave.shape('arrow')

dave.backward(100)
dave.speed(1)


