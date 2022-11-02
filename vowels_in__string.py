a=input()
v=['a','e','i','o','u','A','E','I','O','U']
F=[]
for i in a:
    if i in v:
        if i in F:
            pass
        else:
            F.append(i)
if len(F)==0:
    print('-1')
else:
    print(*F)