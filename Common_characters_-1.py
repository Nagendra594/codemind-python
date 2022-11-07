a=input().lower().split()
b=a.pop(a.index(min(a)))
ans=''
for i in b:
	c=0
	for j in a:
		if i in j:
			c+=1
	if c==len(a):
		ans+=i
if len(ans)>0:
	print(ans)
else:
	print('-1')