from turtle import Turtle


class Display(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        new = Turtle()
        new.color("white")
        new.pensize(5)

        x_0 = -300
        x_1 = -300
        for _ in range(30):
            new.hideturtle()
            new.setheading(90)
            new.penup()
            new.goto(0, x_0)
            new.pendown()
            new.goto(0, x_1)
            x_0 = x_1 + 20
            x_1 = x_0 + 20

    def game_over(self):
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("courier", 24, "normal"))


class LeftScore(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.hideturtle()

    def score_left(self):

        self.penup()
        self.hideturtle()
        self.color("red")

        self.goto(-20, 260)
        self.clear()
        self.write(f"{self.left_score}", align="center", font=("courier", 24, "normal"))


class RightScore(Turtle):
    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.hideturtle()

    def score_right(self):
        self.penup()
        self.hideturtle()
        self.color("red")

        self.goto(20, 260)
        self.clear()
        self.write(f"{self.right_score}", align="center", font=("courier", 24, "normal"))




