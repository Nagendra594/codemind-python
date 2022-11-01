a=int(input())
ar=list(map(int,input().split()))
M=a//2
print(abs(sum(ar[:M])-sum(ar[M:])))