l=input()
v=['a','e','i','o','u']
V=['A','E','I','O','U']
c=0
for i in l:
	if i in v or i in V:
		c+=1
print(c)