def rev(x):
	reverse=0
	while x:
		r=x%10
		reverse=(reverse*10)+r
		x=x//10
	return reverse
def pal(x):
	b=rev(x)
	if b==x:
		return True
a=int(input())
if a==rev(a):
	print(a+rev(a))
else:
	while a:
		if pal(a):
			print(a)
			break
		a=a+rev(a)