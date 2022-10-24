a=int(input())
arr=list(map(int,input().split()))
A,L=map(int,input().split())
B=[]
for i in range(a):
	if arr[i]<A or arr[i]>L:
		B.append(arr[i])
if len(B)==0:
	print('-1')
else:
	print(*B)