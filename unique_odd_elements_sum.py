a=int(input())
ar=set(map(int,input().split()))
S=0
for i in ar:
	if i%2!=0:
		S+=i
print(S)
		