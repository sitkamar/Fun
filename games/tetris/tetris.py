from random import choice
from turtle import *
from freegames import vector, floor
import json

state = {'score': 0, 'eating': 0, 'speed': 0,
         'moving': '', 'mode': 1, 'level': 1}
state['mode'] = int(input('Enter mode: '))
path = Turtle(visible=False)
writer = Turtle(visible=False)
def square(x, y):
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()
    for count in range(4):
        path.forward(20)
        path.left(90)
    path.end_fill()
def longPiece(x, y, r):
    if r == 0:
        square(x, y)
        square(x, y + 20)
        square(x, y + 40)
        square(x, y -20)
    else:
        square(x, y)
        square(x, y+20)
        square(x, y+40)
        square(x, y-20)
def s1Piece(x, y,r):
    if r == 0:
        square(x, y)
        square(x, y + 20)
        square(x-20, y + 20)
        square(x+20, y)
    else:
        square(x, y)
        square(x+20, y)
        square(x+20, y+20)
        square(x, y-20)
def s2Piece(x, y,r):
    if r == 0:
        square(x, y)
        square(x, y + 20)
        square(x+20, y + 20)
        square(x-20, y)
    else:
        square(x, y)
        square(x-20, y)
        square(x-20, y+20)
        square(x, y-20)
def l1Piece(x, y, r):
    if r == 0:
        square(x, y)
        square(x, y + 20)
        square(x, y + 20)
        square(x+20, y)
    else:
        square(x, y)
        square(x-20, y)
        square(x-40, y)
        square(x+20, y)
def l2Piece(x, y, r):
    if r == 0:
        square(x, y)
        square(x, y + 20)
        square(x, y + 40)
        square(x-20, y)
    else:
        square(x, y)
        square(x+20, y)
        square(x+40, y)
        square(x, y+20)

def offset(point):
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index


def world():
    bgcolor('black')
    path.color('white')
    for x in range(0, 300, 20):
        for y in range(0, 420, 20):
            square(x-220, 200-y)


def move():
    writer.undo()
    writer.write(state['score'])
    path.color('blue')
    if state['moving'] == '':
        state['moving'] = choice(['l', 's1', 's2', 'l1', 'l2','sq'])
    
    update()
    ontimer(move, 100)
def change(x,y):
    pass
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.goto(180, 160)
writer.color('white')
writer.write(state['score'])
listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world()
move()
done()
