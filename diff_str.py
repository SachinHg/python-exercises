# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for i in range(t):
     s1 = list(input())
     s2 = list(input())
     s1 = sorted(list(set(s1)))
     s2 = sorted(list(set(s2)))
     s_diff = {}
     res = []
     for c in s1:
          s_diff[c] = 1
     for c in s2:
          if c in s_diff:
               s_diff[c] = 0
          else:
               s_diff[c] = 1
     #print(s_diff)
     for c in s1:
          if s_diff[c]==1:
               res.append(c)
     for c in s2:
          if s_diff[c]==1:
               res.append(c)
     if len(res)>0:
          print(''.join(sorted(res)))
          
     
     