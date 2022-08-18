a,b=map(int,input().split(':'))
c=abs((a*30)-(5.5*b))
if c>180:
    print(360-c)
else:
    print(c)