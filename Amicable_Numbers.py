a=int(input())
b=int(input())
c=0
d=0
for i in range(1,a):
    if a%i==0:
        c+=i
for j in range(1,b):
    if b%j==0:
        d+=j
if c==b and d==a:
       print('Amicable')
else:
       print('Not Amicable')
       