a=input().lower().split()
b=input().lower().split()
c=0
for i in a:
	if i in b:
		c+=1
print(c)