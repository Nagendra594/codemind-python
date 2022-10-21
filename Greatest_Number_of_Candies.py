l=int(input())
arr=list(map(int,input().split()))
C=int(input())
for i in arr:
    if C+i>=max(arr):
        print('True',end=' ')
    else:
        print('False',end=' ')