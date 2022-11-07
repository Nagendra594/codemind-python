a=input().lower()
b=[]
for i in a:
	if i!=' ' and i not in b:
		b.append(i)
print(''.join(sorted(b)))