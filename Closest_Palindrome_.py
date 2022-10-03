def po(a):
    ver=a
    rev=0
    while a:
        r=a%10
        rev=rev*10+r
        a//=10
    if rev==ver:
        return True
    else:
        return False
a=int(input())
A=[]
for i in range(a):
    if po(i):
        A.append(abs(i-a))
if po(abs(min(A)-a)) and po(min(A)+a):
    print(abs(min(A)-a),min(A)+a)
else:
    print(abs(min(A)-a))