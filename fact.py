def fact(n,fact_arr):
	if n == 1 or n == 0:
		return 1
	elif fact_arr[n]!=0:
		return fact_arr[n]
	else:
		fact_arr[n] = n * fact(n-1,fact_arr)
	return fact_arr[n]

n = int(input('Enter the number to calculate the factorial!'))
fact_arr = [0 for i in range(n+1)]
fact_val = fact(n,fact_arr)
print(fact_val)