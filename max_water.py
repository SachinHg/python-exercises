def max_water(A):
	n = len(A)
	max_left = max_right = 0
	water = 0
	low = 0
	high = n-1
	while low <= high:
		if A[low] < A[high]:
			if A[low] > max_left:
				max_left = A[low]
			else:
				water+=max_left - A[low]
				low+=1
		else:
			if A[high] > max_right:
				max_right = A[high]
			else:
				water+= max_right - A[high]
				high-=1
	return water


a = [0,1,0,2,1,0,1,3,2,1,2,1]
print(max_water(a))