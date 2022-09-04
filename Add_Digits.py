def sd(a):
    A=[]
    while a>0:
        A.append(a%10)
        a=(a-a%10)//10
        
    return A
a=int(input())
b=sum(sd(a))
c=sum(sd(b))
d=sum(sd(c))
print(d)