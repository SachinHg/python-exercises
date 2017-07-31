def spiral_matrix(A,rows,cols):
	k = 0
	l = 0
	while k < rows and l < cols:
		for i in range(l,cols):
			print(A[k][i],end=' ')
		k+=1
		for i in range(k,rows):
			print(A[i][cols-1],end=' ')
		cols-=1
		if k < rows:
			for i in range(cols-1,0,-1):
				print(A[rows-1][i],end=' ')
			rows-=1
		if l < cols:
			for i in range(rows-1,k-1,-1):
				print(A[i][l],end = ' ')
			l+=1

a = [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18]]
spiral_matrix(a,3,6)
