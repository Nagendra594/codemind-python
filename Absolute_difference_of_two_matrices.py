rc=int(input())
A=[]
B=[]
for j in range(rc):
    mat1=list(map(int,input().split()))
    A.extend([mat1])
    
for i in range(rc):
    mat2=list(map(int,input().split()))
    B.extend([mat2])
for i in range(rc):
    c=[]
    for j in range(rc):
        c.append(abs(A[i][j]-B[i][j]))
    print(*c)