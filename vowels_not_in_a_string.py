l=input()
v=['a','e','i','o','u']
for i in l:
	if i in v:
		v.remove(i)
print(*v if len(v)>0 else '0')