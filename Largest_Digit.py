a=int(input())
A=[]
while a:
    A.append(a%10)
    a=(a-a%10)//10
print(max(A))