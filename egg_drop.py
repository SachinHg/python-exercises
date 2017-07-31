def egg_drop(eggs,floors):
	mat = [[0 for i in range(floors+1)] for j in range(eggs+1)]
	for i in range(1,eggs+1):
		mat[i][0] = 0
		mat[i][1] = 1
	for j in range(1,floors+1):
		mat[1][j] = j
	for i in range(2,eggs+1):
		for j in range(2,floors+1):
			mat[i][j] = 999999999
			for x in range(1,j+1):
				res = 1 + max(mat[i-1][x-1], mat[i][j-x])
				if res < mat[i][j]:
					mat[i][j] = res
	return mat
eggs = 2
floors = 6
print(egg_drop(eggs,floors))