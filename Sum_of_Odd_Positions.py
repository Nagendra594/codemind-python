a=int(input())
l=list(map(int,input().split()))
O=0
for i in range(len(l)):
    if i%2!=0:
        O+=l[i]
print(O)