#ex3A_polygon.py

# Full Name: Pranav Tumminkatti
# Form Class: 2L

import turtle
tim = turtle.Turtle()

'''
    Example: Using for loop to create a square (4-sided polygon) of length 100
'''
for i in range(4):
    tim.forward(100)
    tim.left(90)
tim.clear()

'''
   Exercise: Use for loop to create a regular triangle (3-sided polygon) of length 100
'''
for i in range (3):
    tim.forward(100)
    tim.left(360/3)
tim.clear()
'''
   Exercise: Use for loop to create a regular pentagon (5-sided polygon) of length 100
'''
for i in range(5):
    tim.forward(100)
    tim.left(360/5)
tim.clear()
'''
   Exercise: Use for loop to create a regular hexagon (6-sided polygon) of length 100
'''
for i in range(6):
    tim.forward(100)
    tim.left(360/6)
tim.clear()
'''
   Exercise: Use for loop to create a regular heptagon (7-sided polygon) of length 100
'''
for i in range(7):
    tim.forward(100)
    tim.left(360/7)
tim.clear()
'''
   Exercise: Use for loop to create a regular octagon (8-sided polygon) of length 100
'''
for i in range(8):
    tim.forward(100)
    tim.left(360/8)
tim.clear()
'''
    Challenge: 
       Use for loop to create a circle (?-sided polygon) 
'''
for i in range(100):
    tim.forward(10)
    tim.left(360/100)






