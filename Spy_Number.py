def sd(a):
    A=[]
    while a>0:
        A.append(a%10)
        a=(a-a%10)//10
    return A
def pr(a):
    b=1
    for i in sd(a):
        b*=i
    return b
a=int(input())
if sum(sd(a))==pr(a):
    print('Spy Number')
else:
    print('Not Spy Number')