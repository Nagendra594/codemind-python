a=int(input())
ar=list(map(int,input().split()))
A=[i for i in ar if i%2==0]
B=[i for i in ar if i%2!=0]
C=[]
while True:
	if len(A)==0 or len(B)==0:
		break
	else:
		e=A.pop(0)
		o=B.pop(0)
		C.extend([e,o])
if len(A)>0:
	for i in A:
		C.append(i)
elif len(B)>0:
	for i in B:
		C.append(i)
if a%2!=0:
	C.append(0)
print(*C)