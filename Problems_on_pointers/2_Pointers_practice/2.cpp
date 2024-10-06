#include<bits/stdc++.h>
using namespace std;

int main(){

    int a = 7;
    int b = 17;
    int *c = &b;
    *c = 7;

    cout<<a<<" "<<b<<endl;

    // output : 7 7
}