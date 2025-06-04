from turtle import *

tracer(0)
lt(90)
m = 20

rt(30)
for i in range(3):
    rt(150)
    fd(6*m)
    rt(30)
    fd(12*m)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(3, 'darkred')

done()

#https://kompege.ru/variant?kim=25102704