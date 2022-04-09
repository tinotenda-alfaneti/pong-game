from turtle import Screen
from display import Display, RightScore, LeftScore
from paddle import FirstPaddle, SecondPaddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("blue")
screen.title("Atarist Pong Game")

screen.tracer(0)
display = Display()
right_score = RightScore()
left_score = LeftScore()
screen.update()
pad_one = FirstPaddle()
pad_two = SecondPaddle()
ball = Ball()


screen.tracer(1)
screen.listen()
screen.onkey(pad_one.move_up, "Up")
screen.onkey(pad_one.move_down, "Down")
screen.onkey(pad_two.move_up, "w")
screen.onkey(pad_two.move_down, "s")

game_is_on = True
while game_is_on:
    ball.move()
    right_score.score_right()
    left_score.score_left()

    # Detecting collisions
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detecting collision with paddles
    if ball.distance(pad_two) < 50 or ball.distance(pad_one) < 50:
        ball.bounce_x()

    # Detecting when it misses the ball

    if ball.xcor() > 360:
        left_score.left_score += 1
        left_score.score_left()
        ball.reset_position()

    if ball.xcor() < -360:
        right_score.right_score += 1
        right_score.score_right()
        ball.reset_position()


screen.exitonclick()
