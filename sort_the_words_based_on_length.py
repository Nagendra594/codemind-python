a=input()
a=a.split()
A=[]
B=[]
for i in a:
	A.append(len(i))
A.sort()
for i in A:
	for j in a:
		if len(j)==i:
			B.append(j)
			a.remove(j)
			break
def sumw(a):
	s=0
	for i in a:
		s+=ord(i)
	return s
C=[]
for i in B:
	C.append(sumw(i))
C.sort()
D=[]
for i in C:
	for j in B:
		if sumw(j)==i:
			D.append(j)
			B.remove(j)
			break
D=' '.join(D)
print(D)