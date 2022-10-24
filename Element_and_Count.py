a=int(input())
arr=list(map(int,input().split()))
B=[]
for i in arr:
    if i in B:
        pass
    else:
        B.append(i)
for i in B:
    print(i,end=' ')
    print(arr.count(i),end=' ')