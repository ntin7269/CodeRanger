#include<bits/stdc++.h>
using namespace std;

int  main(){

int t;
cin>>t;
while(t--){
int n;
cin>>n;
long long ans=0;
while(n>0){
int rem=n%10;
ans+rem;
n/=10;
}
cout<<ans<<endl;
}