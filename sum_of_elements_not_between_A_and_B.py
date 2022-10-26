a=int(input())
arr=list(map(int,input().split()))
p,q=map(int,input().split())
s=0
for i in range(a):
	if arr[i]<p or arr[i]>q:
		s+=arr[i]
print(s)