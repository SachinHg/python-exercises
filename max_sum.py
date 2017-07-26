"""(1) optimal solution must consist of either 1 or Bi for each position. proof left to reader. you can go through the various cases to see that if we have a solution consist of a point that's not 1 or Bi, then we can better that solution using 1 or Bi instead of that point 1<=x<=Bi.
(2) define three functions:
L(i) = max cost using first i items of array B, ending with 1 at i th position. {note: 1 is low so we use L to denote low}
H(i) = max cost for first i items of array B, ending in Bi at i th position. {note: Bi is higher of 1 or Bi thus use H to denote that}
F(i) = max cost for first i items regardless of ending.
L(i) = max (L(i-1),H(i-1)+|B(i-1) - 1|)
H(i) = max (H(i-1)+|B(i)-B(i-1)|,L(i-1)+|B(i) - 1|)
F(i) = max(L(i),H(i))
This take advantage of the fact that, the optimal solution for either L(i) or H(i) must be based on the optimal solution for L(i-1) and H(i-1). 
We see this must be true, since if L(i) or H(i) doesn't contain a prefix that's optimal i.e. doesn't contain either L(i-1) or H(i-1) prefixes, then we can better this solution by replacing it using L(i-1) or H(i-1) prefixes.
Using the above we can compute the answer simply using code like this:"""



t = int(input())
for i in range(t):
    size = int(input())
    array = list(map(int, input().split(' ')))
    max_cur, max_fin = 0,0
    for j in range(1,size):
        ele = array[j]
        prev = array[j-1]
        max_cur_1 = max(max_cur+abs(ele-prev),max_fin+(ele-1))
        max_fin_1 = max(max_cur+abs(prev-1), max_fin)
        max_cur,max_fin = max_cur_1, max_fin_1
    print(max(max_cur,max_fin))