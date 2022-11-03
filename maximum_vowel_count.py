l=input()
L=l.split()
v=['a','e','i','o','u','A','E','I','O','U']
C=[]
for i in range(len(L)):
	c=0
	for j  in L[i]:
		if j in v:
			c+=1
	C.append(c)
print(max(C))