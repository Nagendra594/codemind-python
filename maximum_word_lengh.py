a=input()
B=a.split()
C=[]
for i in B:
    C.append(len(i))
print(max(C))