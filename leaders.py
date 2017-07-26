def leaders(A):
	A = A[::-1]
	res = [A[0]]
	max_till = A[0]
	for i in range(1,len(A)):
		flag = True
		if A[i] < max_till:
			flag = False
		else:
			max_till = A[i]
		if flag == True:
			res.append(A[i])
	return res[::-1]

A = [3,4,5,6,7,1,2,1,4,6,4,3,1]
print(leaders(A))

