from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep


l_paddle = Paddle((350, 0))
r_paddle = Paddle((-350, 0))
ball = Ball()
screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)
screen.setup(width=800, height=600)

screen.listen()
screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")

screen.onkey(r_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "s")
game_is_on = True
while game_is_on:
	sleep(0.1)
	screen.update()
	ball.move()

	# detect collision with wall
	if ball.ycor() > 280 or ball.ycor() < -280:
		# need to bounce
		ball.bounce()

screen.exitonclick()
