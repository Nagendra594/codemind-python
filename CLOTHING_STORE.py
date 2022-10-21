l=int(input())
arr=list(map(int,input().split()))
s=set(arr)
pairs=0
for i in s:
    pairs+=(arr.count(i)//2)
print(pairs)
    