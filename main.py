from turtle import Screen, Turtle

from player import Player

from ball import Ball

import time

from scoreboard import  Scoreboard

screen = Screen()


screen.setup(width = 800, height = 600)

screen.bgcolor("black")

screen.title("pong game")
screen.tracer(0)

goOrstop=True

p1 = Player()

p2 = Player(-350)

ball = Ball()

scoreboard = Scoreboard()

# middle_wall = Player(0,0,8,1)

screen.listen()

screen.onkey(p1.up,"Up")
screen.onkey(p1.down,"Down")

def move_player2():
    if ball.xcor() < -100 and ball.xcor() > -350:
        if ball.ycor() > p2.ycor():
            p2.up()
        elif ball.ycor() < p2.ycor():
            p2.down()
    else:

        if p2.ycor() < 250:
            p2.up()
        elif p2.ycor() > -250:
            p2.down()


while goOrstop:
    move_player2()
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(p1) < 50 and ball.xcor() > 328):
        ball.bounce_x()
        scoreboard.r_point()
    if (ball.distance(p2) < 50 and ball.xcor() < -328):
        ball.bounce_x()
        scoreboard.l_point()
    if ball.xcor() >400 or ball.xcor()< -400:
        scoreboard.clearScoreBoard()
        ball.reset_ball()





screen.exitonclick()