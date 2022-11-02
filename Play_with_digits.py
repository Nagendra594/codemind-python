def sd(a):
    s=0
    while a:
        r=a%10
        s+=r
        a//=10
    return s
a=int(input())
b=list(map(int,input().split()))
S=0
for i in b:
    S+=(sd(i))
print(S)