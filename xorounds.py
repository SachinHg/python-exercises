n,rounds = map(int,input().split(' '))
binary = list(map(int,input()))
xor_till = 0
res = []
for i in range(n):
	binary[i] = binary[i] ^ xor_till
	res.append(binary[i])
	xor_till = xor_till ^ binary[i]
	if i>=rounds-1:
		xor_till = xor_till^binary[i-rounds+1]
		print(i-rounds+1)
for r in res:
    print(r,end='')