a=int(input())
arr=list(map(int,input().split()))
A=[]
for i in range(a):
    c=0
    for j in range(a):
        if arr[i]>arr[j]:
            c+=1
    A.append(c)
print(*A)
            