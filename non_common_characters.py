a=input().lower()
b=input().lower()
v=[]
for i in b:
	if i not in a and i not in v and i!=' ':
		v.append(i)
for i in a:
	if i not in b and i not in v and i!=' ':
		v.append(i)
print(''.join(sorted(v)))