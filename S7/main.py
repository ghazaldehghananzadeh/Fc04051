import turtle
import time

x0r = -300
y0r = 0
x0p = 300
y0p = 0
t = 0
dt = 0.01
vxr = 250
vyr = 100
Rx = x0r
Ry = y0r
Rxp = x0p
Ryp = y0p
Bx = 100
Vxp = -600
Vyp = 200
g = -9.8



def make_rocket():
    
    r = turtle.Turtle()
    r.penup()
    r.shape("triangle")
    r.shapesize(1)
    r.color("green")
    return r


def make_padafand():
    
    r = turtle.Turtle()
    r.penup()
    r.shape("circle")
    r.shapesize(1)
    r.color("red")

    return r

def explode(t):
    turtle.tracer(1)
    for i in range(5):
        t.color("orange")
        # time.sleep(0.2)
        t.shapesize(i+1)
        time.sleep(0.2)
        t.color("red")
        # t.shapesize(i+1)
        time.sleep(0.2)
        turtle.update()
def draw_barrier(Bx):

    turtle.penup()
    turtle.setpos(Bx , -300)  
    turtle.pendown()
    turtle.setpos(Bx , 300)
turtle.tracer(0)     
r = make_rocket()
p = make_padafand()
draw_barrier(Bx)


while t < 10:
    r.setpos(Rx, Ry)
    p.setpos(Rxp , Ryp)
    t = t + dt
    Rx = Rx + dt * vxr
    Rxp = Rxp + dt * Vxp
    Vyp =0.935 * Vyp + dt * g
    vyr = 0.95 *vyr + dt * g
    Ry = Ry +  vyr * dt
    Ryp = Ryp + Vyp * dt
    time.sleep(dt)
    turtle.update()
    if Rxp <= Rx:
        explode(p)
        explode(r)
        break


turtle.mainloop()




