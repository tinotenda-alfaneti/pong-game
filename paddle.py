from turtle import Turtle


class FirstPaddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.color("white")
        self.speed(0)
        self.goto(-350, 0)
        self.setheading(90)



    def move_up(self):
        self.forward(20)


    def move_down(self):
        self.backward(20)


class SecondPaddle(FirstPaddle):

    def __init__(self):
        super().__init__()
        self.goto(350, 0)
        self.shapesize(stretch_wid=1, stretch_len=4)





