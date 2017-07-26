def assembly(line1,line2,costs1,costs2,e1,e2,x1,x2):
	num = len(line1)
	t1 = [0]*num
	t2 = [0]*num
	t1[0] = e1 + line1[0]
	t2[0] = e2 + line2[0]
	for i in range(1,num):
		t1[i] = min(t1[i-1]+line1[i], t2[i-1]+costs2[i]+line1[i])
		t2[i] = min(t2[i-1]+line2[i], t1[i-1]+costs1[i]+line2[i])
	print(min(t2[num-1]+x2,t1[num-1]+x1))

line1 = [4,5,3,2]
line2 = [2,10,1,4]
costs1 = [0,7,4,5]
costs2 = [0,9,2,8]
e1 = 10
e2 = 12
x1 = 18
x2 = 7
assembly(line1,line2,costs1,costs2,e1,e2,x1,x2)