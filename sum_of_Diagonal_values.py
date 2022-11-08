r,c=map(int,input().split())
pd=0
sd=0
A=[]
for i in range(r):
    arr=list(map(int,input().split()))
    A.extend([arr])
    pd+=arr[i]
    sd+=arr[-i-1]
if r%2:
    m=A[r//2][r//2]
    print((pd+sd)-m)
else:
    print(pd+sd)
