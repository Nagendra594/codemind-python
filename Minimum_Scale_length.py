def gcd(a,b):
    c=0
    for i in range(1,max(a,b)+1):
        if a%i==0 and b%i==0:
            c=i
    return c
def gd(nums):
    if len(nums)==1:
        return 0
    G=gcd(nums[0],nums[1])
    if len(nums)==2:
        return G
    if len(nums)>2:
        for i in range(1,len(nums)-1):
            G=gcd(G,nums[i+1])
            return G
    return G
a=int(input())
a=list(map(int,input().split()))
print(gd(a))
    
            