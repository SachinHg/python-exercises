def ugly(n):
	ugly = [0]*n
	ugly[0] = 1
	i2=i3=i5=0
	mul_2 = 2
	mul_3 = 3
	mul_5 = 5

	for i in range(1,n):
		ugly[i] = min(mul_2,mul_3,mul_5)
		if ugly[i] == mul_2:
			i2+=1
			mul_2 = ugly[i2]*2
		if ugly[i] == mul_3:
			i3+=1
			mul_3 = ugly[i3]*3
		if ugly[i] == mul_5:
			i5+=1
			mul_5 = ugly[i5]*5
	return(ugly[-1])

print(ugly(150))	
