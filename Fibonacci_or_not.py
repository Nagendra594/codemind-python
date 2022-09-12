def feb(n):
    A=[0,1]
    a=0
    b=1
    for i in range(2,n+1):
        c=a+b
        A.append(c)
        a=b
        b=c
    return A
a=int(input())
b=feb(a)
if a in b:
    print('True')
else:
    print('False')