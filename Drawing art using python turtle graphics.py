import turtle

def draw_square(some_turtle):

    for _ in range(4):
        some_turtle.forward(200)
        some_turtle.right(90)

def draw_art():

    # Turtle Brad
    brad = turtle.Turtle()
    brad.shape('square')
    brad.color("yellow")
    brad.pensize(2)
    brad.speed(0)  

    for _ in range(36):
        draw_square(brad)
        brad.right(10)

    # Turtle Angie
    angie = turtle.Turtle()
    angie.shape('turtle')
    angie.color("blue")
    angie.pensize(2)
    angie.speed(0)  

    size = 1

    for _ in range(300):
        angie.forward(size)
        angie.right(91)
        size += 1

window = turtle.Screen()
window.bgcolor("black")

draw_art()

window.exitonclick()


