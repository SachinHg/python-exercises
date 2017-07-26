def flip(A):
	A = list(str(A))
	n = len(A)
	aa = [0]*n
	res = [-1,-1]
	if A.count('1') == len(A):
		return []
	for i in range(n):
		if A[i] == '1':
			aa[i]=-1
		else:
			aa[i]=1
	best_end = best_till = l = 0
	for i in range(n):
		if best_end+aa[i]<0:
			l=i+1
			best_end = 0
		else:
			best_end+=aa[i]
		if best_end > best_till:
			best_till = best_end
			res = [l,i]

	if res[0] == -1:
		return []
	else:
		return res

A = '10001'
print(flip(A))