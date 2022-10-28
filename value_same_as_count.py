l=int(input())
ar=list(map(int,input().split()))
A=set()
for i in ar:
	if i==ar.count(i):
		A.add(i)
print(len(A))