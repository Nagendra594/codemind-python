a=int(input())
arr=list(map(int,input().split()))
B=[]
C=[]
for i in range(a):
	if arr[i]%2==0:
		B.append(arr[i])
	else:
		C.append(arr[i])
print(*(C+B))