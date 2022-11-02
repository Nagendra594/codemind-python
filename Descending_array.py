a=int(input())
b=list(map(int,input().split()))
for i in range(1,a):
    if b[i]>b[i-1]:
        print('no')
        break
else:
    print('yes')
