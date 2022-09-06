a=int(input())
if a==1:
    print('not a prime')
if a>1:
    for i in range(2,a):
        if a%i==0:
            print('not a prime')
            break
    else:
        print('prime')