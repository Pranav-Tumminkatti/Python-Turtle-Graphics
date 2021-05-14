import turtle
def spiral(sideLen,angle,scaleFactor,numSides):
    tim = turtle.Turtle()
    tim.speed(0)
    for i in range(numSides):
        tim.fd(sideLen)
        tim.left(angle)
        sideLen*=scaleFactor
