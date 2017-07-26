def dict_invert(d):
	values = d.values()
	values = list(set(values))
	invert_dict = {}
	for v in values:
		v_array = []
		for k in d:
			if d[k] == v:
				v_array.append(k)
		v_dup = v_array[:]
		v_dup.sort()
		invert_dict[v] = v_dup
	return invert_dict

d = {1:10,2:20,3:30,4:30}
print(dict_invert(d))