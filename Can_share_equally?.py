x,y=map(int,input().split())
c=(y*2)+x
if x==0 and y%2!=0:
    print('NO')
elif c%2!=0:
    print('NO')
else:
    print('YES')
