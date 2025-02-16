from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.cnt=0
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.write(f"Score : {self.cnt}", align="center", font=("Courier", 24, "normal"))
        self.hideturtle()

    def update(self):
        self.clear()
        self.cnt+=1
        self.color('white')
        self.penup()
        self.goto(0,270)

        self.write(f"Score : {self.cnt}", align="center", font=("Courier", 24, "normal"))
        self.hideturtle()

    def end(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))