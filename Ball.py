from turtle import Turtle
import random
import time
class Ball(Turtle):
    def __init__(self,paddle1,paddle2,score1,score2):
        super().__init__()
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.color("Red")
        self.shape("circle")
        self.penup()
        self.listOfAngles = [1,2,3,-1,-2,-3]#list of different y adds to randomly choose at start
        self.YAdd = random.choice(self.listOfAngles) *3
        self.XAdd = random.choice((-3,3))
        self.X = self.xcor()
        self.Y = self.ycor()
        self.paddle1=paddle1
        self.paddle2=paddle2
        self.score1 = score1
        self.score2 = score2
    def move(self):
        self.X+=self.XAdd
        self.Y+=self.YAdd
        if self.Y>=295:
            self.YAdd = -1*(self.YAdd)
        elif self.Y<=-295:
            self.YAdd = -1*(self.YAdd)
        if self.distance(self.paddle1)<38 and self.XAdd <0:
            self.XAdd = -1*(self.XAdd)
        elif self.distance(self.paddle2)<38 and self.XAdd>0:
            self.XAdd = -1* self.XAdd

        self.goto(self.X,self.Y)
    def refresh(self):
        self.X = 0
        self.Y = 0
        self.YAdd = random.choice(self.listOfAngles) * 3
        self.XAdd = random.choice((-4, 4))
        time.sleep(1)

    def scored(self):
        self.X = self.xcor()
        if self.X>400:
            self.refresh()
            return True
        elif self.X<-400:
            self.refresh()
            return False
