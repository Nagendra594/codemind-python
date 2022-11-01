a=int(input())
ar=list(map(int,input().split()))
S=int(input())
s=0

for i in ar:
	if i<=S:
		s+=i
print(s)