def sf(a):
	s=0
	for i in range(1,a+1):
		if a%i==0:
			s+=i
	return s
a=list(input())
A=[]
B=[]
for i in a:
	if i==',':
		pass
	else:
		A.append(int(i))
for i in A:
	if sf(i) in A:
		B.append(i)
B.sort()
if len(B)>0:
	print(*B)
else:
	print('-1')