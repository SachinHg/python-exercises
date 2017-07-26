import math
def maxXor(arr):
	l = arr[0]
	r = arr[n-1]
	d = l^r
	digits = math.log(d,2)
	guess = math.ceil(digits)
	res = (2**guess)-1
	return res

n = int(input())
arr = list(map(int,input().split(' ')))
print(maxXor(arr))
