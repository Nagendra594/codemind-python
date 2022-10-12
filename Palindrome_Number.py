def pal(a):
	org=a
	rev=0
	while a:
		r=a%10
		rev=rev*10+r
		a//=10
	if org == rev:
		return True
	else:
		return False
for i in range(int(input())):
	a=int(input())
	print(pal(a))