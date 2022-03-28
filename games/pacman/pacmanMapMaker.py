from turtle import *
from freegames import vector, floor
import json

tiles = []
ghosts = []
pacman = vector(0, 0)
path = Turtle(visible=False)
jsonFile = "D:\Programming\Fun\games\pacman\levels.json"
reader = open(jsonFile, 'r')
levels = json.load(reader)
reader.close()
state = {'mode': 'n', 'level': len(levels["levels"])}


def initialize():
    global tiles, pacman, ghosts, levels
    state['mode'] = input('Editing(e), new(n): ')
    if state['mode'] == 'e':
        state['level'] = input('Enter level: ')
        tiles = levels["levels"][state['level']]["tiles"]
        ghostsHelp = levels["levels"][state['level']]["ghosts"]
        for ghost in ghostsHelp:
            ghosts.append(vector(ghost[0], ghost[1]))
        pacman = vector(levels["levels"][state['level']]["pacman"]
                        [0], levels["levels"][state['level']]["pacman"][1])
    else:
        tiles = [0] * 400
        ghosts = []
        pacman = vector(0, 0)
    world()


def square(x, y):
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()
    for count in range(4):
        path.forward(20)
        path.left(90)
    path.end_fill()


def world():
    bgcolor('black')
    path.color('blue')
    for index in range(len(tiles)):
        if tiles[index] == 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            path.color('black')
            square(x, y)
        elif tiles[index] > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            path.color('blue')
            square(x, y)
            if tiles[index] == 1:
                path.up()
                path.goto(x+10, y+10)
                path.dot(2, 'white')
            if tiles[index] == 3:
                path.up()
                path.goto(x+10, y+10)
                path.dot(8, 'white')
    for ghost in ghosts:
        up()
        goto(ghost.x + 10, ghost.y + 10)
        dot(20, 'red')
    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')
    update()


def click(x, y):
    newX = (floor(x, 20) + 200) / 20
    newY = (180 - floor(y, 20)) / 20
    index = int(newX + newY * 20)
    if tiles[index] == 0:
        tiles[index] = 1
    elif tiles[index] == 1:
        tiles[index] = 2
    elif tiles[index] == 2:
        tiles[index] = 3
    elif tiles[index] == 3:
        tiles[index] = 0
    world()
    update()


def send():
    global jsonFile
    writer = open(jsonFile, 'w')
    ghostsHelp = []
    save = input('Save as new(n), replace(r): ')
    for ghost in ghosts:
        ghostsHelp.append([ghost.x, ghost.y])
    newLevel = {"tiles": tiles, "pacman": [
        pacman.x, pacman.y], "ghosts": ghostsHelp}
    if save == 'n':
        num = len(levels["levels"])+1
        levels["levels"][num] = newLevel
    elif save == 'r':
        levels["levels"][state['level']] = newLevel
    json.dump(levels, writer)


def figurs(x, y):
    global pacman
    if vector(floor(x, 20), floor(y, 20)) in ghosts:
        pacman = vector(floor(x, 20), floor(y, 20))
        ghosts.remove(vector(floor(x, 20), floor(y, 20)))
    elif vector(floor(x, 20), floor(y, 20)) == pacman:
        pacman = vector(0, 0)
    else:
        ghosts.append(vector(floor(x, 20), floor(y, 20)))
    world()


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
initialize()
listen()
onscreenclick(lambda x, y: click(x, y), 1)
onscreenclick(lambda x, y: figurs(x, y), 3)
onkey(send, 'space')
world()
done()
