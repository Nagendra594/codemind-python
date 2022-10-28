l=int(input())
ar=list(map(int,input().split()))
t=int(input())
A=set()
for i in ar:
	if t==ar.count(i):
		A.add(i)
if len(A)>0:
		print(*A)
else:
		print('-1')
		