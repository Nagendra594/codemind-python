r,c=map(int,input().split())
A=[]
for i in range(r):
	ar=list(map(int,input().split()))
	A.extend([ar])
cc=0
for i in A:
	S=sorted(i)
	S.reverse()
	if sorted(i)==i:
		cc+=1
	elif S==i:
		cc+=1
print(cc)