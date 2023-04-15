from turtle import *
import time
from random import randint
import random
delay=0.2

def init_screen():
    scr=Screen()
    scr.bgcolor("sky blue")
    scr.title("game")
    scr.setup(width=800,height=600)
    scr.tracer(0)
    return scr

def init_snake_head():
    snake_head = Turtle()
    snake_head.shape('square')
    snake_head.color("blue")
    snake_head.goto(0,0)
    snake_head.penup()
    snake_head.direction="none"
    return snake_head


def make_border():
    border = Turtle()
    border.penup()
    border.shape('square')
    border.shapesize(stretch_len=40, stretch_wid=1)
    border.color("steel blue")
    border.setpos(0,-290)

    border1 = Turtle()
    border1.penup()
    border1.shape('square')
    border1.shapesize(stretch_len=40, stretch_wid=1)
    border1.color("steel blue")
    border1.setpos(0,300)

    border2=Turtle()
    border2.penup()
    border2.shape('square')
    border2.shapesize(stretch_len=1, stretch_wid=40)
    border2.color("steel blue")
    border2.setpos(385,0)

    border3=Turtle()
    border3.penup()
    border3.shape('square')
    border3.shapesize(stretch_len=1, stretch_wid=40)
    border3.color("steel blue")
    border3.setpos(-390,0)
    return border1 , border2 , border3 , border

def goup():
    if snake_head.direction!="down":
        snake_head.direction="up"
def godown():
    if snake_head.direction!="up":
        snake_head.direction="down"
def goright():
    if snake_head.direction!="left":
        snake_head.direction="right"
def goleft():
    if snake_head.direction!="right":
        snake_head.direction="left"

def init_food():
    food=Turtle()
    food.shape('circle')
    food.shapesize(1,1)
    food.color("olive")
    food.penup()
    food.speed(0)
    food.setpos(0,50)
    food.position()
    return food

def check_border(snake):
    if snake.xcor()>354 or snake.xcor()<-390 or snake.ycor()>300 or snake.ycor()<-290:
        snake.goto(0,0)
        snake.direction="stop"
        style = ('Courier', 40, 'italic')
        pen.write('GAME OVER', font=style)
        

def command(S):
    S.listen()
    S.onkey(goup,"Up")
    S.onkey(godown,"Down")
    S.onkey(goright,"Right")
    S.onkey(goleft,"Left")

def update_snake_head(snake):
    x,y = snake.position()
    if snake.direction=="down":
        snake.sety(y-15)
    if snake.direction=="up":
        snake.sety(y+15)
    if snake.direction=="left":
        snake.setx(x-15)
    if snake.direction=="right":
        snake.setx(x+15)

def eat_food():

    if snake_head.distance(food) < 10:
        x=random.randint(-200,200)
        y=random.randint(-200,200)
        food.goto(x,y)
        length =Turtle()
        length.speed(0)
        length.shape("square")
        length.color("blue")
        length.penup()
        snake_body.append(length)
       
    
        
    for i in range(len(snake_body)-1,0,-1):
            x = snake_body[i-1].xcor()
            y = snake_body[i-1].ycor()
            snake_body[i].goto(x,y)
    if len(snake_body)>0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        snake_body[0].goto(x,y)
        
def check_self(snake_body,snake): 
    for i in  range(len(snake_body)):
        for j in range(len(snake_body)):
            if i-j>3 and snake_body[i].distance(snake_body[j])<10:
             snake.goto(0,0)
             snake.direction="stop"  
             style = ('Courier', 40, 'italic') 
             pen.write('GAME OVER', font=style)
             
             
pen =Turtle()
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(-150, 100)



scr = init_screen()
snake_head = init_snake_head()
snake_body = []
food = init_food()
Game_over = False
command(scr)
while not Game_over:
    scr.update()
    update_snake_head(snake_head)
    time.sleep(0.05)
    make_border()
    check_border(snake_head)
    check_self(snake_body,snake_head)
    eat_food()
    Game_over=False
done()







