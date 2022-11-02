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
N,K=map(int,input().split())
ar=list(map(int,input().split()))
c=0
for i in ar:
    if dc(i)==K:
        c+=1
print(c)