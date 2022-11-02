def dc(a):
    c=0
    while a:
        r=a%10
        c+=1
        a//=10
    return c
a=int(input())
b=list(map(int,input().split()))
C=[]
for i in b:
    C.append(dc(i))
print(C.count(min(C)))