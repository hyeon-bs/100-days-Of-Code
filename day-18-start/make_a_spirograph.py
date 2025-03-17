import turtle as t
import random, time

tim = t.Turtle()

num = 50

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed("fastest")

# for _ in range(num):
#   tim.color(random_color())
#   tim.circle(100)
#   tim.left(360/num)

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
      tim.color(random_color())
      tim.circle(100)
      tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = t.screen()
screen.exitonclick()