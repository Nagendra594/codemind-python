l=input()
L=l.split()
c=0
for i in range(len(L)):
	for j in L[i]:
		c+=1
print(c)