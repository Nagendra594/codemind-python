def gcd(a,b):
    for i in range(1,max(a,b)):
        if a%i==0 and b%i==0:
            c=i
    return c
a,b=map(int,input().split())
print(gcd(a,b))