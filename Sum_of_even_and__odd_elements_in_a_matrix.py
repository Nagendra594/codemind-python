r,c=map(int,input().split())
o=0
e=0
for i in range(r):
    arr=list(map(int,input().split()))
    for i in arr:
        if i%2:
            o+=i
        else:
            e+=i
print(e,o)
