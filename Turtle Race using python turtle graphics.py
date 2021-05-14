import random
import turtle

turtle.bgcolor('black')
drawline = turtle.Turtle()
drawline.color('white')
drawline.pu()
drawline.setpos(300,250)
drawline.pd()
drawline.right(90)
drawline.fd(400)

frank = turtle.Turtle()
stacey = turtle.Turtle()
tim = turtle.Turtle()
bob = turtle.Turtle()

frank.shape('turtle')
stacey.shape('turtle')
tim.shape('turtle')
bob.shape('turtle')

frank.color('red')
stacey.color('blue')
tim.color('green')
bob.color('yellow')

frank.pu()
frank.setpos(-300,200)
frank.pd()
stacey.pu()
stacey.setpos(-300,100)
stacey.pd()
tim.pu()
tim.setpos(-300,0)
tim.pd()
bob.pu()
bob.setpos(-300,-100)
bob.pd()

frank.width(3)
stacey.width(3)
tim.width(3)
bob.width(3)

for move in range(50):
    f = random.randint(-5,30)
    s = random.randint(-5,30)
    t = random.randint(-5,30)
    b = random.randint(-5,30)
    
    frank.fd(f)
    stacey.fd(s)
    tim.fd(t)
    bob.fd(b)

#check for the winner
winner = None
turtles = [frank,stacey,tim,bob]
while not winner:
    for i in turtles:
        if i.xcor() >= 300:
            winner = i
            break  
    else: 
        continue

    break
if winner == frank:
    turtle.bgcolor('red')
elif winner == stacey:
    turtle.bgcolor('blue')
elif winner == tim:
    turtle.bgcolor('green')
else:
    turtle.bgcolor('yellow')
    
turtle.pencolor('black')
FONT = ("Times New Roman", 20, 'bold')
turtle.write("{} won the race!".format(winner.pencolor()), font=FONT)
