def merge(A,l,r,m):
	n1 = m-l+1
	n2 = r - (m)
	L = [0]*n1
	R = [0]*n2
	for i in range(n1):
		L[i] = A[l+i]
	for j in range(n2):
		R[j] = A[m+1+j]
	i = j = 0
	k = l
	while i < n1 and j < n2:
		if L[i] <= R[j]:
			A[k] = L[i]
			i+=1
		else:
			A[k] = R[j]
			j+=1
		k+=1
	while i < n1:
		A[k] = L[i]
		i+=1
		k+=1
	while j < n2:
		A[k] = R[j]
		j+=1
		k+=1

def merge_sort(A,l,r):
	if l < r:
		m = (l+r)//2
		merge_sort(A,l,m)
		merge_sort(A,m+1,r)
		merge(A,l,r,m)
	return A

A = [4,5,6,3,2,1,8,9,0]
print(merge_sort(A,0,len(A)-1))