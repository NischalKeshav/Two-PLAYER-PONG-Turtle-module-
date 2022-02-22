from turtle import Turtle
class Paddle(Turtle):
  def __init__(self,Xpos):
    super().__init__()#self = turtle
    self.Xpos = Xpos#start position
    self.Ypos = 0#
    self.hideturtle()#hides to start up turtle
    self.goto(self.Xpos,self.Ypos)# goes to position
    self.penup()#pen up to not draw during game
    self.color("white")#Settings
    self.shape("square")
    self.shapesize(stretch_len=5,stretch_wid=.75)#resize
    self.showturtle()
    self.head = 0#direction
    self.setheading(90)#heading is set upwards to go one direction
  def up(self):#Funcs for up and down on key presses
    self.head = 8
  def down(self):#
    self.head =-8
  def move(self):# every new frame
    self.Ypos = self.ycor()
    if (self.head<0 and self.Ypos<=-240) or (self.head >0 and  self.Ypos>=240):
      self.head = self.head
    else:
      self.forward(self.head)
  
