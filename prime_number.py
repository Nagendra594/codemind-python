a=int(input())
for i in range(1,a):
    if i==1:
        pass
    elif a%i==0:
        print('not a prime')
        break
else:
    print('prime')