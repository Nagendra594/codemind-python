def sd(a):
    s=0
    while a:
        s+=(a%10)
        a=(a-a%10)//10
    if s<10:
        return s
    else:
        return sd(s)
a=int(input())
print(sd(a))