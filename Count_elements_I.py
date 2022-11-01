
A,B=map(int,input().split())
a=list(set(map(int,input().split())))
b=list(set(map(int,input().split())))
c=0
for i in a:
	if i in b:
		c+=1
print(c)