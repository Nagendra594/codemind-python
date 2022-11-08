a=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if i%2:
        c+=1
print('YES' if c<=2 else 'NO')