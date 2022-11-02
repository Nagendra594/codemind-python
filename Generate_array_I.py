a=int(input())
ar=list(map(int,input().split()))
A=[]
for i in range(0,a-1,2):
	for j in range(ar[i+1]):
		A.append(ar[i])
print(*A)