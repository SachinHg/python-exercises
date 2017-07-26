t = int(input())
for _ in range(t):
    size = int(input())
    mat = []
    for i in range(size):
        mat_t = list(input())
        mat_t = sorted(mat_t)
        for m in mat_t:
            mat.append(m)
    flag = 1
    #print(mat)
    if size > 1:
        for i in range(0,len(mat) - size):
            #print(":::::::::",mat[i],mat[i+size])
            if mat[i] > mat[i + size]:
                flag = 0
                break
        if flag == 1:
            print('YES')
        else:
            print('NO')
    else:
        print('YES')