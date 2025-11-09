import turtle

def draw_line(x1,y1,x2,y2):
    turtle.penup()
    turtle.setpos(x1,y1)
    turtle.pendown()
    turtle.setpos(x2,y2)
    
    
turtle.pensize(2)
turtle.speed(0)
turtle.tracer(0)
for x in range(0, 300,20):
    y = 300 - x
    draw_line(x,0,0,y)
   
def draw_line1(x1,y1,x2,y2):
    turtle.penup()
    turtle.setpos(y1,x1)
    turtle.pendown()
    turtle.setpos(y2,x2)
    turtle.pensize(2)
turtle.speed(0)
turtle.tracer(0)
for x in range(0, 300,20):
    x = 300 - y
    draw_line1(x,0,0,y)
   
   
    
turtle.mainloop()


 