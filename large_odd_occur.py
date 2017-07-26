def largest_odd_times(L):
	max_init = max(L)
	max_count = L.count(max_init)
	while(max_count%2==0 and len(L)>0):
		L = [i for i in L if i !=max_init]
		if len(L) > 0:
			max_init = max(L)
			max_count = L.count(max_init)
		else:
			return 

	return(max_init)

print(largest_odd_time([5,5,5,5,2,2,4,4,4]))