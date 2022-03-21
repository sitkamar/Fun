from random import randrange, choice
from turtle import *
from freegames import vector, square, floor

ball = vector(0, 0)
aim1 = vector(0, 0)
aim2 = vector(0, 0)
aimBall = vector(0, 0)
maxSpeed = 15
topPaddle1 = [vector(-200, 200),vector(-200, 190),vector(-200, 180),vector(-200, 170), vector(-200,160)]
topPaddle2 = [vector(190, 200),vector(190, 190),vector(190, 180),vector(190, 170), vector(190,160)]
bottomPaddle1 = [vector(-200, -200),vector(-200, -190),vector(-200, -180),vector(-200, -170), vector(-200, -160)]
bottomPaddle2 = [vector(190, -200),vector(190, -190),vector(190, -180),vector(190, -170), vector(190, -160)]
paddle1Start = [vector(-200, -10),vector(-200, 0),vector(-200, 10),vector(-200, 20), vector(-200, 30)]
paddle2Start = [vector(190, -10),vector(190, 0),vector(190, 10),vector(190, 20), vector(190, 30)]
paddle1 = paddle1Start
paddle2 = paddle2Start
throws = [vector(5, 10),vector(10, 5),vector(-10, 5),vector(-5, 10),vector(5, -10),vector(-5, -10),vector(10, -5),vector(-10, -5)]
state = {'score1': 1, 'heighscore1': 1, 'score2': 1, 'heighscore2': 1, 'mode': 'normal'}
height = 420
width = 420
playing = False
writer1 = Turtle(visible=False)
writer2 = Turtle(visible=False)
paddler = Turtle(visible=False)
baller = Turtle(visible=False)

def square(x, y, drawer):
    drawer.up()
    drawer.goto(x, y)
    drawer.down()
    drawer.begin_fill()
    drawer.forward(10)
    drawer.left(90)
    drawer.forward(10)
    drawer.left(90)
    drawer.forward(10)
    drawer.left(90)
    drawer.forward(10)
    drawer.left(90)
    drawer.end_fill()

def start():
    global aim1
    global aim2, paddle1, paddle2, ball
    global state, throws, aimBall
    global playing
    clear()    
    playing = True
    ball = vector(0, 0)
    aim1 = vector(0, 0)
    aim2 = vector(0, 0)
    aimBall = choice(throws)
    paddle1 = paddle1Start
    paddle2 = paddle2Start
    state['score1'] = 0
    state['score2'] = 0
    writer1.undo()
    writer1.write(str(state['score1']))    
    writer1.up()
    writer1.goto(180, 180)
    writer1.color('black')
    writer1.write(str(state['score1']))
    writer2.up()
    writer2.color('white')
    writer2.goto(-180, 180)
    writer2.color('black')
    writer2.write(str(state['score2']))
    update()
    move()
def aiMovemant():
    pass
def inside(head):
    return -width/2 < head.x < width/2 and -height/2 < head.y < height/2

def paddleCollision():
    global paddle1, paddle2, aimBall, ball, aim1, aim2
    paddle1Top = paddle1[-1].y
    paddle1Bottom = paddle1[0].y
    paddle2Top = paddle2[-1].y
    paddle2Bottom = paddle2[0].y
    if aim1.y > 0:
        paddle1Bottom-=aim1.y
    elif aim1.y < 0:
        paddle1Top-=aim1.y
    if aim2.y > 0:
        paddle2Bottom-=aim2.y
    elif aim2.y < 0:
        paddle2Top-=aim2.y
    if ball.x < -180 and paddle1Bottom < ball.y < paddle1Top and aimBall.x < 0:
        aimBall.x *= -2
        if aim1.y != 0:
            aimBall.y += aim1.y
        fixBallSpeed()
    if 180 < ball.x and paddle2Bottom < ball.y < paddle2Top and aimBall.x > 0:
        aimBall.x *= -2
        if aim2.y != 0:
            aimBall.y += aim2.y
        fixBallSpeed()
    
def change2(up, push):
    global aim2
    if up:
        if push:
            aim2.y = 15
        else:
            aim2.y = 0
    else:
        if push:
            aim2.y = -15
        else:
            aim2.y = 0
def change1(up, push):
    global aim1
    if up:
        if push:
            aim1.y = 15
        else:
            aim1.y = 0
    else:
        if push:
            aim1.y = -15
        else:
            aim1.y = 0
def movePaddles():
    global paddle1, paddle2, aim1, aim2, topPaddle1, topPaddle2, bottomPaddle1, bottomPaddle2
    global state, paddler
    paddler.clear()
    if vector(-200, 200) in paddle1 and aim1.y > 0:
        aim1 = vector(0, 0)
        paddle1 = topPaddle1
    if vector(-200, -200) in paddle1 and aim1.y < 0:
        aim1 = vector(0, 0)
        paddle1 = bottomPaddle1
    if vector(190, 200) in paddle2 and aim2.y > 0:
        aim2 = vector(0, 0)
        paddle2 = topPaddle2
    if vector(190, -200) in paddle2 and aim2.y < 0:
        aim2 = vector(0, 0)
        paddle2 = bottomPaddle2
    for i in range(len(paddle1)):
        paddle1[i].move(aim1)
        paddle2[i].move(aim2)
    for point in paddle1:
        square(point.x, point.y, paddler)
    for point in paddle2:
        square(point.x, point.y, paddler)
def fixBallSpeed():
    global ball, aimBall
    speed = aimBall.__abs__()
    if speed > maxSpeed:
        aimBall.x = aimBall.x / speed * maxSpeed
        aimBall.y = aimBall.y / speed * maxSpeed

def moveBall():
    global ball, aimBall
    baller.clear()
    fixBallSpeed()
    ballHead = ball.copy()
    ballHead.move(aimBall)
    if ball.y < 20-height/2:
        aimBall.y *= -1
    if ball.y > height/2 - 20:
        aimBall.y *= -1
    if ball.x < - width/2:
        aimBall.x *= -1
        state['score1'] += 1
        writer1.undo()
        writer1.write(str(state['score1']))
        ball = vector(0, 0)
    if ball.x > width/2:
        aimBall.x *= -1
        state['score2'] += 1
        writer2.undo()
        writer2.write(str(state['score2']))
        ball = vector(0, 0)
    paddleCollision()
    ball.move(aimBall)
    baller.up()
    baller.goto(ball.x, ball.y)
    baller.dot(10)
def move():
    global score1
    global heighscore1
    global snake1
    global snake2
    global playing
    if playing:
        if state['mode'].__contains__('ai'):
            aiMovemant()
        movePaddles()
        moveBall()
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

setup(width, height, 370, 100)
hideturtle()
tracer(False)
writer1.color('white')
writer1.goto(-100, 0)
writer1.color('black')
writer1.write('Press: 1 - Normal, 2 - AI')

listen()
onkey(startNormal, '1')
onkey(startAI, '2')
onkeypress(lambda: change2(True, True), 'Up')
onkeypress(lambda: change2(False, True), 'Down')
onkeypress(lambda: change1(True, True), 'w')
onkeypress(lambda: change1(False, True), 's')
onkeyrelease(lambda: change2(True, False), 'Up')
onkeyrelease(lambda: change2(False, False), 'Down')
onkeyrelease(lambda: change1(True, False), 'w')
onkeyrelease(lambda: change1(False, False), 's')

done()
