a=int(input())
b=a*a
A=[]
while b:
    A.append(b%10)
    b=(b-b%10)//10
if sum(A)==a:
    print('Neon Number')
else:
    print('Not Neon Number')