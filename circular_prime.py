from math import sqrt as s
def prime(a):
    g=int(s(a))
    if a<=1:
        return False
    for i in range(2,g+1):
        if a%i==0:
            return False
            break
    return True
def rev(a):
    rev=0
    while a:
        r=a%10
        rev=rev*10+r
        a//=10
    return rev
a=int(input())
if prime(a) and prime(rev(a)):
    print('circular prime')
elif prime(a):
    print('prime but not a circular prime')
else:
    print('not prime')