for _ in range(int(input())):
    a=int(input())
    b=list(map(int,input().split()))
    c=0
    for i in range(0,len(b)-1):
        if b[i]<b[i+1]:
            c+=1
    if c==(len(b)-1):
        print('0')
    else:
        print(max(b)-min(b))