a=int(input())
b=int(input())
s=0
for i in range(a):
    arr=list(map(int,input().split()))
    for j in arr:
        s+=j
print(s)
    