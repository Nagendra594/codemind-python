for _ in range(int(input())):
    l=int(input())
    arr=list(map(int,input().split()))
    c=0
    for i in arr:
        for j in range(arr.index(i)+1,l):
            if i+arr[j] in arr:
                c+=1
    if c>0:
        print(c)
    else:
        print('-1')
                
