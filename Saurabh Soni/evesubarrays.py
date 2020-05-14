n=input().split()
c=0
for i in range(len(n)):
	k=[]
	for j in range(i,len(n)):
		k.append(j)
		h=1
		for i in k:
			if i%2==0:
				h=0
		if h==1:
			c+=1
print(c)