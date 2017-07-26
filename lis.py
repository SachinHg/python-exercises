def longestincrsubseq(string,table):
	maxx = 0
	for i in range(len(string)):
		table[i] = 1
	for i in range(len(string)):
		for j in range(i):
			if string[i] > string[j] and table[i] < table[j]+1:
				table[i]=table[j]+1
		if table[i] > maxx:
			maxx = table[i]
	return maxx
	# return m[0]

# size = int(input())
# for i in range(size):
# 	arr.append(int(input()))
# table = [0]*size
# print(longestincrsubseq(string,table))



#### Easier and readable code

def CeilIndex(v,l,r,key):
	while r-l > 1:
		m = l+(r-l)//2
		if v[m]>=key:
			r = m
		else:
			l = m
	return r

def LongestIncreasingSubsequenceLength(v):
	if len(v) == 0:
		return 0
	tail = [0]*len(v)
	tail[0] = v[0]
	length = 1
	for i in range(1,len(v)):
		if v[i] < tail[0]:
			tail[0] = v[i]
		elif v[i] > tail[length-1]:
			tail[length] = v[i]
			length+=1
		else:
			tail[CeilIndex(tail,-1,length-1,v[i])] = v[i]
	return length

v = [2, 5, 3, 7, 11, 8, 10, 13, 6]
print(LongestIncreasingSubsequenceLength(v))
