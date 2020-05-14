n=input().split()
e=o=0
for i in n:
	if i%2==0:
		e+=1
	else:
		o+=1
if(e>o):
	print(o)
else:
	print(e)
