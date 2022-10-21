l=int(input())
arr=list(map(int,input().split()))
O=0
E=0
for i in range(l):
    if i%2:
        O+=arr[i]
    else:
        E+=arr[i]
if O-E:
    print('NO')
else:
    print('YES')
