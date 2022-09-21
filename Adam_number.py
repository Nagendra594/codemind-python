def AN(a):#12
    b=a**2#144
    f=b#144
    rev=0#21
    while a:
        r=a%10
        rev=rev*10+r
        a//=10
    c=rev**2#441
    d=0#144
    while c:
        rem=c%10
        d=d*10+rem
        c//=10
    if f==d:
        return True
    else:
        return False
a=int(input())
print(AN(a))
