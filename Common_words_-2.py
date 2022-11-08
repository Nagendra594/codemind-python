a=input().lower().split()
b=input().lower().split()
c=0
for i in a:
	if i in b and b.count(i)==1 and a.count(i)==1:
		c+=1
print(c)