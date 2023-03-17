from turtle import Turtle, Screen

joni = Turtle()
screen = Screen()


def move_forward():
    joni.forward(15)


def move_backward():
    joni.back(15)


def turn_left():
    joni.left(10)


def turn_right():
    joni.right(10)

def clear():
    joni.clear()
    joni.penup()
    joni.home()
    joni.pendown()


screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")
screen.exitonclick()
