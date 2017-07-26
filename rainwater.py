def rainwater(A):
	init = [A[0]]
	quant = 0
	max_till = A[0]
	for i in range(1,len(A)-1):
		quant+=max_till-A[i]
	return quant

# A = [3,0,0,2,0,4]
A = [3,0,1,2,4,0,0,3,6]
print(rainwater(A))

