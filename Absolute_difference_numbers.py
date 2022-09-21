def rev(a):
    c=0
    while a:
        r=a%10
        c=c*10+r
        a//=10
    return c
a,b=map(int,input().split())
d=a%(10**b)
c=rev(a)%(10**b)
print(max(rev(c),d)-min(rev(c),d))
