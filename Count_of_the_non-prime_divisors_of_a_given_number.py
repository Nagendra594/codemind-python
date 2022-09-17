def prime(a):
	c=0
	for l in range(1,a+1):
		if a%l==0:
			c+=1
	if c==2:
		return 1
	else:
		return 0
a=int(input())
A=[]
for i in range(1,a+1):
		if a%i==0:
			if prime(i)==0:
				A.append(i)
print(len(A))