def pal(a):
	b=a[::-1]
	if b==a:
		return True
a=input().lower().split()
c=0
for i in a:
	if pal(i):
		c+=1
print(c)