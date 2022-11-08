r,c=map(int,input().split())
s=0
for i in range(r):
    arr=list(map(int,input().split()))
    s+=sum(arr)
print(s)
    