def swap(a,b):
    t = a
    a = b
    b = t
    return a,b
def partition(A,l,h):
    p = A[h]
    i = l-1
    for j in range(l,h):
        if A[j] <= p:
            i+=1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[h] = A[h],A[i+1]
    res = []
    for digit in A:
        res.append(str(digit))
    print(' '.join(res))
    return i+1

def qsort(A,l,h):
    if l < h:
        p = partition(A,l,h)
        qsort(A,l,p-1)
        qsort(A,p+1,h)
def printArray(A,n):
    for i in range(n):
        print(A[i],end=' ')

a = [1,3,9,8,2,7,5]
n = len(a)
qsort(a,0,n-1)
# printArray(a,n)