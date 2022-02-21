import turtle
from turtle import Turtle
class ScoreBoard(Turtle):    
  def __init__(self):  
    super().__init__()
    self.hideturtle()
    self.color('White')
    self.speed('fastest')
    self.penup()
    self.goto(0,-300)
    self.setheading(90)
    self.len = 15
    for i in range(21):  
        self.forward(self.len)
        self.pendown()
        self.forward(self.len)
        self.penup()
    self.goto(-45,270)
  def keep_score(self,score1,score2): 
      self.clear()
      self.write(f"{score1}        {score2}",font=("Times New Roman",22,'normal'))
    

