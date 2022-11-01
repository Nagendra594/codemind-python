a=int(input())
ar=list(map(int,input().split()))
print(sum(ar[:a//2]))
print(sum(ar[a//2:]))