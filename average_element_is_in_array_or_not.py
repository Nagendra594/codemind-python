a=int(input())
b=list(map(int,input().split()))
print('True')if sum(b)//a in b else print('False')
