def heapify(A,n,i):
	large = i
	l = 2*i+1
	r = 2*i+2
	if l < n and A[i] < A[l]:
		large = l
	if r < n and A[large] < A[r]:
		large = r
	if large!=i:
		A[i],A[large] = A[large],A[i]
		heapify(A,n,large)

def heapsort(A):
	n = len(A)
	for i in range(n,-1,-1):
		heapify(A,n,i)
	for i in range(n-1,0,-1):
		A[i],A[0] = A[0],A[i]
		heapify(A,i,0)
	return A

A = [5,6,3,4,1,9,0,2]
print(heapsort(A))