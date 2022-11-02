N,K=map(int,input().split())
ar=list(map(int,input().split()))
c=0
for i in ar:
    if i%K==0:
        c+=1
print(c)