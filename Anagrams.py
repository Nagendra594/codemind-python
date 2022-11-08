a=input().lower()
b=input().lower()
if len(a)==len(b):
	c=0
	for i in a:
		if i in b:
			c+=1
	if c==len(a):
		print('True')
	else:
		print('False')
else:
	print('False')