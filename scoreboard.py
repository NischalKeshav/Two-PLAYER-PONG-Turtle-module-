import turtle
from turtle import Turtle
class ScoreBoard(Turtle):#define class
  def __init__(self):  
    super().__init__()#self is turtle
    self.hideturtle()#hides turtle since it does not need to be seen
    self.color('White')#color
    self.speed('fastest')#fastes speed
    self.penup()#draws middle line
    self.goto(0,-300)#
    self.setheading(90)#
    self.len = 15#
    for i in range(21):  #
        self.forward(self.len)#
        self.pendown()#
        self.forward(self.len)#
        self.penup()#
    self.goto(-45,270)#
  def keep_score(self,score1,score2): # function to keep score on scree
      self.clear()
      self.write(f"{score1}        {score2}",font=("Times New Roman",32,'normal'))
    

