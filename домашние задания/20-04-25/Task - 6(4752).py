from turtle import *

tracer(0)
m = 10
lt(90)

for i in range(15):
    fd(4*m)
    rt(60)

up()
goto(0, 0)
dot(5, 'green')
down()

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(3, 'darkred')

update()
done()
