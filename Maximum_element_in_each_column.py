a,b=map(int,input().split())
m=[]
for i in range(a):
    m.extend([list(map(int,input().split()))])
for i in range(b):
    n=[]
    for j in range(a):
        n.append(m[j][i])
    print(max(n))
    