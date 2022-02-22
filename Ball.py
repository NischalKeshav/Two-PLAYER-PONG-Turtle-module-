from turtle import Turtle
import random
import time
class Ball(Turtle):
    def __init__(self,paddle1,paddle2,score1,score2):
        super().__init__()#self = turtle
        self.shapesize(stretch_wid=.75,stretch_len=.75)#make it smaller
        self.color("Red")#settings#
        self.shape("circle")
        self.penup()
        self.listOfAngles = [2,3,-2,-3]#list of different y adds to randomly choose at start
        self.YAdd = random.choice(self.listOfAngles) *3
        self.XAdd = random.choice((-3,3))*random.randrange(1,3)#
        self.X = self.xcor()#X position
        self.Y = self.ycor()#Y position
        self.paddle1=paddle1
        self.paddle2=paddle2
        self.score1 = score1
        self.score2 = score2
    def move(self):#all things procceded per frame
        self.X+=self.XAdd
        self.Y+=self.YAdd
        if self.Y>=290:
            self.YAdd = -1*(self.YAdd)
        elif self.Y<=-290:
            self.YAdd = -1*(self.YAdd)
        if self.distance(self.paddle1)<50 and self.XAdd <0 and self.X<-365:
            self.XAdd = -1*(self.XAdd)
        elif self.distance(self.paddle2)<50 and self.XAdd>0 and self.X>365:
            self.XAdd = -1* self.XAdd

        self.goto(self.X,self.Y)
    def refresh(self):#New game Func
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
