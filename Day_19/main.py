from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_leftwards():
    tim.lt(10)

def move_rightwards():
    tim.rt(10)

def Clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_leftwards)
screen.onkey(key="d", fun=move_rightwards)
screen.onkey(key="c", fun=Clear)
screen.exitonclick()