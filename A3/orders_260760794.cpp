#include <bits/stdc++.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

using namespace std;

void run_one_time(vector<int>& v, vector<int> cost, int ord) {
    
    vector<int> ans;

    if(-1==v[ord]) {cout<<"Ambiguous"<<endl; return;}

    if(-2==v[ord]) {cout<<"Impossible"<<endl; return;}

    while(0<ord) {
        ans.push_back(1 + v[ord]);
        ord = ord - cost[v[ord]];
    }

    if(0>ord) {cout<<"Ambiguous"<<endl; return;}

    sort(ans.begin(),ans.end());
    
    for(auto i : ans){cout<<i<<" ";}

    cout<<endl;
}

int main() {
    vector<int> v(32000, -2);
    
    v[0] = 0;

    int n;
    cin >> n;
    
    vector<int> costs(n);
    
    for(auto& i : costs) {cin >> i;}

    for(int i=0; i<n; i++) {
       
        int cost = costs[i];
       
        for(int j=0; j<=30000; j++) {
       
            if(0<=v[j]) {
                if(-2==v[j+cost]){v[j+cost]=i;}
                else{v[j+cost] = -1;}
            }
       
            if(v[j] == -1) {v[j+cost]=-1;}
        }
    }

    int q;

    cin>>q;

    for(int i=0; i<q; i++) {

        int ord;

        cin>>ord;

        run_one_time(v, costs, ord);
    }
}