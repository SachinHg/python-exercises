def issumpresent(A,start,target):
	rem = A[0]
	start = 0
	n = len(A)
	for i in range(1,n+1):
		while rem > target and start < i-1:
			rem-=A[start]
			start+=1
		if rem == target:
			return [start,i]
		if i < n:
			rem+=A[i]
	return False

A = [4,5,6,3,1,3]
t = 13
print(issumpresent(A,0,t))
