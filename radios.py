rows,cols,tracks = map(int,input().split(' '))
mat = [[0 for i in range(cols)]for j in range(rows)]
cnt = 0
hash1 = {}
for _ in range(tracks):
    row_no, start,end = map(int,input().split(' '))
    if hash1.get(row_no,[]):
        vals = hash1[row_no]
        if vals[0] > start:
            vals[0] = start
        if vals[1] < end:
            vals[1] = end
    else:
        hash1[row_no] = [start,end]
count = 0
for h in hash1:
    vals = hash1[h]
    tmp = vals[1]-vals[0]+1
    count+=tmp
print(rows*cols - count)