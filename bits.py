def totalbits_each(x):
	print(":::::",x)
	if x<=0:
		return 0
	else:
		if x%2 == 0:
			return 1+totalbits_each(x//2)
		else:
			return totalbits_each(x//2)

def totalbits(b):
	cnt = 0
	for i in range(1,b+1):
		i = int(bin(i)[2:])
		cnt+=totalbits_each(i)
	return cnt

t = int(input())
for i in range(t):
	n = int(input())

	print(totalbits(n))