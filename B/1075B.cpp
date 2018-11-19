#include<bits/stdc++.h>
using namespace std;

int main(){
	int n, m;
	cin>>n>>m;
	vector<int> a, b, passenger, driver, answer;
	for (int i = 0; i< m; i++) answer[i] = 0;
	for (int i = 0; i<n+m; i++){
		int in;
		cin>>in;
		a.push_back(in);
	}
	for (int i = 0; i<n+m; i++){
		int in;
		cin>>in;
		b.push_back(in);
	}
	for (int i = 0; i < n+m; i++){
		if (b[i] == 0) passenger.push_back(a[i]);
		else driver.push_back(a[i]);
	}
	int j = 0;
	for (int i = 0; i < n; i++){
		while (i < m-1) && (passenger[i] > (driver[i] + driver[i+1])/2){
			j+=1;
		}
		answer[i]+=1;
	}
	for(int i = 0; i < m; i++) cout<<answer[i]<<" ";
	cout<<endl;
	return 0;
}