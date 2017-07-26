# Enter your code here. Read input from STDIN. Print output to STDOUT
def getminsquares(n):
	table = [0]*(n+1)
	for i in range(4):
		table[i] = i
	for i in range(4,n+1):
		table[i] = i
		for x in range(1,i+1):
			t = x*x
			if t > i:
				break
			else:
				table[i] = min(table[i],1+table[i-t])
	return table[n]

print(getminsquares(99))