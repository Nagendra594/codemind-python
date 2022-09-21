import math
def prime(s):
    g=int(math.sqrt(s))
    if s<=1:
        return False
    if s>1:
        for i in range(2,g+1):
            if s%i==0:
                return False
    return True
a=int(input())
b=int(input())
for i in range(a+1,b):
    if prime(i):
        print(i)