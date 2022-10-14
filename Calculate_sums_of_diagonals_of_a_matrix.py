r=int(input())
sd=0
pd=0
for i in range(r-1,-1,-1):
    arr=list(map(int,input().split()))
    sd+=arr[i]
    pd+=arr[-i-1]
print('Principal Diagonal:{}'.format(pd))
print('Secondary Diagonal:{}'.format(sd))
