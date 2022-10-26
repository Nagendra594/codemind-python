a=int(input())
arr=list(map(int,input().split()))
arr.extend([arr[0],arr[1]])
c=0
for i in range(len(arr)-2):
	if arr[i]%2==0 and arr[i+2]%2!=0 or arr[i]%2!=0 and arr[i+2]%2==0:
		c+=1
print(c)