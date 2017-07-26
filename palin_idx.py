def palindromeIndex(s):
    s_r = s[::-1]
    len1 = len(s)
    if s == s_r:
        return -1
    else:
        i = 0
        s_ar = list(s)
        while i < len1//2:
            if s_ar[i] != s_ar[len1-1-i] :
                if s_ar[i+1] == s_ar[len1-1-i] and s_ar[i+2]==s_ar[len1-1-i]:
                    return i
                elif s_ar[i]==s_ar[len1-1-i-1] and s_ar[i+1]==s_ar[len1-1-i-2]:
                    return len1-1-i
            else:
                i+=1
        return -1
    # Complete this function

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = palindromeIndex(s)
    print(result)
