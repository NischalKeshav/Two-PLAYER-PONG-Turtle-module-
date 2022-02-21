import turtle
import time
from turtle import Screen,Turtle
from scoreboard import ScoreBoard
from paddle import Paddle
Screen = Screen()
Screen.bgcolor("Black")
Screen.setup(width=800,height=600 )
sector = ScoreBoard()
Player_1_score = 0
Player_2_score = 0
turtle.tracer(False)
Scoreboard = ScoreBoard()
Scoreboard.keep_score(Player_1_score,Player_2_score)
paddle1 = Paddle(-380)
paddle2 = Paddle(380)
listOfObjects=[]
listOfObjects.append(paddle1)
listOfObjects.append(paddle2)

def moveAll(list):
  for i in list:
    i.move()
Screen.update()
gameCont = True
Screen.listen()
while gameCont:
  #paddle1 controls
  Screen.onkey(key = "w",fun=paddle1.up)
  Screen.onkey(key="s",fun=paddle1.down)
  Screen.onkey(key = "Up",fun=paddle2.up)
  Screen.onkey(key="Down",fun=paddle2.down)
  moveAll(listOfObjects)
  Screen.update()
  time.sleep(1/30)
  
  



