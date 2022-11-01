
A,B=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
S=[]
for i in a:
	if i in b:
		if i in S:
			pass
		else:
			S.append(i)
print(*S)