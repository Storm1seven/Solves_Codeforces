/* I feel the need... the need for speed. */
#include<bits/stdc++.h>
using namespace std;
# define ll long long
# define vll vector<ll>
# define vvll vector<vector<ll>>
# define vchar vector<char>
# define vstr vector<string>
# define vpll vector<pair<ll, ll>>
# define mll map<ll, ll>
# define sll set<ll>
# define schar set<char>
# define pll pair<ll, ll>
# define append_left push_front
# define append push_back
# define pop_left pop_front
# define popb pop_back
# define add insert
# define all(v) v.begin(), v.end()
# define rall(v) v.rbegin(), v.rend()
# define loop(i, k, n, inc) for(ll i = k; i < n; i+=inc)
# define rloop(i, k, n, inc) for(ll i = k; i > n; i+=inc)
# define printlist(a) {for(auto i : a){cout<<i<<' ';} cout<<'\n';}
vll vin(ll n){vll a(n); loop(i, 0, n, 1) cin>>a[i]; return a;}
ll intin() {ll n; cin>>n; return n;}
int main(){
    ios_base::sync_with_stdio(false);
    ll n = intin();
    vll a = vin(n);
    ll m = intin();
    vll b = vin(m);
    mll d;
    loop(i, 0, n ,1 ) d[a[i]] = i;
    ll v = 0, p = 0;
    for(auto i:b){
        v+=d[i]+1;
        p+=n-d[i];
    }
    cout<<v<<" "<<p<<"\n";
    return 0;
}