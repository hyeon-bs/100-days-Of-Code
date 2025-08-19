from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.move_speed = 0.1

    def go_up(self):
        if self.xcor() > 380:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.xcor() < -380:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)