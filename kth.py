def partition(A,l,r):
	low = l
	while l < r:
		if A[l] < A[r]:
			A[l],A[low] = A[low],A[l]
			low+=1
		l+=1
	A[low],A[r] = A[r],A[low]
	return low

def kth(A,k):
	if A:
		pos = partition(A,0,len(A)-1)
		if k > pos+1:
			return kth(A[pos+1:],k-pos-1)
		elif k < pos+1:
			return kth(A[:pos],k)
		else:
			return A[pos]

A = [1,2,3,4,4,6,7]
k = 5
print(kth(A,k))