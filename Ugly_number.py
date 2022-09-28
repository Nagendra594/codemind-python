import math
def prime(a):
	s=int(math.sqrt(a))
	if a==1:
		return False
	for i in range(2,s+1):
		if a%i==0:
			return False
	return True
def ug(a):
	if a<0:
		return 'Not Ugly Number'
	A=[]
	for i in range(1,a+1):
		if a%i==0:
			A.append(i)		
	for i in A:	
			if i==2 or i==3 or i==5 or i==1:
				continue
			elif prime(i):
				return 'Not Ugly Number'
	return 'Ugly Number'
a=int(input())
print(ug(a))
		