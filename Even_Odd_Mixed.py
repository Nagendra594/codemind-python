a=int(input())
A=[]
while a:
    A.append(a%10)
    a=(a-a%10)//10
odd=0
even=0
for i in A:
    if i%2==0:
        even+=1
    else:
        odd+=1
if odd>0 and even>0:
    print('Mixed')
elif odd==0 and even>0:
    print('Even')
else:
    print('Odd')