a=int(input())
arr=list(map(int,input().split()))
s=set(arr)
A=[]
for i in s:
    if arr.count(i)==i:
        A.append(i)
if len(A)>0:
    print('%.2f'%(sum(A)/len(A)))
else:
    print('-1')