def BMM(a,b):
    bmm = 1
    for i in range(1,a+1):
        if (a%i==0 and b%i==0):
            bmm = i

    return bmm

t = BMM(8,12)
print(t)



def BMM2(a,b):
    
    for i in range(a , 0 , -1):
        if (a%i==0 and b%i==0):
            return i
          
p = BMM2(8,12)
print(p)


def KMM(a,b):
    bmm= BMM(a,b)
    return (a*b)//bmm


def KMM2(a , b):
    for i in range(b,(a*b)+1):
        if (i%a==0 and i%b==0):
            return i 
        
print(KMM(8,12))
print(KMM2(8,12))


def KMM3(a,b):
    i = 1
    kmm = b
    while(kmm%a!=0 or kmm%b!=0):
        kmm = i*b
        i += 1

    return kmm
print(KMM3(8,12))

