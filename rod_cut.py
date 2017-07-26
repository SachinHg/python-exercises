def cut_rod(amount,n):
	mat = [0]*(n+1)
	for i in range(1,n+1):
		max_t = 0
		print("*********")
		for j in range(i):
			print("::::::",amount[j],mat[i-j-1])
			max_t = max(max_t,amount[j]+mat[i-j-1])
		mat[i] = max_t
		print(mat)
	print(mat[n])
arr = [1,5,8,9,10,17,17,20]
cut_rod(arr,len(arr))