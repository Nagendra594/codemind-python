a=int(input())
b=list(map(int,input().split()))
c=0
if a%2==0:
	b.append(0)
	c-=1
for i in range(1,a,2):
			if b[i-1]>b[i] or b[i]<b[i+1]:
				break
			else:
				c+=1
if a%2==0:
	if c==(a//2)-1:
		print(c)
	else:
		print('-1')
else:
	if c==(a//2):
		print(c)
	else:
		print('-1')
