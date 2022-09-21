a=int(input())
rev=0
while a:
    r=a%10
    rev=rev*10+r
    a//=10
print(rev)