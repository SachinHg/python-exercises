# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for i in range(t):
    count = 0
    size = int(input())
    array = list(map(int, input().split(' ')))
    array = sorted(array)
    ar_set = sorted(list(set(array)))
    while len(ar_set) !=1:
        #print(ar_set)
        min_diff = abs(ar_set[1]-ar_set[0])
        if min_diff >= 5:
            ar_set = [ch-5 if ch !=ar_set[1] else ch for ch in ar_set]
            count+=1
            #print(ar_set)
        elif min_diff >=2:
            ar_set = [ch-2 if ch !=ar_set[1] else ch for ch in ar_set]
            count+=1
            #print(ar_set)
        elif min_diff == 1:
            ar_set = [ch-1 if ch !=ar_set[1] else ch for ch in ar_set]
            count+=1
        #print(ar_set)
        ar_set = sorted(list(set(ar_set)))
        # print(ar_set)
    print(count)
        
