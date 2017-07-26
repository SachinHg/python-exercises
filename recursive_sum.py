def recursive(arr):
    if len(arr) == 1:
        print(arr[0])
        return
    else:
        s = 0
        arr_dup = arr[:]
        arr_dup = [int(x) for x in arr_dup]
        s = sum(arr_dup)
        arr = str(s)
        recursive(arr)

n,k = input().split(' ')
print("////",n)
#multiply n k times and send the product to the recursive function
arr_expd = int(n)*int(k)
arr_expd = str(arr_expd)
arr_expd = [int(x) for x in arr_expd]
s = recursive(arr_expd)