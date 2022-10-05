a=int(input())
b=list(map(int,input().split()))
for i in range(-1,-(len(b)+1),-1):
	if b[i]%2==0:
		print(b[i])
		break