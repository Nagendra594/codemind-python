def feb(i):
    A=[0,1]
    a=0
    b=1
    for i in range(2,i):
        c=a+b
        a=b
        b=c
        A.append(c)
    return A
a=int(input())
if a==1:
    print('0')
elif a==2:
    print('0 1')
else:
    print(*feb(a))
