#include<bits/stdc++.h>
using namespace std;

int main(){
    int n, a[3];
    int count = 0;
    cin>>n;
    for(int i = 0;  i<3; i++){
        cin>>a[i];
    }
    int z = sizeof(a)/sizeof(a[0]); 
    sort(a, a+z); 
    while (n>0){
        if (n >= a[0]){
            n-=a[0];
            count+=1;
        }
        else if(n >= a[1] ){
            n-=a[1];
            count+=1;
        }
        else{
            n-=a[2];
            count+=1;
        }
    }
    cout<<count<<endl;
    return 0;
}