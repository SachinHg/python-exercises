def lcs(s1,l1,s2,l2,l_arr):
	for i in range(0,l1+1):
		l_arr[i][l2] = 0
	for i in range(0,l2+1):
		l_arr[l1][i] = 0
	for i in range(l1-1,-1,-1):
		for j in range(l2-1,-1,-1):
			l_arr[i][j] = l_arr[i+1][j+1]
			if s1[i] == s2[j]:
				l_arr[i][j]+=1
			if l_arr[i][j+1] > l_arr[i][j]:
				l_arr[i][j] = l_arr[i][j+1]
			if l_arr[i+1][j] > l_arr[i][j]:
				l_arr[i][j] = l_arr[j+1][j]
	return l_arr[0][0]

str1 = list(input('Enter string 1'))
len1 = len(str1)
str2 = list(input('Enter string 2'))
len2 = len(str2)
lcs_array = [[0 for i in range(1025)] for i in range(1025)]
print(lcs(str1,len1,str2,len2,lcs_array))