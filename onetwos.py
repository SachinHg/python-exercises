t = int(input())
ones = [1,2,3,4,5]
for _ in range(t):
     n = int(input())
     i = 1
     cnt = 0
     while i <=n:
          ii = i
          flag = 1
          while ii > 0:
               dig = ii%10
               if dig not in ones:
                    flag = 0
                    break
               ii = ii//10
          if flag == 1:
               cnt+=1
          i+=1
     print(cnt)