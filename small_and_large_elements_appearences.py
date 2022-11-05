a=input()
a=a.split()
b=''
for i in a:
	b+=i
print(min(b),b.count(min(b)),max(b),b.count(max(b)))
	