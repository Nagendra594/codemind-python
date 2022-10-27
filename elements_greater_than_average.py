a=int(input())
ar=list(map(int,input().split()))
av=sum(ar)//a
c=0
for i in ar:
	if i>=av:
		c+=1
		
print(c)
