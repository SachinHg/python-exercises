def makingAnagrams(s1,s2):
    l1 = len(s1)
    l2 = len(s2)
    s1_ar = list(s1)
    s2_ar = list(s2)
    int1 = set(s1_ar)
    int2 = set(s2_ar)
    count = 0
    chr_dict = {}
    for i in int1:
        if i not in chr_dict:
            c1 = s1_ar.count(i)
            c2 = s2_ar.count(i)
            chr_dict[i] = abs(c1-c2)
    for i in int2:
        if i not in chr_dict:
            c1 = s1_ar.count(i)
            c2 = s2_ar.count(i)
            chr_dict[i] = abs(c1-c2)
    vals = list(chr_dict.values())
    count = sum(vals)
    return count
s1 = input().strip()
s2 = input().strip()
result = makingAnagrams(s1, s2)
print(result)
