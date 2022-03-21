from random import randint
from freegames import vector, floor
from turtle import *

writer = Turtle(visible=False)
height = 420
width = 420
squarePath = Turtle(visible=False)
LinePath = Turtle(visible=False)

def square(x, y, fuel):
    squarePath.up()
    squarePath.goto(x, y)
    squarePath.down()
    squarePath.begin_fill()
    for count in range(4):
        squarePath.forward(20)
        squarePath.left(90)
    squarePath.end_fill()
    squarePath.goto(x+10, y+5)
    squarePath.color('white')
    squarePath.write(fuel)
    squarePath.color('blue')


def line(x, y, angle):
    LinePath.up()
    LinePath.goto(x, y)
    LinePath.setheading(angle)
    LinePath.down()
    LinePath.forward(30)

class Dock:
    docks = []
    def __init__(self, coordinates, fuel, paths):
        self.coordinates = coordinates
        self.fuel = fuel
        self.paths = paths
        Dock.docks.append(self)
    def __str__(self):
        return "Dock: " + str(self.coordinates) + " Fuel: " + str(self.fuel) + " Paths: " + str(self.paths)
    def getNeighbors(self):
        answer = []
        for path in self.paths:
            if path[1] > 0:
                answer.append(path[0])
        return answer
    def getFuel(self):
        return self.fuel
    def getCoordinates(self):
        return self.coordinates
    def getPaths(self):
        return self.paths
    def getPath(self, dock):
        for path in self.paths:
            if path[0] == dock:
                return path
        return None
    def getPathFuel(self, dock):
        for path in self.paths:
            if path[0] == dock:
                return path[1]
        return None    
    def addPath(self, dock, fuel):
        self.paths.append((dock, fuel))
def world(docks):
    global height, width
    global path
    bgcolor('black')
    LinePath.color('blue')
    squarePath.color('blue')
    for dock in docks:
        x = (dock.getCoordinates().x * 40) - 200
        y = 180 - (dock.getCoordinates().y * 40)
        for dock2 in dock.getNeighbors():
            if dock2.getCoordinates().x == dock.getCoordinates().x:
                if dock2.getCoordinates().y > dock.getCoordinates().y:
                    line(x+10, y+10, 270)
                else:
                    line(x+10, y+10, 90)
            elif dock2.getCoordinates().y == dock.getCoordinates().y:
                if dock2.getCoordinates().x > dock.getCoordinates().x:
                    line(x+10, y+10, 0)
                else:
                    line(x+10, y+10, 180)
            else:
                if dock2.getCoordinates().x > dock.getCoordinates().x:
                    if dock2.getCoordinates().y > dock.getCoordinates().y:
                        line(x+10, y+10,315)
                    else:
                        line(x+10, y+10, 45)
                else:
                    if dock2.getCoordinates().y > dock.getCoordinates().y:
                        line(x+10, y+10, 225)
                    else:
                        line(x+10, y+10, 135)
        square(x, y, dock.getFuel())

    update()

for i in range(0,10):
    for j in range(0,10):
        Dock(vector(i,j), randint(1,10), [])
for dock in Dock.docks:
    for dock2 in Dock.docks:
        if dock != dock2 and (dock.getCoordinates() - dock2.getCoordinates()).__abs__() < 2:
            fuel = randint(1,10)
            dock.addPath(dock2, fuel)
            dock2.addPath(dock, fuel)
for dock in Dock.docks:
    print(dock.getCoordinates())
setup(width, height, 370, 100)
hideturtle()
tracer(False)
world(Dock.docks)
done()
