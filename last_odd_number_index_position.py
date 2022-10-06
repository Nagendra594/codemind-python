a=int(input())
c=list(map(int,input().split()))
b=0
for i in range(-1,-(len(c)+1),-1):
    b+=1
    if c[i]%2!=0:
        break
print(a-b)