a=int(input())
b=list(map(int,input().split()))
if sum(b)//a in b:
	print('True')
else:
	print('False')