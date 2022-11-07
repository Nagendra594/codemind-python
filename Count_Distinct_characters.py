a=input().lower()
b=set()
for i in a:
	if i!=' ':
		b.add(i)
print(len(b))