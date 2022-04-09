from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("yellow")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        time.sleep(0.1)

    def bounce_y(self):
        self.y_move *= -1
        time.sleep(0.1)

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.hideturtle()
        self.goto(0,0)
        self.showturtle()
        self.bounce_x()




