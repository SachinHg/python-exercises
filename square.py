import math

def is_triangular(k):
	root = k**(1/2)
	init = math.floor(root)
	chk_val = 1
	diff = k - chk_val
	while(diff > 0):
		chk_val = init*(init+1)/2
		init+=1
		diff = k - chk_val
	if diff == 0:
		return True
	else:
		return False

print(is_triangular(2))
