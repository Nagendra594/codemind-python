arr_1=list(map(int,input().split()))
arr_2=list(map(int,input().split()))
Alice=0
Bob=0
for i in range(len(arr_1)):
    if arr_1[i]==arr_2[i]:
        pass
    elif arr_1[i]>arr_2[i]:
        Alice+=1
    else:
        Bob+=1
print(Alice,Bob)