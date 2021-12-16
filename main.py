from turtle import Screen

from snake2 import Snake
from food import Food
from scoreboard import Scoreboard

import time

screen = Screen()
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

snake.create_snake()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.head.xcor() > 470 or snake.head.xcor() < -470 or snake.head.ycor() > 400 or snake.head.ycor() < -400:
        score.reset()
        snake.reset()
    #Detect collision with tail
    #if head collides with any segment in the tail
   #Detect collision with wall
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.reset()
            snake.reset()

screen.exitonclick()

