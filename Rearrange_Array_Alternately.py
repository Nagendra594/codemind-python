for _ in range(int(input())):
	l=int(input())
	arr=list(map(int,input().split()))
	fin=[]
	if l%2==0:
		while True:
			if len(arr)==0:
				break
			M=max(arr)
			m=min(arr)
			fin.append(M)
			arr.remove(M)
			fin.append(m)
			arr.remove(m)
		print(*fin)
	else:
		while True:
			if len(arr)<=1:
				break
			M=max(arr)
			m=min(arr)
			fin.append(M)
			arr.remove(M)
			fin.append(m)
			arr.remove(m)
		fin.append(arr[0])
		print(*fin)
		