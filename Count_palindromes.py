def pal(a):
    ori=a
    rev=0
    while a:
        r=a%10
        rev=rev*10+r
        a//=10
    if ori==rev:
        return True
a=int(input())
ar=list(map(int,input().split()))
c=0
for i in ar:
    if pal(i):
        c+=1
print(c)