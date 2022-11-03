l=input()
c=0
for i in l:
	if 33<=ord(i)<=47 or 58<=ord(i)<=64 or 91<=ord(i)<=96 or 123<=ord(i)<=126:
		c+=1
print(c)