def bracket_match(string):
	diff = 0
	ans = 0
	n = len(string)
	for i in range(n):
		if string[i] == '(':
			diff+=1
		elif string[i] == ')':
			diff-=1
		if diff < 0:
			diff+=1
			ans+=1
	return ans+diff

string = input('Enter the string with brackets')
print(bracket_match(string))