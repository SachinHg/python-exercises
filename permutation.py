def is_list_permutation(L1,L2):
	if len(L1)==0 and len(L2)==0:
		return (None,None,None)
	if len(L1) == len(L2):
		dict_tmp = {}
		set1 = set(L1)
		set2 = set(L2)
		for s in set1:
			count1 = L1.count(s)
			count2 = L2.count(s)
			if count1 != count2:
				return False
			else:
				dict_tmp[s] = count1
		d_vals = list(dict_tmp.values())
		max_val = max(d_vals)
		for k,v in dict_tmp.items():
			if v == max_val:
				key = k
				type1 = type(key)
				break
		return (key,max_val,type1)
	else:
		return False

L1 = []
L2 = []
print(is_list_permutation(L1,L2))