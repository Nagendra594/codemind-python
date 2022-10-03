def prime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        return True
a=int(input())
B=[]
A=[]
for i in range(a//2+1):
    if prime(i):
        A.append(i)
for i in range(len(A)):
    for j in range(1,len(A)):
        if A[i]*A[j]==a:
            B.append([A[i],A[j]])
if len(B)==0:
    print('-1')
else:
    print(*B[0])