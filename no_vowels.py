def print_without_vowels(s):
	vowels = ['a','e','i','o','u','A','E','I','O','U']
	s_arr = list(s)
	if (s_arr != ['a'] or s_arr != ['A']):
		s_arr = ['' if ch in vowels else ch for ch in s_arr]
		print (''.join(s_arr))

print(print_without_vowels("abbaba"))