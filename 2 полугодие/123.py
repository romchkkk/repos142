from turtle import *
left(90)
for i in range(7):
    forward(200)
    left(240)
pu()
for x in range(1,9):
    for y in range(1,10):
        goto(x*20,y*20)
        dot(3)
done()
