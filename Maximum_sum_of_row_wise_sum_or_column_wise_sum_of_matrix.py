r,c=map(int,input().split())
S=[]
for i in range(r):
    arr=list(map(int,input().split()))
    S.append(sum(arr))
print(max(S))
    