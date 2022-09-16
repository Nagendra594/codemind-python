for _ in range(int(input())):
    a=int(input())
    for i in range(1,a):
        b=i**2
        if b==a:
            print('True')
            break
 
    else:
        print('False')
        