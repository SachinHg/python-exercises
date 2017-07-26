def minWindow(s, t):
        m = len(s)
        n = len(t)
        if m < n:
            return ''
        lt = {}
        for i in t:
            if i not in lt:
                lt[i] = 1
            else:
                lt[i] += 1
        missing = n
        i = I = J = 0
        for j, c in enumerate(s, 1):   
            print("::::::::",c,j) 
            if c in lt and lt[c] > 0:
                missing -= 1
            if c in lt:
                lt[c] -= 1
            while i < j and missing <= 0:
                if J <= 0 or j-i < J-I:
                    I, J = i, j
                if s[i] not in lt:
                    i += 1
                    continue
                else:
                    lt[s[i]] += 1
                    if lt[s[i]] > 0:
                        missing += 1
                    i += 1
        return s[I:J]

print(minWindow('asdasfaf','df'))