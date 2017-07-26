def max_square(mat,r,c):
	aux = [[0]*c]*r
	print(mat)
	i = 0
	while i < r:
		aux[i][0] = mat[i][0]
		i+=1
	print(aux)
	j = 0
	while j < c:
		aux[0][j] = mat[0][j]
		j+=1
	print(aux)
	for i in range(1,r):
		for j in range(1,c):
			if mat[i][j] == 1:
				print(":::")
				aux[i][j] = 1+min(aux[i-1][j],aux[i-1][j-1],aux[i][j-1])
			else:
				aux[i][j] = 0
	print(aux)
	
	max_s = aux[0][0] 
	maxi = maxj = 0
	for i in range(1,r):
		for j in range(1,c):
			if aux[i][j] > max_s:
				max_s = aux[i][j]
				maxi = i
				maxj = j
	print(max_s)
	print(aux)
	print("::",maxi)
	print("<<>",maxj)
	for i in range(maxi,max_s-maxi,-1):
		for j in range(maxj,max_s-maxj,-1):
			print(mat[i][j])

mat = [[0, 1, 1, 0, 1], [1, 1, 0, 1, 0], [0, 1, 1, 1, 0],[1, 1, 1, 1, 0],[1, 1, 1, 1, 1],[0, 0, 0, 0, 0]]
max_square(mat,6,5)
