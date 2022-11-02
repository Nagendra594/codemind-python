a=input()
B=a.split()
for i in range(0,len(B),2):
    b=B[i]
    B.remove(B[i])
    B.insert(i,b[::-1])
S=' '.join(B)
print(S)