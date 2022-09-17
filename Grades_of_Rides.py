a,b,c=map(int,input().split())
if a>50 and b>60 and c>100:
    print('10')
elif a>50 and b>60 and c<100:
    print('9')
elif a<50 and b>60 and c>100:
    print('8')
elif a>50 and b<60 and c>100:
    print('7')
elif a>50 or b>60 or c>100:
    print('6')
else:
    print('5')