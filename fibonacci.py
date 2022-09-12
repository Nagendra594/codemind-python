def feb(n):
    A=[0,1]
    a=0
    b=1
    for i in range(2,n):
        c=a+b
        A.append(c)
        a=b
        b=c
    return A
a=int(input())
print(*(feb(a)))