def equilibrium(A):
	s = sum(A)
	sum_till = 0
	for i in range(len(A)):
		print(i,sum_till,(s-A[i])//2)
		if sum_till == (s - A[i])/2:
			return i
		sum_till+= A[i]
	return False

A = [1,3,4,9,3,2,3]
print(equilibrium(A))
