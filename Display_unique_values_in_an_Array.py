l=int(input())
arr=list(map(int,input().split()))
s=set(arr)
c=0
for i in s:
    if arr.count(i)==1:
        c+=1
        print(i,end=' ')
if c==0:
    print('-1')