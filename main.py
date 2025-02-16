from turtle import Turtle, Screen
import time
from food import Food
from scoreboard import Scoreboard

from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)


    snake.move()

    if snake.snake_list[0].distance(food) < 15:
        food.refresh()
        scoreboard.update()
        snake.extend()

    if snake.snake_list[0].xcor()>280 or snake.snake_list[0].xcor()<-280 or snake.snake_list[0].ycor()>280 or snake.snake_list[0].ycor()<-280:
        scoreboard.end()
        game_is_on=False

    for segment in snake.snake_list:
        if segment==snake.snake_list[0]:
            pass
        elif snake.snake_list[0].distance(segment)<10:
            scoreboard.end()
            game_is_on=False
            
screen.exitonclick()