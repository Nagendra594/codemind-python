l=input()
v=['a','e','i','o','u']
V=['A','E','I','O','U']
if l.isupper():
	for i in l:
		if i in V:
			V.remove(i)
	if len(V)==0:
		print('True')
	else:
		print('False')
elif l.islower:
		for i in l:
			if i in v:
				v.remove(i)
		if len(v)==0:
			print('True')
		else:
			print('False')
else:
		print('False')
		