import turtle

def draw_frac():
    circle = turtle.Turtle()
    circle.shape("classic")
    circle.color("orange")
    circle.speed(100)
    for i in range(0,36):
        circle.circle(100)
        circle.right(10)
    
carpet = turtle.Screen()
carpet.bgcolor("green")
draw_frac()

carpet.exitonclick()
