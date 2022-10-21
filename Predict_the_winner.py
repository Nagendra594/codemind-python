a=int(input())
arr=list(map(int,input().split()))
X=[]
Y=[]
for i in range(0,a-1,2):
    X.append(arr[i])
    Y.append(arr[i+1])
if (sum(X)-sum(Y))%4==0:
    print('X')
else:
    print('Y')