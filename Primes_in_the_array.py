from math import sqrt as s
def prime(a):
	g=int(s(a))
	if a<=1:
		return False
	for i in range(2,g+1):
		if a%i==0:
			return False
	return True
A=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
	if prime(i):
		c+=1
print(c)
	