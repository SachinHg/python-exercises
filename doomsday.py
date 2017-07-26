from fractions import gcd

def gcd (a,b):
    while b!= 0:
        (a,b) = (b,a%b)
    return a

def gcd_list(lst):
    len1=len(lst)
    gcd_fin = 0
    for i in range(0,len1):
        gcd_fin=gcd(gcd_fin,lst[i])
    return gcd_fin

def answer(matrix):
    init_len=len(matrix)
    init_matrix=list(matrix)
    for i,elem in enumerate(init_matrix):
        elem[i]=0
    sums=[sum(i) for i in init_matrix]
    actual_probs=[i for i,item in enumerate(sums) if item==0]
    not_probs=list((set(range(init_len)) - set(actual_probs)))
    L=len(not_probs)
    for i in range(0,L-1):
        indB=not_probs[L-i-1]
        for j in range(0,L-1):
            indA=not_probs[j]        
            init_matrix[indA]=merge_matrices(init_matrix[indA],indA,init_matrix[indB],indB)
    fin_ans=[]
    for i in actual_probs:
        fin_ans.append(init_matrix[0][i])
    tot=sum(fin_ans)
    fin_ans.append(tot)
    if tot == 0:
        fin_ans=[1 for i in terms]
        fin_ans.append(len(terms))
    return fin_ans

def merge_matrices(v1,i1,v2,i2):
    lenV=len(v1)
    indices=(set(range(lenV))-{i1,i2})
    sum2=sum(v2)
    matrix_tmp = [0 for i in v1]
    for i in indices:
        matrix_tmp[i]= sum2*v1[i]+v1[i2]*v2[i]
    common_denom = gcd_list(matrix_tmp)
    value = [int( i / common_denom ) for i in matrix_tmp ]
    return value