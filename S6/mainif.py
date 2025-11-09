a = 9
if a%2 == 1:
    print("odd")

else: 
    print("even")


a = 5
if a<10:
    print("1")

# else:
    # print("1.5")
if a<20:
    print("2")
if a<50:
  print("3")

if a<120:
  print("4")

else:
    print("5")




a = 5

if a<10:
    print("1")


elif a<20:
    print("2")

elif a<50:
  print("3")

elif a<120:
  print("4")

else:
    print("5")




def add4(a,b):
   result = 0
   if a%2 == 1:
       for i in range(a,b+1 , 2):
          result += i
  

   else:
      for j in range(a+1 , b+1 , 2):
         result += j
         
   return result 
g = add4(7,14) 
print(g)



def add5(a,b):
   result = 0 
   for i in range(a , b+1):
      if i%2==1:
         result += i

   return result     



def isprime1(n): 
    for i in range(2 , n) :
        if n%i == 0:
           print("ok")
        else:
            print("av")
           
         
      
# isprime1(8)

# def isprime(n): 
#     for i in range(2 , n) :
#         if n%i != 0 :
           
            
 
    
        
        
        
       
           
    
        
         
      
# isprime(8)



