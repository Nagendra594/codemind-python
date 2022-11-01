a=int(input())
ar=list(map(int,input().split()))
s=0

for i in ar:
	if i%2!=0:
		break
	else:
		s+=i
print(s)