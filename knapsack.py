def knapsack(weights,vals,W):
	n = len(vals)
	K = [[0 for i in range(W+1)] for j in range(n+1)]
	for i in range(n+1):
		for w in range(W+1):
			if i == 0 or w == 0:
				K[i][w] = 0
			elif weights[i-1] <= w:
				K[i][w] = max(K[i-1][w],vals[i-1]+K[i-1][w-weights[i-1]])
			else:
				K[i][w] = K[i-1][w]
	return K[n][W]

vals = [60,100,120]
weights = [10,20,30]
W = 50
print(knapsack(weights,vals,W))