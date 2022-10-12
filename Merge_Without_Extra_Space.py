for _ in range(int(input())):
	n,m=map(int,input().split())
	arr_1=list(map(int,input().split()))
	arr_2=list(map(int,input().split()))
	A=[]
	for i in arr_1:
		A.append(i)
	for j in arr_2:
		A.append(j)
	A.sort()
	print(*A)
	
			