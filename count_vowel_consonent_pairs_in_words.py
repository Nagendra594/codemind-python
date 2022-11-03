def vc(a):
	v=['a','e','i','o','u']
	aa=0
	b=-1
	c=0
	while True:
		if a[aa] in v and a[b] not in v or a[aa] not in v and a[b] in v:
			c+=1
		if len(a)%2:
			if abs(b*2)+1==len(a):
				break
		else:
			if abs(b*2)==len(a):
				break
		aa+=1
		b-=1
	return c
a=input()
b=a.split()
s=0
for i in b:
	s+=(vc(i))
print(s)