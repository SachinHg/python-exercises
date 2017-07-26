def no3(n):
	if n<3:
		return n
	if n>=3 and n<10:
		return n-1
	po = 1
	while n//po > 9:
		po*=10
		#n//=po
	msd = n//po
	if msd != 3:
		return no3(msd)*no3(po-1)+no3(msd)+no3(n%po)
	else:
		return no3(msd*po-1)

print(no3(578))