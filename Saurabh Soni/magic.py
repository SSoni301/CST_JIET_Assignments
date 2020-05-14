num =int(input(">>"))
while(len(str(num))!=1 ):
	sum = 0
	nu = num
	while(nu!=0):
		sum = sum + (nu%10)
		nu = nu/10
	num = sum
if(num == 1):
	print("magic no.")
else:
	print("not a magic no.") 
