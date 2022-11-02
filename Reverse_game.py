def rev(a):
    reverse=0
    while a:
        r=a%10
        reverse=reverse*10+r
        a//=10
    return reverse
a=int(input())
b=list(map(int,input().split()))
for i in b:
    print(rev(i),end=' ')