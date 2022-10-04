a=int(input())
l=list(map(int,input().split()))
E=0
O=0
for i in l:
    if i%2==0:
        E+=i
    else:
        O+=i
print(abs(E-O))