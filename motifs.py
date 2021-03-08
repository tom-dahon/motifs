import turtle as t
import math
from random import randint

#t.bgcolor("black")
#t.ht()
t.speed(50)
t.setup(800, 600)
t.up()
t.setposition(250, 30)
phi = (1+math.sqrt(5))/2
i = 360/2*phi*math.pi
t.down()

l = ["red", "yellow", "magenta", "blue", "lime", "white", "cyan"]
def triangles(l):
    for s in l:
        for x in range(200):
            t.color(s)
            t.right(i)
            t.forward(600) 
        
def spirale1():
    t.ht()
    t.up()
    t.setposition((0,0))
    t.down()
    for i in range(700):
        t.forward(i)
        t.left(91)
        
def spirale2():
    t.ht()
    t.up()
    t.setposition((0,0))
    t.down()
    for i in range(90):
        t.circle(i)
        t.right(60)

spirale2()
#spirale1()    
#triangles(l)
t.exitonclick()