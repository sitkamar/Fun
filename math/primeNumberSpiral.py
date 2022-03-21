from turtle import *
from freegames import vector, square, floor
import random
width = 500
height = 500
primes = [2]
def isPrime(num):
    global primes
    for prime in primes:
        if num % prime == 0:
            return False
    return True
def changeCoordinates(x, y, turn):
    if turn == 'left':
        return x-20, y
    elif turn == 'right':
        return x+20, y
    elif turn == 'up':
        return x, y+20
    elif turn == 'down':
        return x, y-20
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
def draw():
    global width, height
    clear()
    x = -5
    y = -5
    turn = 'right'
    turnCounter = 0
    stepsLine = 1
    for num in range(width*height//100):
        square(x, y, 5, 'black')
        x, y = changeCoordinates(x, y, turn)
        stepsLine-=1
        print(stepsLine,turn)
        if turnCounter % 2 == 0 and stepsLine <= 0:
            turn = changeTurn(turn)
            stepsLine = turnCounter/2
        
setup(width, height, 370, 100)
hideturtle()
tracer(False)
draw()
done()