from turtle import Turtle, Screen
class Snake:
    snake_list = []

    def __init__(self):
        screen = Screen()
        screen.tracer(0)


        xcor = [0, -20, -40]
        for i in range(3):
            new_snake = Turtle("square")
            new_snake.penup()
            new_snake.color('white')
            new_snake.teleport(xcor[i], 0)
            global snake_list
            self.snake_list.append(new_snake)

        screen.update()

    def move(self):
        for i in range((len(self.snake_list)) - 1, 0, -1):
            xpos = self.snake_list[i - 1].xcor()
            ypos = self.snake_list[i - 1].ycor()
            self.snake_list[i].goto(xpos, ypos)
        self.snake_list[0].forward(20)

    def up(self):
        if self.snake_list[0].heading()!=270:
            self.snake_list[0].setheading(90)

    def down(self):
        if self.snake_list[0].heading() != 90:
            self.snake_list[0].setheading(270)


    def left(self):
        if self.snake_list[0].heading() != 0:
            self.snake_list[0].setheading(180)


    def right(self):
        if self.snake_list[0].heading() != 180:
            self.snake_list[0].setheading(0)

    def extend(self):
        new_snake = Turtle("square")
        new_snake.penup()
        new_snake.color('white')
        # new_snake.teleport(xcor[i], 0)

        self.snake_list.append(new_snake)
        new_snake.goto(self.snake_list[-1].position())