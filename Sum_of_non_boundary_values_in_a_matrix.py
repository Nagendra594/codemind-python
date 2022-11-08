r,c=map(int,input().split())
A=[]
for i in range(r):
    arr=list(map(int,input().split()))
    if i==0 or i==r-1:
        pass
    else:
        arr1=[]
        for j in range(1,c-1):
            arr1.append(arr[j])
        A.append(sum(arr1))
print(sum(A))

