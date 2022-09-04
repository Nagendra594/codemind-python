a=int(input())
A=[]
for i in range(1,a):
    if a%i==0:
        A.append(i)
if sum(A)==a:
    print('True')
else:
    print('False')