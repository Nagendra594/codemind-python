from math import sqrt as s
def persq(a):
	g=int(s(a))
	if g*g==a:
		return True
L=int(input())
Arr=list(map(int,input().split()))
S=0
for i in Arr:
	if persq(i):
		S+=i
print(S)
