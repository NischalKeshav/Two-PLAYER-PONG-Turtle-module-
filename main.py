import turtle
import time
from turtle import Screen,Turtle
from scoreboard import ScoreBoard
from paddle import Paddle
from Ball import Ball
Screen = Screen()
Screen.bgcolor("Black")
Screen.setup(width=800,height=600 )
sector = ScoreBoard()
Player_1_score = 0
Player_2_score = 0
turtle.tracer(False)# set tracer to False for complex graphics
Scoreboard = ScoreBoard()# Score Keep
Scoreboard.keep_score(Player_1_score,Player_2_score)
paddle1 = Paddle(-380)#paddles and paddle X positions
paddle2 = Paddle(380)#
Ball = Ball(paddle1,paddle2,Player_1_score,Player_2_score)#Ball object

listOfObjects=[]
listOfObjects.append(paddle1)#appends all objects to list Of objects
listOfObjects.append(paddle2)#
listOfObjects.append(Ball)#
def moveAll(list): # Activates the move func for all in list
  for i in list:
    i.move()
Screen.update()
gameCont = True   # if true continue game
Screen.listen()#Allows us to read the key inputs
matches = 3 # number of matches needed to win
while Player_2_score<matches and Player_1_score<matches:
  #paddle1 controls
  Screen.onkey(key = "w",fun=paddle1.up)
  Screen.onkey(key="s",fun=paddle1.down)
  #paddle2 controls
  Screen.onkey(key = "Up",fun=paddle2.up)
  Screen.onkey(key="Down",fun=paddle2.down)
  Scoreboard.keep_score(Player_1_score, Player_2_score)
  moveAll(listOfObjects)
  if Ball.scored()== True:#decides who gets a point
    Player_1_score+=1
  elif Ball.scored() == False:
    Player_2_score+=1

  Screen.update()
  time.sleep(1/30)
Scoreboard.keep_score(Player_1_score,Player_2_score)
if Player_1_score>Player_2_score:#decides who wins
  output = "<<<<LEFT SIDE WINS"
else:
  output = "RIGHT SIDE WINS>>>>"

sector.goto(-200,0)
sector.write(output,font=("Times New Roman)",32,'normal'))

Screen.exitonclick()

