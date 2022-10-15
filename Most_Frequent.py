a=int(input())
arr=list(map(int,input().split()))
S=set(arr)
C=[]
for i in S:
	C.append(arr.count(i))
s=set()
for i in arr:
	if arr.count(i)==max(C):
		s.add(i)
print(min(s))