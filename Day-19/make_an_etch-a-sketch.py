from turtle import Turtle, Screen

# W = Forwards
# S = Backwards
# A = Counter_Clockwise
# D = Clockwise
# C = Clear drawing

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    # new_heading = tim.left(10)
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    # new_heading = tim.right(10)
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_drawing, "c")

screen.exitonclick()