def feb(s):
    a=0
    b=1
    A=[a,b]
    if s==1:
        A.remove(b)
    for I in range(2,s-1):
        c=a+b
        a=b
        b=c
        A.append(c)
    return A
a=int(input())
B=[]
b=feb(a)
for j in b:
    B.append(abs(a-j))
for I in b:
    if a-min(B)==I or a+min(B)==I:
        print(I,end=' ')
        
