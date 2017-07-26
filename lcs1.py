### brute force sub problem overlapping
# def lcs(s1,s2,l1,l2):
# 	print("::")
# 	if l1==0 or l2==0:
# 		return 0
# 	else:
# 		if s1[l1-1] == s2[l2-1]:
# 			return 1+lcs(s1,s2,l1-1,l2-1)
# 		else:
# 			return max(lcs(s1,s2,l1-1,l2),lcs(s1,s2,l1,l2-1))

### dynamic programming

def lcs(X, Y, m, n):
	L = [[0 for x in range(n+1)] for x in range(m+1)]
	for i in range(m+1):
		for j in range(n+1):
			if i == 0 or j == 0:
				L[i][j] = 0
			elif X[i-1] == Y[j-1]:
				L[i][j] = L[i-1][j-1] + 1
			else:
				L[i][j] = max(L[i-1][j], L[i][j-1])
	index = L[m][n]
	lcs = [""] * (index)
	#lcs[index] = "\0"
	i = m
	j = n
	while i > 0 and j > 0:
		if X[i-1] == Y[j-1]:
			lcs[index-1] = X[i-1]
			i-=1
			j-=1
			index-=1
		elif L[i-1][j] > L[i][j-1]:
			i-=1
		else:
			j-=1
	print(lcs)

X = [1,2,3,4,1]
Y = [2,3,4,1,2,3]
m = len(X)
n = len(Y)
lcs(X, Y, m, n)