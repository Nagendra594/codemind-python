a=int(input())
arr=list(map(int,input().split()))
A,B=map(int,input().split())
L=[]
for i in arr:
    if i<A or i>B:
        L.append(i)
if len(L)==0:
    print('-1')
else:
    print(max(L))