a=int(input())
arr=list(map(int,input().split()))
if a%2==0:
	for i in range(a//2):
		a=arr[i]
		b=arr[-(i+1)]
		print(a,b,end=' ')
else:
	arr.insert(a//2+1,0)
	for i in range(len(arr)//2):
		a=arr[i]
		b=arr[-(i+1)]
		print(a,b,end=' ')
	