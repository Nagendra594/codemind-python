a=int(input())
ar=list(map(int,input().split()))
E=[i for i in ar if i%2==0]
O=[i for i in ar if i%2!=0]
C=[]
while True:
	if len(E)==0 or len(O)==0:
		break
	o=O.pop(0)
	e=E.pop(0)
	C.extend([o,e])
if a%2==0:
	if len(E)>0:
		for i in E:
			C.append(i)
	elif len(O)>0:
		for i in O:
			C.append(i)
else:
		if len(E)>0:
			for i in E:
				C.append(i)
			C.append(0)
		elif len(O)>0:
			for i in O:
				C.append(i)
			C.append(0)
print(*C)