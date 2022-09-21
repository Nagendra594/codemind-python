def dig(a):
    A=[]
    while a:
        A.append(a%10)
        a=(a-a%10)//10
    return A
def SDN(a):
    A=dig(a)
    for i in A:
        if i==0 or a%i!=0:
            A.remove(i)
    if len(dig(a))==len(A):
        return True
a=int(input())
b=int(input())
for i in range(a,b+1):
    if SDN(i):
        print(i,end=' ')