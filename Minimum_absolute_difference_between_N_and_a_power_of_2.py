import math
a=int(input())
b=int(math.sqrt(a))
A=[]
for i in range(0,b+1):
    A.append(abs((2**i)-a))
print(min(A))
