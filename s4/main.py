

# Head()  


# def Line():
#     print(r"+-------+")

# Line()  


# def Body(w,h):
#     for i in range(h):
#          print(r"+*******+")  
#     print(r"+-------+")

# Body(10,20)  



# def sookht(w,h):
#      for i in range(h):
#           print("+", end="")
#           for i in range(w):
#                print("*", end="")
#           print("+")
#      print("+", end="")
#      for i in range(w):
#           print("-", end="")
# #      print("+")

# sookht(20,7)



def khat_bekesh(w, c):
    print("+", end="")
    for i in range(w):
         print(c, end="")
    print("+ ")

def sookht(w,h,c):
     for i in range(h):
          khat_bekesh(w, c)
     khat_bekesh(w, "-")

# sookht(15,6,"%")       

# def Head():
#     print(r"    ^    ")  
#     print(r"   /|\   ")  
#     print(r"  //|\\  ")  
#     print(r" ///|\\\ ")
#     print(r"+-------+")


def Head(h):
    print(r"    ^    ")  
    for i in range(h):
         print(" "*(h+1-i), end="")
         print("/"*(i+1))
         print(""*(h+1-i), end="")
         print(r"\"*(i+1))


    print(r"+-------+")

Head(10)