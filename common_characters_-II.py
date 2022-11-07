a=input().lower()
b=input().lower()
v=[]
for i in b:
	if i in a and i not in v and i!=' ':
		v.append(i)
print(len(v))