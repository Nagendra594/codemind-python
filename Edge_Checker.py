a,b=map(int,input().split())
if a==1 and b==10:
    print('Yes')
elif a==10 and b==1:
    print('Yes')
elif a+1==b or a-1==b:
    print('Yes')
else:
    print('No')