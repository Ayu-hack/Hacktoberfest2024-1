#include<bits/stdc++.h>
using namespace std;

int main(){

    int a = 5;
    int *p = &a;
    int **q = &p;

    cout<<a<<endl;//5
    cout<<&a<<endl;//address of a
    cout<<p<<endl;//address of a
    cout<<&p<<endl;// address of p
    cout<<*p<<endl;// value of a
    cout<<q<<endl;// address of p
    cout<<&q<<endl;// address of q
    cout<<*q<<endl;// address of a
    cout<<**q<<endl;//5
}