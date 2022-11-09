a=input()
ans=[]
Ans=''
v='aeiou'
c=0
for i in a:
	if i in v:
		ans.append('V')
	else:
		ans.append('C')
M=''
for i in ans:
	if i in M:
		pass
	else:
		Ans+=i
		M=i
	
print(Ans)