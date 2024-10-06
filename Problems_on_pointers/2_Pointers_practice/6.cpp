#include<bits/stdc++.h>
using namespace std;

int main(){

    int a = 7;
    int *c = &a;
    c = c+1; // the address of c pointer shifts 4 bytes ahead of address of a, thus giving some garbage value
    cout<<a<<" "<<*c<<endl;
    
    // output : 7 garbage_value(system defined!)
}