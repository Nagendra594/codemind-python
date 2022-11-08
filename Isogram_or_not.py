a=input().lower()
c=0
for i in a:
	if a.count(i)==1:
		c+=1
print('True' if c==len(a) else 'False')