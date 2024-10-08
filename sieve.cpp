#include <bits/stdc++.h>
using namespace std;
#define int long long
// sieve= n(log(log(n)))
const int N = 1e7 + 10;
vector<bool> isPrime(N, 1);
vector<int> lp(N, 0), hp(N);
void sieve()
{
    isPrime[0] = isPrime[1] = false;
    for (int i = 2; i < N; i++)
    {

        if (isPrime[i] == true)
        {
            lp[i] = hp[i] = i;
            for (int j = 2 * i; j < N; j += i)
            {
                isPrime[j] = false;
                hp[j] = i; // highest prime
                if (lp[j] == 0)
                    lp[j] = i; // lowest prime
            }
        }
    }
}
signed main()
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);
    int t;
    cin >> t;
    sieve();
    while (t--)
    {
        int n;
        cin>>n;
        cout<<n<<" "<< isPrime[n]<<endl;
    }
    return 0;
}
