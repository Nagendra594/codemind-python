a=int(input())
arr=list(map(int,input().split()))
if a%2:
	arr.append(0)
	for i in range(0,len(arr),2):
		print(arr[i],arr[i+1],end=' ')
else:
		for i in range(0,len(arr),2):
			print(arr[i],arr[i+1],end=' ')
		
	