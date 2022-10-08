a=int(input())
b=list(map(int,input().split()))
c=a//2
A=[]
B=[]
A.append(b[c:])
for i in A:
    for j in i:
        B.append(j)
        if j in b:
            b.remove(j)
B.reverse()
for i in b:
    B.append(i)
print(*B)