def sd(a):
    A=[]
    while a>0:
        A.append(a%10)
        a=(a-a%10)//10
    return A
def final(a):
    for i in sd(a):
        if i==0:
            pass
        elif a%i!=0:
            break
    else:
        return True
a=int(input())
b=int(input())
A=[]
for i in range(a,b+1):
    if final(i)==True:
        A.append(i)
for j in A:
    if j%10==0:
        A.remove(j)
print(*A)
