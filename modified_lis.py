def modified_lis(arr):
	min_init = arr[0][0]
	i = 0
	min_idx = 0
	for a in arr:
		if a[0] < min_init:
			min_init = a[0]
			min_idx = i
		i+=1
	table = [1]*len(arr)
	res = []
	max_len = 0
	for i in range(1,len(arr)):
		res_tmp = [arr[i]]
		for j in range(0,i):
			if arr[j][1] < arr[i][0] and table[i] < table[j]+1:
				table[i] = table[j]+1
				res_tmp.append(arr[j])
		if len(res_tmp) > max_len:
			res = res_tmp
			max_len = len(res_tmp)
	print(sorted(res))
arr = [[27,40] ,[15,28] ,[5,24],[39,60],[50,90]]
modified_lis(arr)