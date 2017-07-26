def lis_sum(arr):
	l = [0]*len(arr)
	l[0] = arr[0]
	for i in range(1,len(arr)):
		for j in range(0,i):
			if arr[i] > arr[j] and l[i]<l[j]+arr[i]:
				l[i] = l[j]+arr[i]
	print(max(l))

arr = [1, 101, 2, 3, 100, 4, 5]
lis_sum(arr)