N=int(input())
L=list(map(int,input().split()))
if sum(L)%2==0:
    print('1')
else:
    print('0')