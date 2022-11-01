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
m=a.index(min(a))
M=a.index(max(a))
mm=m if M>m else M
MM=M if mm==m else m
c=0
for i in range(mm,MM+1):
	if prime(a[i]):
		c+=1
print(c)
	