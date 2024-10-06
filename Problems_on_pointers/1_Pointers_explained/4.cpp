#include<bits/stdc++.h>
using namespace std;

int main(){

    int a = 5;
    int *p = &a;
    int *q = p;
   

    cout<<a<<endl;
    // this would print the value of a - 5
    cout<<&a<<endl;
    // this would print the address of a,  stored in memory
    
    cout<<p<<endl;
    // This would print the address of a

    cout<<&p<<endl;
    // this would print the address of p and not a!

    cout<<*p<<endl;
    // This would print value of p - 5

    cout<<*q<<endl;
    // This would print the value of a - 5

    cout<<q<<endl;
    // This would print the address of a
    
}