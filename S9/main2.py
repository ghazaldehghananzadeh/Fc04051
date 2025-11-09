import turtle
import time

count = 9


turtle.tracer(0)
tlx= -300
tly = 300
tlx1 = 300
tly1 = -300
def hit(b , fence):
    x,y = b.pos()
    fx,fy = fence.pos()
    d = ((x - fx)**2 + (y-fy)**2)**0.5
    return d < 10
    

list_top = []


for i in range(count):
    t = turtle.Turtle()
    t .penup()
    t.setpos(tlx , tly)
    t.pendown
    tlx = tlx + 70
    t.shape("square")
    t.shapesize(stretch_len=3 , stretch_wid=1)
    list_top.append(t)

count1 = 9
list_top1 = []
for i in range(count1):
    p = turtle.Turtle()
    p.penup()
    p.setpos(tlx1 , tly1)
    p.pendown
    tly1 = tly1 + 70
    p.shape("square")
    p.shapesize(stretch_len=1 , stretch_wid=3)
    list_top1.append(p)


count2 = 9
list_top2 = []
for i in range(count2):
    w = turtle.Turtle()
    w.penup()
    w.setpos(-tlx , -tly)
    w.pendown
    tly = tly - 70
    w.shape("square")
    w.shapesize(stretch_len=1 , stretch_wid=3)
    list_top2.append(w)


count3= 9
list_top3 = []
for i in range(count2):
    w = turtle.Turtle()
    w.penup()
    w.setpos(-tlx1 , tly)
    w.pendown
    tlx1 = tlx1 - 70
    w.shape("square")
    w.shapesize(stretch_len=3, stretch_wid=1)
    list_top3.append(w)




b = turtle.Turtle()
while True:
    x , y = b.pos()
    x += 0.1 * 30
    y += 0.1 * 60
    b.setpos(x , y)
    turtle.update()
    time.sleep(0.1)










turtle.update()
turtle.mainloop()
