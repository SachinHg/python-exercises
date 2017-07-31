def stocks_mul(A):
	res = []
	print(A)
	n = len(A)
	if n == 1:
		return 0 
	count = 0
	i = 0
	print(res)
	while i < n-1:
		while i < n-1 and A[i+1] <= A[i]:
			i+=1
		if i == n-1:
			break
		res.append(['buy',i])
		i+=1
		while i < n and A[i] >= A[i-1]:
			i+=1
		res.append(['sell',i-1])
		count+=1
	print(res)
	if count == 0:
		print("No solution")
	else:
		return res

A = [100,180,260,310,40,535,695]
stocks_mul(A)
