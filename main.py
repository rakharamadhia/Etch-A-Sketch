from turtle import Turtle, Screen

joni = Turtle()
screen = Screen()


def move_forward():
    joni.forward(15)


def move_backward():
    joni.back(15)


screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")

screen.exitonclick()