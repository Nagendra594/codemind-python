def sub_lists (l):
	lists = [[]]
	for i in range(len(l) + 1):
		for j in range(i):
			lists.append(l[j: i])
	return lists
a=int(input())
b=int(input())
l1=[]
for i in range(a,b+1):
    l1.append(i)
l2=sub_lists(l1)
c=0
for i in range(len(l2)):
    if (sum(l2[i]))%2!=0:
        c+=1
print(c)
