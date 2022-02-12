import turtle

t=turtle.Turtle()
s= turtle.Screen()
s.bgcolor("white")
t.pencolor("green")
t.speed(0)
for i in range(18):
    if i%18==0:
        t.pencolor("green")
    elif i%18==6:
        t.pencolor("red")
    elif i%18==12:
        t.pencolor("blue")
    t.circle(190-i,90)
    t.lt(98)
    t.circle(190-i,90)
    t.lt(18)
t._rotate(265)
t.color("white")
t._go(32)
for i in range(18):
    if i%18==0:
        t.pencolor("green")
    elif i%18==6:
        t.pencolor("red")
    elif i%18==12:
        t.pencolor("blue")
    t.circle(20-i/40,90)
    t.lt(98)
    t.circle(20-i/40,90)
    t.lt(18)
while True:
    pass