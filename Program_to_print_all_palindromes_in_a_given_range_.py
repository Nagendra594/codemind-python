def rev(a):
    b=0
    while a:
        r=a%10
        b=(b*10)+r
        a//=10
    return b
a=int(input())
b=int(input())
for i in range(a,b):
    if i==rev(i):
        print(i,end=" ")