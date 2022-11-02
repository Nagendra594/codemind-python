a=int(input())
b=list(map(int,input().split()))
if a<=2:
    print('no')
else:
    for i in range(2,a):
        if b[i-2]+b[i-1]!=b[i]:
            print('no')
            break
    else:
        print('yes')