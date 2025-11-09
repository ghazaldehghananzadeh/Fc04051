import turtle
import time
count = 10

turtle.tracer(0)
tlx= -300
tly = 300

def hit(b , fence):
    x,y = b.pos()
    fx,fy = fence.pos()
    d = ((x - fx)**2 + (y-fy)**2)**0.5
    return d < 10
    
currentx = tlx
currenty = tly
list_top = []

for i in range(count):
    t = turtle.Turtle()
    t .penup
    t.setpos(currentx , tly)
    currentx = currentx + 70
    t.shape("square")
    t.shapesize(stretch_len=3 , stretch_wid=1)
    list_top.append(t)


b = turtle.Turtle()
while True:
    x , y = b.pos()
    x += 0.1 * 30
    y += 0.1 * 60
    b.setpos(x , y)
    turtle.update()
    time.sleep(0.1)



# turtle.update()
# turtle.mainloop()
