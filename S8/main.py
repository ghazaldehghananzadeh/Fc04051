import turtle
import time
import math
import random
x = -300
y = 300
x1=0
y1=0
vx=20
vy=20
t = 0 
dt = 0.01

turtle.penup()
turtle.setpos(x,y)
turtle.pendown()

for i in range(4):
    
    turtle.forward(600)
    turtle.right(90)



def circle():
    
    ball = turtle.Turtle()
   
    ball.shape("circle")
    # ball.shapesize(5)
    c = (random.random)
    ball.color(c)
    ball.penup()



    return ball


def move(b):
    x1,y1 = b.pos()
    t = t + dt
    x1 = x1 + dt * vx
    y1 = y1 + dt * vy
    b.setpos(x1,y1)

turtle.tracer(0)
alpha=30
vb=200
vy= vb * math.sin(math.radians(alpha))
vx= vb * math.cos(math.radians(alpha))
b = circle()
divar=290
while True:
    move(b)
    x,y = b.pos()

    if x1<-divar or x1>divar :
        vx = -vx
    
    if y1 <-divar or y1>divar :
        vy = -vy

    turtle.update()
    time.sleep(dt)


   