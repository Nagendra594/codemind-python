L=[]
for i in range(int(input())):
	l=int(input())
	L.append(l)
w=int(input())
A=0
for i in L:
	if i<=w:
		A+=1
	else:
		A+=2
print(A)