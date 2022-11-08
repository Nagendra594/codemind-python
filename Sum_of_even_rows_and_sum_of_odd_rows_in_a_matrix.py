r,c=map(int,input().split())
e=0
o=0
for i in range(r):
	ar=list(map(int,input().split()))
	if i%2:
		o+=(sum(ar))
	else:
		e+=(sum(ar))
print(e,o)