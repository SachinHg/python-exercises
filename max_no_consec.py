# Enter your code here. Read input from STDIN. Print output to STDOUT
def max_sum(array,n):
	till_this = 0
	except_this = 0
	for i in array:
		new_except = except_this if except_this > till_this else till_this
		till_this = except_this+i
		except_this = new_except
	return(except_this if except_this > till_this else till_this)


t = int(input())
res = []
for i in range(t):
	size = int(input())
	arr = list(map(int,input().split(' ')))
	sum1 = max_sum(arr,size)
	res.append(sum1)
for s in res:
     print(s)