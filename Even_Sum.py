a=int(input())
l=list(map(int,input().split()))
E=0
for i in l:
    if i%2==0:
        E+=i
print(E)