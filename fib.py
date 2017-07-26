def fib(n):

	a= 0
	b = 1
	i = 0
	while i < n:
		sum = a + b
		a =b
		b = sum
		i+=1
	return sum

n = int(input('Enter the value of n to find its fibonacci number'))
fib_value = fib(n)
print(fib_value)