import math

def is_prime(n):
	j=2
	while j <= math.sqrt(n):
		if n%j == 0:
			return 0
		else:
			j+=1
	return 1


n = int(input('Enter the value of n'))
primes = [1]
i = 2
while i <= math.sqrt(n):
	if is_prime(i) == 1:
		if n%i==0:
			n = n/i
			primes.append(i)
	i+=1
print(primes)