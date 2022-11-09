r,c=map(int,input().split())
A=[]
for i in range(r):
	ar=list(map(int,input().split()))
	A.extend([ar])
C=[]
for i in range(c):
	c=[]
	for j in range(r):
		c.append(A[j][i])
	C.extend([c])
cc=0
for i in C:
	S=sorted(i)
	S.reverse()
	if sorted(i)==i:
		cc+=1
	elif S==i:
		cc+=1
print(cc)