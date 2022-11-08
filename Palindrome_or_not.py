def pal(a):
	b=a[::-1]
	if b==a:
		return True
	return False
a=input().lower()
print(pal(a))