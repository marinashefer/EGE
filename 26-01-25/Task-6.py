from turtle import *

tracer(0)
lt = 90
m = 10

for i in range(0):
    fd(m*15)
    rt(90)
    fd(m*25)
    rt(90)

up()
bk(10*m)
rt(90)
down()
for i in range(8):
    fd(15*m)
    left(90)
    fd(25*m)
    left(90)

up()
fd(6*m)
left(90)
down()

for i in range(7):
    fd(15*m)
    rt(90)
    fd(25*15)
    rt(90)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(3, 'darkred')


update()