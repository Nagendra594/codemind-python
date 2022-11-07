a=input().lower().split()
b=a.pop(a.index(min(a)))
C=0
for i in b:
	c=0
	for j in a:
		if i in j:
			c+=1
	if c==len(a):
		C+=1
print(C)
		