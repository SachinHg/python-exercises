def long_substr(str1, str2,l1,l2):
	if l1 == 0 or l2 == 0:
		print(0)
	res = [[0]*(l2+1)]*(l1+1)
	l_fin = 0
	for i in range(1,l1):
		for j in range(1,l2):
			if str1[i-1] ==  str2[j-1]:
				res[i][j] = res[i-1][j-1]+1
				l_fin = max(res[i][j],l_fin)
	print(l_fin)


str1 = "Monday"
str2 = "Sonday"
long_substr(str1,str2,len(str1),len(str2))