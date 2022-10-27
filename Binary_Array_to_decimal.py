a=int(input())
ar=list(map(int,input().split()))
ar.reverse()
dec=0
for i in range(a):
		if ar[i]==1:
			dec+=(2**i)
print(dec)
		