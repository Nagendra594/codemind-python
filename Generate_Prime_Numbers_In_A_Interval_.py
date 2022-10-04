def prime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        return True
a=int(input())
b=int(input())
for i in range(a+1,b):
    if prime(i):
        print(i)