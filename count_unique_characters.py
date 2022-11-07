a=input().lower()
v=[]
for i in a:
	if i!=' ' and a.count(i)==1 and i not in v:
		v.append(i)
print(len(v))