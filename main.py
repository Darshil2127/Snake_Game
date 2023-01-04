from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Scoreboard
screen = Screen()
food = Food()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update() #program refresh or turn on the screen
    time.sleep(0.1) #delay the segment time

    snake.Move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or \
            snake.head.ycor() < -290 :
        game_is_on = False
        scoreboard.gameover()

    # detect collision with tail
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.gameover()

screen.exitonclick()