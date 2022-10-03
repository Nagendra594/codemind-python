n=int(input())#175
a=n
A=[]
s=0
while n:
    r=n%10
    A.append(r)
    n//=10
A.reverse()
for i in A:
    s+=i**(A.index(i)+1)
if s==a:
    print('True')
else:
    print('False')
