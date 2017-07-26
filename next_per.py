def next_per(A):
	i = len(A)-1
	while i > 0 and A[i-1] >= A[i]:
		i-=1
	if i <=0:
		return sorted(A)
	j = len(A) - 1
	while A[j] <=A[i-1]:
		j-=1
	A[i-1],A[j] = A[j],A[i-1]
	A[i:] = A[len(A)-1:i-1:-1]
	return A

#A = [1,2,3]
A = [3,2,1]
A = [1,1,5]
A = [20,50,113]
print(next_per(A))