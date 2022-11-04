def vc(a):
	v='aeiouAEIOU'
	if a[0] in v and a[-1] not in v:
			return True
a=input().strip()
b=a.split()
c=0
for i in b:
	if vc(i):
		c+=1
print(c)

		