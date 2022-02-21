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
turtle.tracer(False)
Scoreboard = ScoreBoard()
Scoreboard.keep_score(Player_1_score,Player_2_score)
paddle1 = Paddle(-380)
paddle2 = Paddle(380)
Ball = Ball(paddle1,paddle2,Player_1_score,Player_2_score)

listOfObjects=[]
listOfObjects.append(paddle1)
listOfObjects.append(paddle2)
listOfObjects.append(Ball)
def moveAll(list):
  for i in list:
    i.move()
Screen.update()
gameCont = True
Screen.listen()
matches = 5
while Player_2_score<matches and Player_1_score<matches:
  #paddle1 controls
  Screen.onkey(key = "w",fun=paddle1.up)
  Screen.onkey(key="s",fun=paddle1.down)
  Screen.onkey(key = "Up",fun=paddle2.up)
  Screen.onkey(key="Down",fun=paddle2.down)
  Scoreboard.keep_score(Player_1_score, Player_2_score)
  moveAll(listOfObjects)
  if Ball.scored()== True:
    Player_1_score+=1
  elif Ball.scored() == False:
    Player_2_score+=1

  Screen.update()
  time.sleep(1/30)

if Player_1_score>Player_2_score:
  output = "<<<<LEFT SIDE WINS"
else:
  output = "RIGHT SIDE WINS>>>>"

sector.goto(-100,0)
sector.write(output,font=("Times New Roman)",32,'normal'))

Screen.exitonclick()

