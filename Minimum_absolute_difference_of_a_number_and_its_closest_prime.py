def prime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        return True
    else:
        return False
a=int(input())
A=[]
B=[]
for i in range(1,a+10):
    if prime(i):
        A.append(i)
for j in A:
    B.append(abs(a-j))
print(min(B))

