a=int(input())
b=list(map(int,input().split()))
for i in range(0,a-2,2):
    if b[i+1]<b[i] and b[i+2]<b[i+1]:
        print('no')
        break
else:
    print('yes')
