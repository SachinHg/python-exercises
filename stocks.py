def stocks(A):
	min_init = A[0]
	# A = sorted(A)
	min_arr = [A[0]]
	res = []
	for i in range(1,len(A)):
		if A[i] < min_init:
			min_init = A[i]
		min_arr.append(min_init)
	print(min_arr)
	for i in range(len(A)):
		A[i] = A[i]-min_arr[i]
	max_prof = 0
	print(A)
	for i in range(len(A)):
		if A[i] > max_prof:
			max_prof = i
			day = i
	res.append(max_prof)

	return res

A = [23,13,25,29,33,19,34,45,65,67]
print(stocks(A))

