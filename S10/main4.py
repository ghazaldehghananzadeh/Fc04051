
def AVG(scores):
    size = len(scores)
    sum = 0


    for i in range(size):
        sum += scores[i]

    return sum/size





# def AVG2(scores , weight):

#     sum_s = 0
#     sum_w = 0
#     for i in range(len(scores)):
#         sam_s += scores[i] * weight[i]
#         sam_w += weight[i]

#     return sam_s/sam_w

  


    
# a = [18,19,16,19,18] 
# w = [3,3,3,2,2]

# print(AVG(a))
# print(AVG2(a,w))


def Append2(a,indx,val):
    a_list = []
    for i in range(indx):
        a_list.append(a[i])
    
    a_list.append(val)

    for i in range(indx,len(a)):
        a_list.append(a[i])
    
    return a_list
print(Append2([1,2,3,4],2,5))

y=[1,2,1,3,4,1,2,1,4,1,5,1]
def count(lst,val):
    n =0 
    for i in range(len(lst)):
        if lst[i]==val:
            n+=1
        return n 
print(count(y,5))
print(count(y,9))

print()
t = [4,1,7,20,3]

for i in range(len(t)):
    print(t[i])
print()
for i in t:
    print(i)
 
