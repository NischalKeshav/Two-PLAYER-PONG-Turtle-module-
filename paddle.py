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
    self.shapesize(stretch_len=5,stretch_wid=.75)
    self.showturtle()
    self.head = 0
    self.setheading(90)
  def up(self):
    self.head = 3
  def down(self):
    self.head = -3
  def move(self):
    self.forward(self.head)
  
