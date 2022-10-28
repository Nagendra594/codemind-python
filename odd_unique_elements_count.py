l=int(input())
ar=list(map(int,input().split()))
s=list(set(ar))
c=0
for i in s:
		if i%2!=0:
			c+=1
print(c)
		