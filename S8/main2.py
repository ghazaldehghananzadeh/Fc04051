import turtle
import time
import math
import random

def color():
   r = random.random()
   g = random.random()
   b = random.random()
   return (r,g,b)




def circle():
    ball = turtle.Turtle()
    for i in range(ball):
          

        ball.shape("circle")

    c = color()
    ball.color(c)

    ball.penup()
  
    return ball
   

def box(x0,y0, x1,y1):
    turtle.penup()
    turtle.setpos(x0,y0)
    turtle.pendown()
    turtle.setheading(0)
    for i in range(4):
        turtle.forward(x1-x0)
        turtle.right(90)

def velocity():
    v = random.randint(100 , 250)
    alpha = random.randint(0,361)
    vx , vy = v * math.cos(math.radians(alpha)) , v * math.sin(math.radians(alpha))
    return vx , vy
def move(b):
    x,y = b.pos()
    x = x + vx * dt
    y = y + vy * dt
    b.setpos(x,y)

def make_balls(n):
    list_balls = []
    for i in range(n):
        list_balls.append(make_balls())
        vx , vy = velocity()
        list_vx.append(vx)
        list_vy.append(vy)

    while True :
        for i in range(len(list_balls)):
            move(list_balls[i], list_vx[i], list_vy[i])
            x , y = list_balls[i].pos()
            if x > 290 or x < -290:
                list



turtle.tracer(0)
box(-300,300,300,-300)
b = circle()
alpha = 30
vb = 200
dt = 0.1

divar = 300 - 10

while True:
    move(b)
    x,y = b.pos()
    if x > divar or x<-divar:
        vx = -vx

    if y > divar or y<-divar:
        vy = -vy

    turtle.update()
    time.sleep(dt)


    