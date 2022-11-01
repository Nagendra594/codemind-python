a=int(input())
ar=list(map(int,input().split()))
S,E=map(int,input().split())
m=S if E>S else E
M=E if m==S else S
A=[]

for i in ar:
	if m<=i<=M:
		A.append(i)
if len(A)==0:
	print('-1')
else:
	print(*A)