
A,B=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
F=[]
for i in a:
	if i not in b:
		F.append(i)
for i in b:
	if i not in a:
		F.append(i)
print(*F)