/* I feel the need... the need for speed. */
#include<bits/stdc++.h>
using namespace std;
# define ll long long
# define vll vector<ll>
# define vpll vector<pair<ll, ll>>
# define append_left push_front
# define append push_back
# define pop_left pop_front
# define pop pop_back
# define add insert
# define loop(i, k, n, inc) for(ll i = k; i < n; i+=inc)
# define rloop(i, k, n, inc) for(ll i = k; i > n; i+=inc)
# define printlist(a) {for(auto i : a){cout<<i<<' '; cout<<'\n';}}
int main(){
    ios_base::sync_with_stdio(false);
    ll n; cin>>n;
    vpll a;
    ll x, y, count = 0;
    loop(i, 0, n, 1){
        cin>>x>>y;
        a.append(make_pair(x, y));
    }
    loop(i, 0, n, 1){
        loop(j, i+1, n, 1){
            if (a[i].first == a[j].second) count++;
            if (a[i].second == a[j].first) count++;
        }
    }
    cout<<count<<"\n";
    return 0;
}
