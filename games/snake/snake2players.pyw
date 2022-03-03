from random import randrange, choice
from turtle import *
from freegames import vector, square

food = vector(0, 0)
poisons = [vector(100, 0)]
snake1 = [vector(10, 0)]
snake2 = [vector(-10, 0)]
savePlace = []
for i in range(5):
    for j in range(5):
        savePlace.append(vector(i*10, j*10))
aim1 = vector(0, -10)
aim2 = vector(0, -10)
state = {'score1': 1, 'heighscore1': 1, 'score2': 1, 'heighscore2': 1}
height = 420
width = 420
playing = False
writer1 = Turtle(visible=False)
writer2 = Turtle(visible=False)


def start():
    global aim1
    global snake1
    global food
    global poisons
    global state
    global playing
    clear()
    playing = True
    food = vector(0, 0)
    poisons = [vector(100, 0)]
    snake1 = [choice(savePlace)]
    while snake1 in snake2:
        snake1 = [choice(savePlace)]
    aim1 = vector(0, -10)
    if state['score1'] > state['heighscore1']:
        state['heighscore1'] = state['score1']
    state['score1'] = 1
    writer1.undo()
    writer1.write(str(state['heighscore1']) + '\n' + str(state['score1']))
    update()


def reset1():
    global aim1
    global snake1
    global food
    global poisons
    global state
    global playing
    aim1 = vector(0, -10)
    snake1 = [choice(savePlace)]
    while(snake1 in snake2):
        snake1 = [choice(savePlace)]
    if state['score1'] > state['heighscore1']:
        state['heighscore1'] = state['score1']
    state['score1'] = 1
    writer1.undo()
    writer1.write(str(state['heighscore1']) + '\n' + str(state['score1']))


def reset2():
    global aim2
    global snake2
    global food
    global poisons
    global state
    global playing
    aim2 = vector(0, -10)
    snake2 = []
    snake2.append(choice(savePlace))
    while snake2[0] in snake1:
        snake2 = []
        snake2.append(choice(savePlace))
    if state['score2'] > state['heighscore2']:
        state['heighscore2'] = state['score2']
    state['score2'] = 1
    writer2.undo()
    writer2.write(str(state['heighscore2']) + '\n' + str(state['score2']))


def inside(head):
    return -width/2 < head.x < width/2 and -height/2 < head.y < height/2


def change1(x, y):
    if ((aim1.x == -x and aim1.x != 0) or (aim1.y == -y and aim1.y != 0)) and not (len(snake1) == 1):
        return
    aim1.x = x
    aim1.y = y


def change2(x, y):
    if ((aim2.x == -x and aim2.x != 0) or (aim2.y == -y and aim2.y != 0)) and not (len(snake2) == 1):
        return
    aim2.x = x
    aim2.y = y


def move():
    global score1
    global heighscore1
    global playing
    if playing or ((width*height/2000) < len(poisons)):
        head1 = snake1[-1].copy()
        head1.move(aim1)
        head2 = snake2[-1].copy()
        head2.move(aim2)
        if head1 == head2:
            square(head1.x, head1.y, 9, 'red')
            reset1()
            reset2()
        elif not inside(head1) or head1 in snake1 or head1 in poisons or head1 in snake2:
            square(head1.x, head1.y, 9, 'red')
            reset1()
        elif not inside(head2) or head2 in snake2 or head2 in poisons or head2 in snake1:
            square(head2.x, head2.y, 9, 'red')
            reset2()
        else:
            snake1.append(head1)
            snake2.append(head2)
            if head1 == food:
                state['score1'] = len(snake1)
                snake2.pop(0)
            elif head2 == food:
                state['score2'] = len(snake2)
                snake1.pop(0)
            if head1 == food or head2 == food:
                food.x = randrange(round(-width/20)+1, round(width/20)-1)*10
                food.y = randrange(round(-height/20)+1, round(height/20)-1)*10
                while food in snake1 or food in poisons or food in snake2:
                    food.x = randrange(round(-width/20)+1,
                                       round(width/20)-1)*10
                    food.y = randrange(round(-height/20)+1,
                                       round(height/20)-1)*10
                poison = vector(randrange(round(-width/20)+1, round(width/20)-1)
                                * 10, randrange(round(-height/20)+1, round(height/20)-1)*10)
                while poison in snake1 or poison in food or poison in snake2 or poison in savePlace:
                    poison = vector(randrange(round(-width/20)+1, round(width/20)-1)
                                    * 10, randrange(round(-height/20)+1, round(height/20)-1)*10)
                poisons.append(poison)
                writer1.undo()
                writer1.write(str(state['heighscore1']) +
                              '\n' + str(state['score1']))
                writer2.undo()
                writer2.write(str(state['heighscore2']) +
                              '\n' + str(state['score2']))
            else:
                snake1.pop(0)
                snake2.pop(0)
            clear()
            for body in snake1:
                square(body.x, body.y, 9, 'yellow')
            for body in snake2:
                square(body.x, body.y, 9, 'black')
            square(food.x, food.y, 9, 'green')
            for poison in poisons:
                square(poison.x, poison.y, 9, 'red')
        update()
        ontimer(move, 100)
    else:
        clear()
        writer1.undo()
        writer1.color('white')
        writer1.move()
        writer1.color('black')
        if score1 > score2:
            writer1.write('Player 1 wins!')
        else:
            writer1.write('Player 2 wins!')
        update()



setup(width, height, 370, 100)
listen()
onkey(lambda: change1(10, 0), 'Right')
onkey(lambda: change1(-10, 0), 'Left')
onkey(lambda: change1(0, 10), 'Up')
onkey(lambda: change1(0, -10), 'Down')
onkey(lambda: change2(10, 0), 'd')
onkey(lambda: change2(-10, 0), 'a')
onkey(lambda: change2(0, 10), 'w')
onkey(lambda: change2(0, -10), 's')
onkey(start, 'space')
hideturtle()
tracer(False)
writer1.color('white')
writer1.goto(180, 180)
writer1.color('black')
writer1.write(str(state['heighscore1']) + '\n' + str(state['score1']))
writer2.color('white')
writer2.goto(-180, 180)
writer2.color('black')
writer2.write(str(state['heighscore2']) + '\n' + str(state['score2']))
start()
move()
done()
