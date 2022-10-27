a=int(input())
ar=list(map(int,input().split()))
c=0
for i in range(a):
		if ar[i]==0 or ar[i]==1:
			c+=1
print('True' if c==a else 'False')