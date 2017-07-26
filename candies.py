n = int(input())
count = [0]*(n+2)
for i in range(n):
	ratings.append(int(input()))
ratings = [ratings[0]]+ratings
ratings = ratings + [ratings[n]]
if ratings[1] >= ratings[0]:
	count[0] = 1
if ratings[n+1] <= ratings[n]:
	count[n+1] = 1
for i in xrange (1,n+1,1):
	if  ratings[i] <= ratings[i-1] and ratings[i] <= ratings[i+1]:
		count[i] = 1
#print ratings
#print count
for i in xrange(n+2):
    if count[i] != 1:
        if ratings[i] > ratings[i-1]:
            count[i] = max(count[i-1]+1,count[i])
for i in xrange(n+1,-1,-1):
    if count[i] != 1:
        if ratings[i+1] < ratings[i]:
            count[i] = max(count[i], count[i+1]+1)
total = 0        
#print count
for i in count:
    total = total + i
print total - 2