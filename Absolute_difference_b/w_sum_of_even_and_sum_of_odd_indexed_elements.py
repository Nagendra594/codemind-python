a=int(input())
l=list(map(int,input().split()))
E=0
O=0
for i in range(len(l)):
    if i%2==0:
        E+=l[i]
    else:
        O+=l[i]
print(abs(E-O))