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
for _ in range(int(input())):
    a=int(input())
    P=0
    b=0
    N=0
    c=0
    while True:
        if a<=b:
            break
        if prime(b):
            P=b
        b+=1
    while True:
        if a<c and prime(c):
            N=c
            break
        c+=1
    if prime(a):
        print(a)
    elif abs(P-a)==(N-a):
        print(P)
    elif abs(P-a)>(N-a):
        print(N)
    else:
        print(P)