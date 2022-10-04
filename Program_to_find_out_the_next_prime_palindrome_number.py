def prime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        return True
def pal(a):
    rev=0
    n=a
    while a:
        r=a%10
        rev=rev*10+r
        a//=10
    if rev==n:
        if prime(n):
            return True
        else:
            return False
    else:
        return False
a=int(input())
b=a+1
while b:
    if pal(b):
        print(b)
        break
    b+=1
