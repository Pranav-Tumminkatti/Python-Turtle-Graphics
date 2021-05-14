import turtle



def polygonFlower(numPetals,petalSides,petalLen):
    tim = turtle.Turtle()
    tim.speed(0)
    for _ in range(numPetals):
        for i in range(petalSides):
            tim.fd(petalLen)
            tim.left(360/petalSides)
        tim.left(80)


