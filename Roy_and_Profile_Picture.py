a=int(input())
for _ in range(int(input())):
    w,l=map(int,input().split())
    if w>=a and l>=a:
        if w==l:
            print('ACCEPTED')
        else:
            print('CROP IT')
    else:
        print('UPLOAD ANOTHER')
     
     
   