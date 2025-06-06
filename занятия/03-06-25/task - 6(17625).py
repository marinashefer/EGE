from turtle import *

tracer(0)
lt(90)
m = 10

for i in range(10):
    fd(22*m)
    rt(90)
    fd(16*m)
    rt(90)

up()
fd(1*m)
rt(90)
fd(1*m)
lt(90)
down()

for i in range(10):
    fd(72*m)
    rt(90)
    fd(79*m)
    rt(90)

up()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x*m, y*m)
        dot(3, 'white')

update()
done()