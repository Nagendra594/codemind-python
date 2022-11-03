def vc(a):
	v=['A','E','I','O','U','a','e','i','o','u']
	e=0
	E=-1
	c=0
	while True:
		if a[e] in v and a[E] not in v or a[e] not in v and a[E] in v:
			if a[e]==' ' or a[E]==' ':
				pass
			else:
				c+=1
		if len(a)%2:
			if abs(E*2)+1==len(a):
				break
		else:
			if abs(E*2)==len(a):
				break
		e+=1
		E-=1
	return c
a=input()
print(vc(a))