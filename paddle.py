from turtle import Turtle
class Paddle(Turtle):
  def __init__(self,Xpos):
    super().__init__()
    self.Xpos = Xpos
    self.Ypos = 0
    self.hideturtle()
    self.goto(self.Xpos,self.Ypos)
    self.penup()
    self.color("white")
    self.shape("square")
    self.shapesize(stretch_len=.8,stretch_wid=5)
    self.showturtle()
