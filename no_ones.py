def countbits(n):
	binary = bin(n)[2:]
	return binary.count('1')

print(countbits(15))