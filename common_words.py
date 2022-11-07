a=input().lower().split()
b=input().lower().split()
v=[]
for i in b:
	if i in a:
		print(i,end=' ')