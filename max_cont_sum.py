# def maxSubArray(A):
# 	if not A:
# 		return 0
# 	sum_now = sum_max = A[0]
# 	for n in A[1:]:
# 		sum_now = max(n,sum_now+n)
# 		sum_max = max(sum_max,sum_now)
# 	return sum_max

def max_sum(array,n):
	sum_now = 0
	sum_end = 0
	for i in range(n):
		sum_end+=array[i]
		if sum_end < 0:
			sum_end = 0
			continue
		if sum_end > sum_now:
			sum_now = sum_end
	return sum_now

n = int(input('Enter the size of the array'))
array = input('Enter the array of numbers')
array = list(map(int, array.split(' ')))
print(max_sum(array,n))
