def power(a,b):
    # a=3
    # b=4
    result = 1
    for _ in range(1,b+1):
        result = result * a
    print(result)

power(5,4)

def power(a,b=3):
    # a=3
    # b=4
    result = 1
    for _ in range(1,b+1):
        result = result * a
    print(result)

power(5,4)
power(2,5)
power(8)


def power(a,b):
    # a=3
    # b=4
    result = 1
    for _ in range(1,b+1):
        result = result * a
    print(result)
    return result
     
x = power(3,5)
y = power(4,2)

print(x+y)