for _ in range(int(input())):
    c,b=map(int,input().split())
    a=input()
    final=''
    for i in range(b-1,0,-1):
        final=(a[i::-1]+a[i+1:])
        a=final
    print(final)
