from random import choice
from turtle import *
from freegames import vector, floor
import json

state = {'score': 0, 'eating': 0, 'speed': 0,
         'playing': True, 'mode': 1, 'level': 1, 'heighscore': 0}
aimNext = vector(0, 0)
aim = vector(0, 0)
pacmanStart = vector(0, 0)
pacman = vector(-40, -80)
startghosts = []
ghosts = []
tilesStart = []
tiles = []
path = Turtle(visible=False)
writer = Turtle(visible=False)
jsonFile = ".\levels.json"
reader = open(jsonFile,'r')
levels = json.load(reader)
reader.close()

def square(x, y):
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()
    for count in range(4):
        path.forward(20)
        path.left(90)
    path.end_fill()


def offset(point):
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index


def valid(point):
    index = offset(point)
    if tiles[index] == 0:
        return False
    index = offset(point + 19)
    if tiles[index] == 0:
        return False
    return point.x % 20 == 0 or point.y % 20 == 0


def world():
    bgcolor('black')
    path.color('blue')
    for index in range(len(tiles)):
        if tiles[index] > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)
            if tiles[index] == 1:
                path.up()
                path.goto(x+10, y+10)
                path.dot(4, 'white')
            if tiles[index] == 3:
                path.up()
                path.goto(x+10, y+10)
                path.dot(8, 'white')
    state['playing'] = True

def initialize(starting):
    global ghosts, pacman, tiles, startghosts, pacmanStart, tilesStart, levels
    state['playing'] = False
    if state['score'] > state['heighscore']:
        state['heighscore'] = state['score']
    if starting:
        state['score'] = 0
        state['eating'] = 0
    if state['level'] > len(levels['levels']):
        print("You win!")
        print("Your score is: " + str(state['score']))
    tilesStart = levels['levels'][str(state['level'])]['tiles'].copy()
    startghostsHelp = levels['levels'][str(state['level'])]['ghosts'].copy()
    for ghost in startghostsHelp:
        startghosts.append(vector(ghost[0], ghost[1]))
    pacmanStart = vector(levels['levels'][str(state['level'])]['pacman'][0], levels['levels'][str(state['level'])]['pacman'][1])
    ghosts = []
    for ghost in startghosts:
        ghosts.append([ghost.copy(), vector(5, 0), -1])
    pacman = pacmanStart.copy()
    tiles = tilesStart.copy()
    world()

def end():
    global tiles
    if not 1 in tiles:
        state['level'] += 1
        state['eating'] = 0
        initialize(False)
        return True
    return False
    
def move():
    writer.undo()
    writer.write(str(state['heighscore'])+'\n' + str(state['score']))
    state['eating'] -= 1
    clear()
    if not end():
        if valid(pacman + aimNext) and (aim.x != aimNext.x or aim.y != aimNext.y):
            aim.x = aimNext.x
            aim.y = aimNext.y
        if valid(pacman + aim):
            pacman.move(aim)
        index = offset(pacman)

        if tiles[index] == 1:
            tiles[index] = 2
            state['score'] += 1
            x = (index % 20)*20 - 200
            y = 180 - (index // 20)*20
            square(x, y)
        if tiles[index] == 3:
            tiles[index] = 2
            x = (index % 20)*20 - 200
            y = 180 - (index // 20)*20
            square(x, y)
            state['eating'] = 100
        up()
        goto(pacman.x + 10, pacman.y + 10)
        dot(20, 'yellow')
        for ghost in ghosts:
            if ghost[2] > 0:
                ghost[2] -= 1
            elif ghost[2] == 0:
                ghost[2] -= 1
                startghostsHelp = []
                for option in startghosts:
                    startghostsHelp.append(option.copy())
                ghost[0] = choice(startghostsHelp)
            options = []
            if valid(ghost[0] + ghost[1]):
                options.append(ghost[1])
            if valid(ghost[0] + vector(ghost[1].y, ghost[1].x)):
                options.append(vector(ghost[1].y, ghost[1].x))
            if valid(ghost[0] - vector(ghost[1].y, ghost[1].x)):
                options.append(vector(ghost[1].y, ghost[1].x) * -1)
            if valid(ghost[0] - ghost[1]) and len(options) > 1 or len(options) == 0:
                options.append(ghost[1] * -1)
            if len(options) < 3 and ghost[1] in options:
                pass
            elif state['mode'] == 1:
                ghost[1] = direction(ghost, options)
            else:
                ghost[1] = choice(options)
            if state['eating'] > 0:
                ghost[0].move(ghost[1]/5)
                up()
                goto(ghost[0].x + 10, ghost[0].y + 10)
                dot(20, 'purple')
            else:
                ghost[0].move(ghost[1])
                up()
                goto(ghost[0].x + 10, ghost[0].y + 10)
                dot(20, 'red')
            if state['eating'] <= 0:
                if crash(ghost):
                    initialize(True)
            else:
                if crash(ghost):
                    ghost[2] = 100
                    ghost[0] = vector(-20, -20)
                    state['score'] += 10
    update()
    ontimer(move, 100)


def crash(ghost):
    x = ghost[0].x
    y = ghost[0].y
    return floor(x, 20) == floor(pacman.x, 20) and floor(y, 20) == floor(pacman.y, 20)


def direction(ghost, options):
    x = pacman.x - ghost[0].x
    y = pacman.y - ghost[0].y
    answers = []
    if abs(x) > abs(y):
        if x > 0:
            if y > 0:
                answers.append(vector(5, 0))
                answers.append(vector(0, 5))
                answers.append(vector(-5, 0))
                answers.append(vector(0, -5))
            else:
                answers.append(vector(5, 0))
                answers.append(vector(0, -5))
                answers.append(vector(-5, 0))
                answers.append(vector(0, 5))
        else:
            if y > 0:
                answers.append(vector(-5, 0))
                answers.append(vector(0, 5))
                answers.append(vector(5, 0))
                answers.append(vector(0, -5))
            else:
                answers.append(vector(-5, 0))
                answers.append(vector(0, -5))
                answers.append(vector(5, 0))
                answers.append(vector(0, 5))
    else:
        if y > 0:
            if x > 0:
                answers.append(vector(0, 5))
                answers.append(vector(5, 0))
                answers.append(vector(0, -5))
                answers.append(vector(-5, 0))
            else:
                answers.append(vector(0, 5))
                answers.append(vector(5, 0))
                answers.append(vector(0, -5))
                answers.append(vector(-5, 0))
        else:
            if x > 0:
                answers.append(vector(0, -5))
                answers.append(vector(5, 0))
                answers.append(vector(0, 5))
                answers.append(vector(-5, 0))
            else:
                answers.append(vector(0, -5))
                answers.append(vector(-5, 0))
                answers.append(vector(0, 5))
                answers.append(vector(5, 0))
    if state['eating'] > 0:
        for i in range(4):
            if answers[4 - i - 1] in options:
                return answers[4 - i - 1]
    else:
        for answer in answers:
            if answer in options:
                return answer


def change(x, y):
    aimNext.x = x
    aimNext.y = y
    
    
while True:
    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    writer.goto(180, 160)
    writer.color('white')
    writer.write(str(state['heighscore'])+'\n' + str(state['score']))
    listen()
    onkey(lambda: change(5, 0), 'Right')
    onkey(lambda: change(-5, 0), 'Left')
    onkey(lambda: change(0, 5), 'Up')
    onkey(lambda: change(0, -5), 'Down')
    initialize(True)
    move()
    done()
