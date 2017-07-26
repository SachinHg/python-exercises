def sortthrees(A):
	l = len(A)
	j = 0
	k = l-1
	res = [1]*l
	for i in range(l):
		if A[i] == 0:
			res[j] = 0
			j+=1
		elif A[i] == 2:
			res[k] = 2
			k-=1
		else:
			res[j]=1
	return res

A = [0,1,1,1,1,0,0,0,0,0,0,0,0]
print(sortthrees(A))