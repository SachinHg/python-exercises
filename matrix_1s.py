def max1s_matrix(arr,n):
	S = [[0 for i in range(n)] for j in range(n)]
	max_ret = 0
	for i in range(1,n):
		for j in range(1,n):
			if arr[i][j] == 1:
				S[i][j] = min(S[i][j-1],S[i-1][j],S[i-1][j-1])+1
				if S[i][j]> max_ret:
					max_ret = S[i][j]
	return max_ret

a = [[0,1,1,0,1],[1,1,0,1,0],[0,1,1,1,0],[1,1,1,1,0],[1,1,1,1,1],[0,0,0,0,0]]
print(max1s_matrix(a,5))