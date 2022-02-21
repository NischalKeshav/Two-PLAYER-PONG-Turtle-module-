import turtle
from turtle import Screen,Turtle
from scoreboard import ScoreBoard
from paddle import Paddle
Screen = Screen()
Screen.bgcolor("Black")
Screen.setup(width=800,height=600 )
sector = ScoreBoard()
Player_1_score = 0
Player_2_score = 0
turtle.tracer(-1)
sector.keep_score(Player_1_score,Player_2_score)
paddle1 = Paddle(-380)
paddle2 = Paddle(380)
Screen.update()



