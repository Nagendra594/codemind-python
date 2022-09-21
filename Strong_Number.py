def f(a):
    s=1
    for i in range(1,a+1):
            s*=i
    return s
a=int(input())
b=a
s=0
while a:#145
    r=a%10#5
    s+=f(r)#s=0+
    a//=10
if s==b:
    print('The number',b,'is a strong number')
else:
    print('The number',b,'is not a strong number')