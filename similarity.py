# t = int(input())
# for ii in range(t):
#     s = list(input())
#     z = [0]*len(s)
#     ii = 0
#     l = len(s)
#     count = 0
#     for i in range(1,l):
#         j = 0
#         while a[j] == a[i+j]:
#             count+=1
#             j+=1
#     print(count)

void getZarr(string str, int Z[]);
 
//  prints all occurrences of pattern in text using Z algo
long search(string text)
{
    long l = text.length();
    // Construct Z array
    int Z[l];
    getZarr(text, Z);
     long r=0;
    //  now looping through Z array for matching condition
    for (long i = 1; i < l; ++i)
    {
        
        r = r+Z[i];
    }
    return r;
}
 
//  Fills Z array for given string str[]
void getZarr(string str, int Z[])
{
    long n = str.length();
    long L, R, k;
 
    // [L,R] make a window which matches with prefix of s
    L = R = 0;
    for (long i = 1; i < n; ++i)
    {
        // if i>R nothing matches so we will calculate.
        // Z[i] using naive way.
        if (i > R)
        {
            L = R = i;
            while (R<n && str[R-L] == str[R])
                R++;
            Z[i] = R-L;
            R--;
        }
        else
        {
            
            k = i-L;
 
            
            if (Z[k] < R-i+1)
                 Z[i] = Z[k];
 
            
            else
            {
                //  else start from R  and check manually
                L = i;
                while (R<n && str[R-L] == str[R])
                    R++;
                Z[i] = R-L;
                R--;
            }
        }
    }
}
 
// Driver program
int main()
{
    int t;cin>>t;
    while(t--)
        {
    string s;  cin>>s;
        long n = s.length();
    cout<<search(s)+n<<endl;
    }
}


t = int(input())
for i in range(t):
    s = input()
    l = len(s)
    print(search(s)+l)