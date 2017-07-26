t = int(input())
for ii in t:
    s = input()
    check = 1
    for i in range(1,len(s)//2+1):
        n = int(s[:i])
        if ''.join(map(str, [n+j for j in range(len(s)//i)]))[:len(s)] == s:
            print("YES "+str(n))
            check = 0
            break
    if check == 1:            
        print('NO')