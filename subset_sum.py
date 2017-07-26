def isSumSubSet(arr,n,sum):
	check_arr = [[0]*(sum1+1)]*(n+1)
	for i in (0,n):
		check_arr[i][0] = 1
	for i in (1,sum1):
		check_arr[0][i] = 0
	for i in range(1,n+1):
		for j in range(1,sum1+1):
			if j < arr[i-1]:
				check_arr[i][j] = check_arr[i-1][j]
			else:
				check_arr[i][j] = max(check_arr[i-1][j],check_arr[i-1][j-arr[i-1]])
	print(check_arr[n-1][sum1-1])

arr = [0,0,0,0]
sum1 = 3
arr = [x % sum1 for x in arr]
isSumSubSet(arr,len(arr),sum1)