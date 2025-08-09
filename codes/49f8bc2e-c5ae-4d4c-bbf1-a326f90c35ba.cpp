#include <iostream>
using namespace std;

int main() {
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        int ans=0;
        while(n>0){
            int r=n%10;
            ans+=r;
            n/=10;
        }
        cout<<ans<<endl;
    }
    // your code here
    return 0;
}