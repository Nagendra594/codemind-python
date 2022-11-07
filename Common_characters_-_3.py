a=input().lower().split()
b=a.pop(a.index(min(a)))

B=[]
for i in b:
	for j in a:
		if i not in j:
			pass
		else:
			B.append(i)
if len(B)>=len(a)+1:
	print(min(B))
else:
	print('-1')