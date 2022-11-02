a=input()
B=a.split()
for i in range(len(B)):
    b=B[i]
    B.remove(B[i])
    B.insert(i,b[::-1])
S=' '.join(B)
print(S)