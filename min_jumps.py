def min_jumps(arr):
	l = len(arr)
	jump_counts = jumPidcs = [0]*l
	jump_counts[0] = jumPidcs[0] = 0
	for i in range(1,l):
		for j in range(0,i):
			if j + arr[j] >= i:
				if jump_counts[i] == 0:
					jump_counts[i] = jump_counts[j]+1
				else:
					jump_counts[i] = min(jump_counts[i],jump_counts[j]+1)

	print(jump_counts[l-1])		
# arr = [2,3,1,1,2,4,2,0,1,1]
#arr =[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
arr = [5,1,6]
min_jumps(arr)