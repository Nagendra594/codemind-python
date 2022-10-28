l=int(input())
ar=list(map(int,input().split()))
A=[]
for i in ar:
	if i==ar.count(i):
		if i in A:
			pass
		else:
			A.append(i)
if len(A)>0:
	print(*A)
else:
	print('-1')