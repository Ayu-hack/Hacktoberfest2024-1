#include<bits/stdc++.h>
using namespace std;

int main(){

    int a = 50;
    
    int *p = &a;
    // this would store the value of a
    // can also write it as p = &a!

    int *q = p;
    // This would store the address of a
    // can also write it as q = p or q = p = &a

    int *r = q;
    // This would store the address of a
    // can also write it as r = q = p = &a!
    cout<<a<<endl;
    // This would print the value of a - 50

    cout<<p<<endl;
    // This would print the address of a

    cout<<q<<endl;
    // This would also print the address of a
    
    cout<<&a<<endl;
    // This would also print the address of a
    cout<<&p<<endl;
    // this would print the address of p and not a!

    cout<<*p<<endl;
    // This would print the value of a - 50
    cout<<*q<<endl;
    // This would print the value of a - 50

    cout<<*r<<endl;
    // This would also print the value of a - 50
}