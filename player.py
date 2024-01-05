
from turtle import Screen, Turtle

class Player(Turtle):
    def __init__(self,x_pos=350,y_pos=0,width=5,height=1):
        super().__init__()

        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.shapesize(self.width,self.height)
        self.penup()
        self.shape("square")
        self.goto(self.x_pos,self.y_pos)
        self.color("white")


    def up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(),new_y)

    def down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(),new_y)