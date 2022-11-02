def dc(a):
    A=abs(a)
    if a==0:
        return 1
    c=0
    while A:
        A%10
        c+=1
        A//=10
    return c
a=int(input())
ar=list(map(int,input().split()))
for i in ar:
    print(dc(i),end=' ')