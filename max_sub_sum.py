#max sub array sum dynamic 

arr = list(map(int,input().split(' ')))
l = len(arr)
max_end_here = max_so_far = arr[0]
for i in range(0,l):
	max_end_here = max_end_here+arr[i]
	if max_end_here < 0:
		max_end_here = 0
	elif max_so_far < max_end_here:
		max_so_far = max_end_here
print(max_so_far)
	

