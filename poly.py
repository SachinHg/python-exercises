def general_poly(L):
 	def inner(x):
 		sum = 0
 		k = len(L)
 		for i in L:
 			sum+= i*(x**(k-1))
 			k-=1
 		return sum
 	return inner

L = [1,2,3,4]
func = general_poly(L)
print(func(10))