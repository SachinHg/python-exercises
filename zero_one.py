t = int(input())
ii=0
res = []
while ii < t:
     max1 = 0
     size = int(input())
     array = input()
     array = list(map(int, array.split(' ')))
     M = [0]*size
     for j in range(size):
          M[j] = 1
     for j in range(size):
          # for i in range(j):
          i = j-1
          if abs(array[j] - array[i]) == 1: #and M[j] < M[i]+1:
               M[j] = M[i]+1
     max1 = max(M)
     res.append(max1)
     print(max1)
     ii+=1
for r in res:
     print(r)