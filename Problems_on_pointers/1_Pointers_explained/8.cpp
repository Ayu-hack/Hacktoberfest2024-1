#include<bits/stdc++.h>
using namespace std;

int main(){

    int arr[4] = {10, 20, 30, 40};

    int *p = arr;
    int *q = arr+1;


    cout<<arr<<endl;//base address
    cout<<&arr<<endl;//base address
    cout<<&arr[0]<<endl;//base address
    cout<<arr[0]<<endl;//first element
    cout<<p<<endl;//base address
    cout<<*p<<endl;//10
    cout<<&p<<endl;//address of p
    cout<<q<<endl;//address of 2nd element
    cout<<*q<<endl;//20
    cout<<&q<<endl;//address of q
    cout<<*p+1<<endl;//11
    cout<<*p+2<<endl;//12
    cout<<*q+1<<endl;//21
    cout<<*q+2<<endl;//22
}