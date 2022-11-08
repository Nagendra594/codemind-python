r,c=map(int,input().split())
S=[]
for i in range(r):
    arr=list(map(int,input().split()))
    S.extend([arr])
s=[]
for i in range(c):
    ss=[]
    for j in range(r):
        ss.append(S[j][i])
    s.append(sum(ss))
print(max(s))