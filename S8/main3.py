# n = 1
# s = "fvlfd"
# nums = []

import random
def make_nums(l):
    nums = []
    for i in range(l):
        nums.append(random.random())
                  
    return nums
t = make_nums(10)
print(t)
