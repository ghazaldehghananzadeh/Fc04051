# print(r"\nail\vfkdf" , end="")

# print("-\r" )

for i in range(1000000):
    print("-", end="\r")
    print("\\", end="\r")
    print("|", end="\r")
    print("/", end="\r")


def f(x,y):
    r = x + y
    return r

w = f(4,5)

print(w)