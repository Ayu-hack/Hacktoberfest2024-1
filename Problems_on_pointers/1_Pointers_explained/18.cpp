#include<bits/stdc++.h>
using namespace std;

void solve(int * &p){

    *p = *p + 5;
    // Here the parameters is pass by value , thus it is a (PASS BY VALUE) and not PASS BY REFERENCE!

    // pass by value
    // int *p
    
    // pass by reference
    // int* &p
    
}

int main(){

    int a = 5;
    int *p = &a;

    cout<<p<<endl;// address of a
    cout<<&p<<endl;// address of p
    cout<<*p<<endl;// 5

    solve(p);

    cout<<p<<endl;//address of a
    cout<<&p<<endl;// address of 
    cout<<*p<<endl;//10
}