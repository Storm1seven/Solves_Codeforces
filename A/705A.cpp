#include<iostream>
using namespace std;

int main(){
    int n;
    string x = "that";
    cin>>n;
    for(int i = 0; i<n; i++){
        if (i == n-1) x = "it";
        if (i%2 == 0) cout<<"I hate "<< x <<" ";
        else cout<<"I love "<< x <<" ";
    }
    cout<<endl; 
    return 0;
}