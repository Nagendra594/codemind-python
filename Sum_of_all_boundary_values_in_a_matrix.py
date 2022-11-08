r,c=map(int,input().split())
A=[]
for i in range(r):
    arr=list(map(int,input().split()))
    if i==0 or i==r-1:
        A.append(sum(arr))
    else:
        A.append(arr[0])
        A.append(arr[-1])
print(sum(A))
