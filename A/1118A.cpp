#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main(){
    ll t, n, a, b, ans;
    cin>>t;
    for (ll ii = 0; ii < t; ii++){
        cin>>n>>a>>b;
        ans = 0;
        if (b <= 2*a){
            if (n%2 == 0) ans = n*b/2;
            else ans = (n-1)*b/2 + a;
        }
        else ans = n*a;
        cout<<ans<<"\n";
    }
    return 0;
}