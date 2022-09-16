def gcd(a,b):
	c=0
	for i in range(1,max(a,b)+1):
		if a%i==0 and b%i==0:
			c=i
	return c
def hcf(arr):
	if len(arr)==1:
		return 0
	G=gcd(arr[0],arr[1])
	if len(arr)==2:
		return G
	if len(arr)>2:
		for k in range(1,len(arr)-1):
			G=gcd(G,arr[k+1])
			return G
	return G
a=int(input())
b=list(map(int,input().split()))
print(hcf(b))