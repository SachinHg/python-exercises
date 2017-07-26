import math

n = int(input('Enter the value of n'))
d = int(input('Enter the number of digits after decimal point'))
i=0
sum1 = 0.0
while i<=n:
	sum1+= 1/math.factorial(i)
	i+=1
print(round(sum1,d))