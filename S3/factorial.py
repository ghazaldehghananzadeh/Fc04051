def factorial():
    n=6
    result = 1
    for i in range(1,n+1):
        result = result * i
        # result *=i
    

    print(result)

    
factorial()

def factorial(n):
    result = 1
    for i in range(1,n+1):
         result = result * i
    print(result)

factorial(6)

def factorial(n):
    result = 1
    for i in range(1,n+1):
         result = result * i
    # print(result)
    return result

x = factorial(5)
y = factorial(7)

print(x)
print(y)
print(x+y)
print(factorial(5)+factorial(7))
print(x-y)




