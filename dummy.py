def max_sum(A):
    max_till = max_end = A[0]
    for i in range(1,len(A)):
        max_till = max(A[i],A[i]+max_till)
        max_end = max(max_till,max_end)
    return max_end
t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int,input().split(' ')))
    s = max_sum(A)
    print(s)