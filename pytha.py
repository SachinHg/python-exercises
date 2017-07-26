def chocolates(A,m):
	A = sorted(A)
	i = 0
	min_diff = 99999999
	while i+m-1 < len(A):
		diff = A[i+m-1]-A[i]
		if diff < min_diff:
			min_diff = diff
			first = i
			last = i+m-1
		i+=1
	diff_res = 0
	A_res = A[first:last+1]
	for ii in range(len(A_res)-1,0,-1):
		for jj in range(ii-1,-1,-1):
			diff_res+=A_res[ii]-A_res[jj]
	return diff_res

q = int(input())
m = int(input())
A = []
for t in range(q):
    A.append(int(input()))
A = sorted(A)
print(chocolates(A,m))


    