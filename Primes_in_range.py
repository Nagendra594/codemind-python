import math
def po(a,b):
	c=0
	for i in range(a,b+1):
		if i<1 or i==1:
			continue
		elif prime(i):
			c+=1
	return c
def prime(n):
	g=int(math.sqrt(n))
	for j in range(2,g+1):
		if n%j==0:
			return False

	return True
e=int(input())
f=int(input())
print(po(e,f))
