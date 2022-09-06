def gcd(n, m):
	r = n % m
	while r > 0:
		n = m
		m = r
		r = n % m
	#endwhile
	return m
#end fun

t = int(input())
for i in range(t):
	N,A,B,K=map(int,input().split())
	M = A*B/gcd(A,B)
	tot = N/A + N/B - 2*(N/M)
	if tot < K:
		print('Lose')
	else:
		print('Win')
    
    
    