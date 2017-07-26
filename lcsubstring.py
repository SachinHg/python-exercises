# Enter your code here. Read input from STDIN. Print output to STDOUT
def lcs(X, Y, m, n):
	res = 0
	L = [[0 for x in range(n+1)] for x in range(m+1)]
	for i in range(m+1):
		for j in range(n+1):
			if i == 0 or j == 0:
				L[i][j] = 0
			elif X[i-1] == Y[j-1]:
				L[i][j] = L[i-1][j-1] + 1
				###for lc substring
				res = max(res,L[i][j])
			else:
				#L[i][j] = max(L[i-1][j], L[i][j-1])
				L[i][j] = 0
	return res

t = int(input())
for _ in range(t):
     s1 = list(input())
     l1 = len(s1)
     s2 = list(input())
     l2 = len(s2)
     print(lcs(s1,s2,l1,l2))