a=input()
a=a.split()
S=0
s=0
for i in a:
	
	S+=ord(max(i))
	s+=ord(min(i))
print(abs(S-s))