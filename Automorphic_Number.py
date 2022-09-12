a=input()
b=int(a)
c=b**2
d=c%(10**(len(a)))
if d==b:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')