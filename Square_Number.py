import math
a=int(input())
b=int(math.sqrt(a))
c=0
for i in range(b+1):
    for j in range(b+1):
        if i**2+j**2==a:
            c+=1
if c>0:
    print('True')
else:
    print('False')