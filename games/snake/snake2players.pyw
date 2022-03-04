from random import randrange, choice
from turtle import *
from freegames import vector, square
from threading import Thread

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
state = {'score1': 1, 'heighscore1': 1, 'score2': 1, 'heighscore2': 1, 'mode': 'normal'}
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
    writer1.color('white')
    writer1.goto(180, 180)
    writer1.color('black')
    writer1.write(str(state['heighscore1']) + '\n' + str(state['score1']))
    writer2.color('white')
    writer2.goto(-180, 180)
    writer2.color('black')
    writer2.write(str(state['heighscore2']) + '\n' + str(state['score2']))
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
    move()
def aiMovemant():
    global aim2
    global snake2
    global snake1
    global food
    global poisons
    global state
    global playing
    head = snake2[-1].copy()
    headUp = vector(head.x, head.y + 10)
    headDown = vector(head.x, head.y - 10)
    headLeft = vector(head.x - 10, head.y)
    headRight = vector(head.x + 10, head.y)
    options = []
    if not (headUp in poisons or headUp in snake1 or (headUp in snake2 and len(snake2)>1)) and inside(headUp):
        options.append(vector(0, 10))
    if not (headDown in poisons or headDown in snake1 or (headDown in snake2 and len(snake2)>1)) and inside(headDown):
        options.append(vector(0, -10))
    if not (headLeft in poisons or headLeft in snake1 or (headLeft in snake2 and len(snake2)>1)) and inside(headLeft):
        options.append(vector(-10, 0))
    if not (headRight in poisons or headRight in snake1 or (headRight in snake2 and len(snake2)>1)) and inside(headRight):
        options.append(vector(10, 0))
    aim2 = getAIVector(options)
        
def getAIVector(options):
    global aim2
    global snake2
    global snake1
    global food
    global poisons
    global state
    global playing
    newAim = vector(0, 0)

    distanceX = food.x - snake2[-1].x
    distanceY = food.y - snake2[-1].y
    answers = []
    if abs(distanceX) > abs(distanceY):
        if distanceX > 0:
            answers.append(vector(10, 0))
            if distanceY > 0:
                answers.append(vector(0, 10))
                answers.append(vector(0, -10))
                answers.append(vector(-10, 0))
            else:
                answers.append(vector(0, -10))
                answers.append(vector(0, 10))
                answers.append(vector(-10, 0))

        else:
            answers.append(vector(-10, 0))
            if distanceY > 0:
                answers.append(vector(0, 10))
                answers.append(vector(0, -10))
                answers.append(vector(10, 0))
            else:
                answers.append(vector(0, -10))
                answers.append(vector(0, 10))
                answers.append(vector(10, 0))
    else:
        if distanceY > 0:
            answers.append(vector(0, 10))
            if distanceX > 0:
                answers.append(vector(10, 0))
                answers.append(vector(-10, 0))
                answers.append(vector(0, -10))
            else:
                answers.append(vector(-10, 0))
                answers.append(vector(10, 0))
                answers.append(vector(0, -10))
        else:
            answers.append(vector(0, -10))
            if distanceX > 0:
                answers.append(vector(10, 0))
                answers.append(vector(-10, 0))
                answers.append(vector(0, 10))
            else:
                answers.append(vector(-10, 0))
                answers.append(vector(10, 0))
                answers.append(vector(0, 10))
    for answer in answers:
        if answer in options:
            return answer
    return vector(10, 0)

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
    if state['mode'].__contains__('hard'):
        aim1.x = x
        aim1.y = y
    else:
        if ((aim1.x == -x and aim1.x != 0) or (aim1.y == -y and aim1.y != 0)) and not (len(snake1) == 1):
            return
        aim1.x = x
        aim1.y = y



def change2(x, y):
    if state['mode'].__contains__('ai'):
        return
    elif state['mode'].__contains__('hard'):
        aim2.x = x
        aim2.y = y
    else:
        if ((aim2.x == -x and aim2.x != 0) or (aim2.y == -y and aim2.y != 0)) and not (len(snake2) == 1):
            return
        aim2.x = x
        aim2.y = y


def move():
    global score1
    global heighscore1
    global snake1
    global snake2
    global playing
    if playing or ((width*height/2000) < len(poisons)):
        if state['mode'].__contains__('ai'):
            aiMovemant()
        head1 = snake1[-1].copy()
        head1.move(aim1)
        head2 = snake2[-1].copy()
        head2.move(aim2)
        if state['mode'].__contains__('hard'):
            if len(snake1)>1:
                if head1 == snake1[-2]:
                    head1 = snake1[0].copy()
                    body = snake1[1].copy()
                    snake1 = snake1[::-1]
                    aim1.x = head1.x - body.x
                    aim1.y = head1.y - body.y
                    head1.move(aim1)
            if len(snake2)>1:
                if head2 == snake2[-2]:
                    head2 = snake2[0].copy()
                    body = snake2[1].copy()
                    snake2 = snake2[::-1]
                    aim2.x = head2.x - body.x 
                    aim2.y = head2.y - body.y
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
                square(body.x, body.y, 9, 'blue')
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
def startHard():
    global state
    global playing
    if not playing:
        state['mode'] = 'hard'
        writer1.undo()
        start()
def startAI():
    global state
    global playing
    if not playing:
        state['mode'] = 'ai'
        writer1.undo()
        start()
def startNormal():
    global state
    global playing
    if not playing:
        state['mode'] = 'normal'
        writer1.undo()
        start()
def startAIHard():
    global state
    global playing
    if not playing:
        state['mode'] = 'aihard'
        writer1.undo()
        start()

setup(width, height, 370, 100)
hideturtle()
tracer(False)
writer1.color('white')
writer1.goto(-100, 0)
writer1.color('black')
writer1.write('Press: 1 - hard, 2 - normal, 3 - AI normal, 4 - AI hard')

listen()
onkey(startHard, '1')
onkey(startNormal, '2')
onkey(startAI, '3')
onkey(startAIHard, '4')
onkey(lambda: change1(10, 0), 'Right')
onkey(lambda: change1(-10, 0), 'Left')
onkey(lambda: change1(0, 10), 'Up')
onkey(lambda: change1(0, -10), 'Down')
onkey(lambda: change2(10, 0), 'd')
onkey(lambda: change2(-10, 0), 'a')
onkey(lambda: change2(0, 10), 'w')
onkey(lambda: change2(0, -10), 's')

# if state['mode'] == 'ai':
#     thread = Thread(target=aiMovemant, args=())
#     thread.start()
done()
