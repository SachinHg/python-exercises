# # Enter your code here. Read input from STDIN. Print output to STDOUT
# t = int(input())
# for i in range(t):
#     size = int(input())
#     array = list(map(int,input().split(' ')))
#     sum1 = array[0]
#     max_sum1 = 0
#     for i in range(1,size):
#         sum1+=array[i]
#         max_sum1 = max(array[i],sum1,max_sum1)
#     #print(max_sum1)
#     max_sum2 = array[0]
#     sum2 = array[0]
#    # print("????",sum2)
#     for i in range(1,size):
#     #    print("$$$$$$",array[i])
#         sum2+=array[i]
#      #   print("<<<>>>",sum2)
#         max_sum2 = max(sum2,max_sum2)
#         sum2 = max_sum2
#       #  print("::::",max_sum2)
    
#     print(max_sum1,max_sum2)

size = int(input())
arr = list(map(int,input().split(' ')))
h = m = t = arr[0]
for i in range(1,arr):
    t = max(t, n, t + n)
    h = max(n, h + n)
    m = max(m, h)
print(m, t)


t = int(input())
for i in range(t):
    size = int(input())
    array = list(map(int,input().split(' ')))
    temp_sum = sub_sum = seq_sum = array[0]
    for i in range(1,size):
        seq_sum = max(seq_sum, array[i], seq_sum + array[i])
        temp_sum = max(array[i], temp_sum + array[i])
        sub_sum = max(sub_sum, temp_sum)
    print(sub_sum, seq_sum)