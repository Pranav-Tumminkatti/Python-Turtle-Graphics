import turtle


jim = turtle.Turtle()

jim.pu()
jim.setpos(-50,50)
jim.pd()


jim.color("blue")
jim.begin_fill()
for count in range(2):
  jim.fd(50)
  jim.right(90)
  jim.fd(100)
  jim.right(90)
  
jim.end_fill()


jim.pu()
jim.fd(100)
jim.pd()


jim.begin_fill()
jim.color("red")
for count in range(2):
  jim.fd(50)
  jim.right(90)
  jim.fd(100)
  jim.right(90)
jim.end_fill()


jim.backward(100)
jim.color("black")
for i in range(2):
  jim.fd(150)
  jim.right(90)
  jim.fd(100)
  jim.right(90)

