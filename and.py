import math

# t = int(input())
# for _ in range(t):
# 	a,b = map(int,input().split(' '))
# 	init = a^b
# 	diff = math.floor(math.log(init,2))+1
# 	b>>=diff
# 	b<<=diff
# 	print(b)

### method 2

t = int(input())
for _ in range(t):
	a,b = map(int,input().split(' '))
	res = a&(a+1)
	i = 1
	while a+(2**i) <= b:
		res = a+(2**i)&res
		i+=1
	print(res&b)

### Another method search from the top until you find a bit that is 'on' for "b" but not "a". Then you stop

T = int(input())
for t in range(T):
    a , b = map(int, input().split(' '))
    res = 0
    for k in range(32, -1, -1):
        s = 1<<k
        if b&s:
            if a&s:
                res |= s
            else:
                break
    print(res)