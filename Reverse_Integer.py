a=int(input())
b=abs(a)
rev=0
while b:
    r=b%10
    rev=rev*10+r
    b//=10
if a>0:
    print(rev)
if a<0:
    print(-(rev))