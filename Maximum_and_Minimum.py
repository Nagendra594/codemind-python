l=int(input())
ar=list(map(int,input().split()))
A=[]
for i in ar:
	if i==ar.count(i):
		A.append(i)
if len(A)>0:
	print(min(A),max(A))
else:
	print('-1')