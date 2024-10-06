#include<bits/stdc++.h>
using namespace std;

int main(){

    int a = 10;
    int *p = &a;
    int **q = &p;
    int **r = &p;
    int ***s = &q;

    cout<<a<<endl;//10
    cout<<p<<endl;//address of a
    cout<<&s<<endl;// address of s and not q!
    cout<<&r<<endl;//address of r and not p!
    cout<<&q<<endl;//address of q and not p!
    cout<<*s<<endl;//address of p
    cout<<**r<<endl;//10
    cout<<***s<<endl;//10
    cout<<**q<<endl;//10
    cout<<**s<<endl;//address of a
    cout<<*q<<endl;//address of a
}