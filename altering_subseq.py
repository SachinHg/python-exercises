def altering_subseq(arr,n):
	length = [[0 for i in range(2)] for j in range(n)]
	res = 1
	for i in range(n):
		length[i][0] = length[i][1] = 1
	for i in range(1,n):
		for j in range(i):
			if arr[j] < arr[i] and length[i][0] < length[j][1]+1:
				length[i][0] = length[j][1]+1
			if arr[j] > arr[i] and length[i][1] < length[j][0]+1:
				length[i][1] = length[j][0]+1
		res = max(res,length[i][0],length[i][1])
	return res
res = []
t = int(input())
for _ in range(t):
	l = int(input())
	arr = list(map(int,input().split(' ')))
	res.append(altering_subseq(arr,l))
for r in res:
	print(r)