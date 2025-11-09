import turtle
import random

def get_random_color():
      r = random.random()
      b = random.random()
      g = random.random()
      return(r,b,g)
def tr(n,z):
    for i in range(z):
            turtle.forward(n)
            turtle.right(((z-2)*180)/z)
c = get_random_color()         
turtle.pencolor(c)
           
tr(100,8)
turtle.mainloop()