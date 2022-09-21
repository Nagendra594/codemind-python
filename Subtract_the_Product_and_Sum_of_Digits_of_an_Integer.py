a=int(input())
sq=1
s=0
while a:
    r=a%10
    sq*=r
    s+=r
    a//=10
print(sq-s)
    