def mi(a):
	A=[]
	for i in a:
		A.append(ord(i))
	m=min(A)
	M=m+32
	if M in A:
		A.remove(m)
		if M==min(A):
			return chr(M)
		else:
			return chr(min(A))
	else:
		return chr(min(A))
a=input()
b=a.split()
print(mi(b[-1]))