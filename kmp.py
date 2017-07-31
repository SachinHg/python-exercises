def computeLPS(pat,M,lps):
	l = 0
	lps[0] = 0
	while i < M:
		if pat[i] == pat[l]:
			l+=1
			lps[i] = l
			i+=1
		else:
			if lps[i]!=0:
				l = lps[l-1]
			else:
				lps[i] = 0
				i+=1
def KMPsearch(pat,txt):
	m = len(pat)
	n = len(txt)
	lps = [0]*m
	j = 0
	computeLPS(pat,m,lps)
	i = 0
	while i < n:
		if pat[j] == txt[i]:
			j+=1
			i+=1
		if j == m:
			print("found at "+str(i-j))
		elif i < n and pat[j]!=txt[i]:
			if j!=0:
				j = lps[j-1]
			else:
				i+=1
