def prime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        return True
day1=int(input())
day2=int(input())
b=day1+day2+1
while b:
    if prime(b):
        print(b-(day1+day2))
        break
    b+=1