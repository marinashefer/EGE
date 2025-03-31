from turtle import *

tracer(0)
m = 10
lt(90)
for i in range(5):
    fd(30 * m)
    rt(90)
    fd(40 * m)
    rt(90)

up()
fd(20 * m)
rt(90)
fd(5*m)
rt(90)
down()

for i in range(7):
    fd(10*m)
    rt(90)

up()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x*m, y*m)
        dot(3, 'darkred')

update()