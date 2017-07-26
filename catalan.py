
# recursive function
def catalan(n):
	if n <=1:
		return 1
	ress = 0
	for i in range(0,n):
		# for j in range(i):
		ress+=catalan(i)*catalan(n-i-1)
	return ress
### dynamic solution
def catalan_dynamic(n,res):
	for i in range(2,n):
		res[i] = 0
		for j in range(0,i):
			res[i]+=res[j]*res[i-j-1]
	return res[n-1]


n = int(input('Enter the value of n'))
res = [0] * (n+1)
res[0] = 1
res[1] = 1
print(catalan(n))
print(catalan_dynamic(n,res))