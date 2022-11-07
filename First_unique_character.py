a=input().lower()
v=[]
for i in a:
	
	if a.count(i)==1 and i!=' ' and i not in v:
		v.append(i)
print(v[0] if len(v)>0 else '-1')