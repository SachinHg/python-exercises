def all_paths(r,c):
	res = [[0]*c]*r
	for i in range(r):
		res[i][0] = 1
	for j in range(c):
		res[0][j] = 1
	for i in range(1,r):
		for j in range(1,c):
			res[i][j] = res[i-1][j] + res[i][j-1]
	print(res[r-1][c-1])
all_paths(3,3)
