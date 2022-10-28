l=int(input())
ar=list(map(int,input().split()))
E=0
I=0
for i in ar:
	if i%2!=0:
		E+=1
for i in range(1,l,2):
	if ar[i]%2!=0:
		I+=1
print(E==I)