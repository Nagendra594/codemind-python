for _ in range(int(input())):
    L,R=map(int,input().split())
    arr=list(map(int,input().split()))
    for i in range(R):
        n=arr.pop()
        arr.insert(0,n)
    print(*arr)