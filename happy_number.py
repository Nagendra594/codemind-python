def hp(a):
    s=0
    while a:
        r=a%10
        s+=r**2
        a//=10
    if s<10:
        return s
    else:
        return hp(s)
a=int(input())
if hp(a)==1 or hp(a)==7:
    print('True')
else:
    print('False')

        