def min_dist(s1,s2,l1,l2):
	diff_mat = [[0  for x in range(l2+1)] for x in range(l1+1)]
	for i in range(l1+1):
		for j in range(l2+1):
			if i==0:
				diff_mat[i][j] = j
			elif j == 0:
				diff_mat[i][j] = i
			elif s1[i-1] == s2[j-1]:
				diff_mat[i][j] = diff_mat[i-1][j-1]
			else:
				diff_mat[i][j] = min(diff_mat[i-1][j],diff_mat[i][j-1],diff_mat[i-1][j-1])+1
	print (diff_mat[l1-1][l2-1])

s1 = "monday"
s2 = "mundane"
min_dist(s1,s2,len(s1),len(s2))

