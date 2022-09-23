def prime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        return True
    else:
        return False
for _ in range(int(input())):
    a=int(input())
    A=[]
    for i in range(a-10,a+10):
        if prime(i):
            A.append(abs(a-i))
    c=min(A)+a
    d=abs(min(A)-a)
    if prime(c) and prime(d):
        print(min(c,d))
    elif prime(c):
        print(c)
    else:
        print(d)