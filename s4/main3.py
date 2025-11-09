# import turtle
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(50)
# turtle.mainloop()


# import turtle
# turtle.pencolor("light blue")
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.mainloop()


import turtle
import random
def get_random_color():
   r = random.random()
   g = random.random()
   b = random.random()
   return (r,g,b)




def draw(n, l, ld, ad):
    for j in range(200):
         for i in range(n):
            turtle.forward(l) 
            a = 360/n
            turtle.right(a)
         a = a * ad
         l = l * ld
         turtle.right(5)
         c = get_random_color()
         turtle.pencolor(c)
turtle.speed(0)
turtle.tracer(0)
turtle.pensize(2)
turtle.penup()
turtle.setpos(0, 200)
turtle.pendown()
draw(10, 100, 0.98, 1.03)
turtle.update()
turtle.mainloop()


