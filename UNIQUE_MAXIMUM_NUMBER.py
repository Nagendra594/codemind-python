a=int(input())
arr=list(map(int,input().split()))
s=set(arr)
A=[]
for i in s:
    if arr.count(i)==1:
        A.append(i)
if len(A)==0:
    print('-1')
else:
    print(max(A))