import turtle

def draw_square():
    square = turtle.Turtle()
    square.shape("turtle")
    square.color("blue")
    square.speed(2)
    lines = 0
    while lines < 4:
        square.forward(50)
        square.right(90)
        lines = lines + 1
def draw_circle():
    circle = turtle.Turtle()
    circle.shape("classic")
    circle.color("orange")
    circle.circle(50)
def draw_tri():
    tri = turtle.Turtle()
    lines = 0
    while lines < 3:
        tri.forward(75)
        tri.left(120)
        lines = lines + 1
    
carpet = turtle.Screen()
carpet.bgcolor("red")
draw_square()
draw_circle()
draw_tri()
carpet.exitonclick()
