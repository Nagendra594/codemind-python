a=input()
a=a.split()
for i in a:
	print(abs(ord(max(i))-ord(min(i))),end=' ')