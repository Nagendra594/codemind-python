def vc(a):
	v='aeiou'
	V='AEIOU'
	if a[0] in v and a[-1] not in v:
			return True
	elif a[0] in V and a[-1] not in V:
		return True
a=input().strip()
b=a.split()
c=0
for i in b:
	if vc(i):
		c+=1
print(c)

		