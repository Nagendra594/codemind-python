l=int(input())
arr=list(map(int,input().split()))
A=[]
for i in arr:
    if i in A:
        pass
    else:
        A.append(i)
print(*A)