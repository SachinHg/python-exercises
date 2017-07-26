def repeatedNumber(A):
	h = {}
	for n in A:
		if h.get(n,0) == 0:
			h[n]=1
		else:
			h[n]+=1
	print(h)
	for i in range(1,len(A)+1):
		if h.get(i,0) == 0:
			notf = i
		if h.get(i,0) > 1:
			repeatf = i
	res = [repeatf, notf]
	return res
A = [3,1,2,5,3]
print(repeatedNumber(A))
