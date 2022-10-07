len_arr=int(input())
a=list(map(int,input().split()))
A=[]
while len(a)>1:
		b=max(a)
		a.remove(b)
		c=max(a)
		A.append(c)
		A.append(b)
		a.remove(c)
for i in a:
	A.append(i)
print(*A)