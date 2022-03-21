from turtle import *
from freegames import vector, square, floor
import random
tiles = []
mines = []
state = {'playing': True, 'win': False}
writer = Turtle(visible=False)
def generaet_tiles():
    global tiles
    global mines
    mines = []
    tiles = []
    for i in range(20):
        x = random.randint(-10, 10)*20
        y = random.randint(-9, 9)*20
        mines.append(vector(x, y))
    for x in range(-200, 200, 20):
        for y in range(180, -200, -20):
            if vector(x, y) not in mines:
                num = 0
                neighbors = getNeighbors(x, y)
                for neighbor in neighbors:
                    if neighbor in mines:
                        num += 1
                tiles.append([vector(x, y), 0, num])
            else:
                tiles.append([vector(x, y), 0, -1])
def draw_tiles():
    clear()
    for tile in tiles:
        square(tile[0].x, tile[0].y, 20, 'black')
def getNeighbors(x, y):
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0 or (x+i*20) < -200 or (x+i*20) >= 200 or (y+j*20) < -180 or (y+j*20) > 180:
                pass
            else:
                neighbors.append(vector(x+i*20, y+j*20))
    return neighbors
def color(num):
    if num == 0:
        return 'blue'
    elif num == 1:
        return 'white'
    elif num == 2:
        return 'yellow'
    elif num == 3:
        return 'orange'
    elif num == 4:
        return 'red'
    else:
        return 'purple'
def update_tile(x, y):
    tile = check_tiles(x, y)
    if tile[1] == 0:
        square(tile[0].x, tile[0].y, 20, 'black')
    elif tile[1] == 2:
        square(tile[0].x+5, tile[0].y+5, 10, 'red')
    else:
        if tile[2] == 0:
            square(tile[0].x, tile[0].y, 20, 'blue')
            for neighbor in getNeighbors(x, y):
                tile2 = check_tiles(neighbor.x, neighbor.y)
                if not tile2[1] and tile2[2] == 0:
                    tile2[1] = True
                    update_tile(neighbor.x, neighbor.y)
        elif tile[2] == -1:
            square(tile[0].x, tile[0].y, 20, 'red')
        else:
            square(tile[0].x, tile[0].y, 20, 'blue')
            writer.up()
            writer.goto(tile[0].x+10, tile[0].y+5)
            writer.down()
            writer.color(color(tile[2]))
            writer.write(tile[2])
def check_tiles(x, y):
    for tile in tiles:
        if tile[0].x == x and tile[0].y == y:
            return tile
def checkWin():
    for tile in tiles:
        if tile[1] == 0 or (tile[2] != -1 and tile[1] == 2):
            return False
    return True
def win():
    state['playing'] = False
    clear()
    writer.clear()
    writer.up()
    writer.goto(0, 0)
    writer.write('You win')
    writer.goto(0, -20)
    writer.write('Click to play again')
    update()
def click(x, y):
    if state['playing']:
        if checkWin():
            win()
        else:
            x = floor(x, 20)
            y = floor(y, 20)
            tile = check_tiles(x, y)
            if tile[1] == 0 or tile[1] == 2:
                tile[1] = 1
                if tile[2] == -1:
                    end()
                update_tile(x, y)
    else:
        clear()
        writer.clear()
        generaet_tiles()
        draw_tiles()
        state['playing'] = True
def mark(x, y):
    if state['playing']:
        x = floor(x, 20)
        y = floor(y, 20)
        tile = check_tiles(x, y)
        if tile[1] == 0:
            tile[1] = 2
            update_tile(x, y)
def end():
    state['playing'] = False
    clear()
    writer.clear()
    writer.up()
    writer.goto(0, 0)
    writer.write('You lose')
    writer.goto(0, -20)
    writer.write('Click to play again')
    update()
setup(420, 420, 370, 100)
hideturtle()
tracer(False)
generaet_tiles()
draw_tiles()
listen()
onscreenclick(lambda x, y: click(x,y),1)
onscreenclick(lambda x, y: mark(x,y),3)
done()