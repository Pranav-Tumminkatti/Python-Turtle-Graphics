import turtle

bob = turtle.Turtle()
bob.speed(100)
bob.pu()

flag_height = 250
flag_width = 475


start_x = -237
start_y = 125


stripe_height = flag_height/13
stripe_width = flag_width


star_size = 10


def draw_fill_rectangle(x, y, height, width, color):
    bob.setpos(x,y)
    bob.pd()
    bob.color(color)
    bob.begin_fill()
    bob.fd(width)
    bob.right(90)
    bob.fd(height)
    bob.right(90)
    bob.fd(width)
    bob.right(90)
    bob.fd(height)
    bob.right(90)
    bob.end_fill()
    bob.pu()

def draw_star(x,y,color,length) :
    bob.setpos(x,y)
    bob.pd()
    bob.begin_fill()
    bob.color(color)
    for i in range(0,5) :
        bob.fd(length)
        bob.right(144)
        bob.fd(length)
        bob.right(144)
    bob.end_fill()
    bob.penup()


def draw_stripes():
    x = start_x
    y = start_y    
    for stripe in range(0,6):
        for color in ["red", "white"]:
            draw_fill_rectangle(x, y, stripe_height, stripe_width, color)
            y = y - stripe_height           
    draw_fill_rectangle(x, y, stripe_height, stripe_width, 'red')
    y = y - stripe_height


def draw_square():
    square_height = (7/13) * flag_height
    square_width = (0.76) * flag_height
    draw_fill_rectangle(start_x, start_y, square_height, square_width, 'navy')


def draw_six_stars_rows():
    gap_between_stars = 30
    gap_between_lines = stripe_height + 6
    y = 112
    for row in range(0,5) :
        x = -222
        for star in range (0,6) :
            draw_star(x, y, 'white', star_size)
            x = x + gap_between_stars
        y = y - gap_between_lines


def draw_five_stars_rows():
    gap_between_stars = 30
    gap_between_lines = stripe_height + 6
    y = 100
    for row in range(0,4) :
        x = -206
        for star in range (0,5) :
            draw_star(x, y, 'white', star_size)
            x = x + gap_between_stars
        y = y - gap_between_lines

draw_stripes()
draw_square()
draw_six_stars_rows()
draw_five_stars_rows()
