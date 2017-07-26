a = list(map(int,input().split(' ')))
n = len(a)
t = 0
for i in range(n):
	# print("????")
	t = a[i]
	while t < n and a[t]+1=t:
		# print(":::")
		tt = t
		t = a[tt]
		a[tt] = tt
		# print("aaaarrrayyy",a)
for i in range(n):
	if a[i] != i:
		print(i)
		break
# for i in range(n):
# 	a[a[i]]-=i

###interview bit solution

def firstMissingPositive(self, A):
    j = 0
    n = len(A)
    for i in range(n):
        if A[i] <= 0:
            A[i],A[j] = A[j],A[i]
            j+=1
    for i in range(j,n):
        if abs(A[i])-1+j < n and A[abs(A[i])-1+j] > 0:
            A[abs(A[i])-1+j] = -A[abs(A[i])-1+j]
    
    for i in range(j,n):
        if A[i] > 0:
            return i-j+1
    return n - j + 1
