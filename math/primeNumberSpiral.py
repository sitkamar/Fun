from turtle import *
from freegames import vector, square, floor
import random
width = 500
height = 500
primes = []
linePath = Turtle(visible=False)
numWriter = Turtle(visible=False)
numWriter.color('blue')
scale = 5
spaces = 0
def isPrime(num):
    global primes
    if num == 1:
        return False
    for prime in primes:
        if num % prime == 0:
            return False
    primes.append(num)
    return True
def changeCoordinates(x, y, turn):
    if turn == 'left':
        return x-scale-spaces, y
    elif turn == 'right':
        return x+scale+spaces, y
    elif turn == 'up':
        return x, y+scale+spaces
    elif turn == 'down':
        return x, y-spaces-scale
    return -1, -1
def changeTurn(turn):
    if turn == 'right':
        return 'up'
    elif turn == 'up':
        return 'left'
    elif turn == 'left':
        return 'down'
    elif turn == 'down':
        return 'right'
def line(x, y, prevX, prevY):
    linePath.up()
    linePath.goto(x+scale/2, y+scale/2)
    linePath.down()
    linePath.goto(prevX+scale/2, prevY+scale/2)
def write(x, y, text):
    numWriter.up()
    numWriter.goto(x, y)
    numWriter.down()
    numWriter.write(text)
def draw():
    global width, height
    clear()
    x = -scale/2
    y = -scale/2
    prevX = x
    prevY = y
    turn = 'right'
    turnCounter = 0
    stepsLine = 1
    square(x, y, scale, 'black')
    #write(x+scale/2, y+scale/2, '1')
    for num in range(2,int(((width*height)//((scale+spaces)*(scale+spaces))))+1):
        if stepsLine == 0:
            turn = changeTurn(turn)
            stepsLine = floor(turnCounter/2, 1) + 1
            if turn == 'left' or turn == 'right':
                stepsLine += 1
            turnCounter += 1
        x, y = changeCoordinates(x, y, turn)
        if isPrime(num):
            square(x, y, scale, 'red')
        else:
            square(x, y, scale, 'black')
        #write(x+scale/2, y+scale/2, num)
        line(x, y, prevX, prevY)
        prevX, prevY = x, y
        stepsLine -= 1
    line(x, y, prevX, prevY)
setup(width, height, 370, 100)
hideturtle()
tracer(False)
draw()
done()