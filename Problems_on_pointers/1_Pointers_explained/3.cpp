#include<bits/stdc++.h>
using namespace std;

int main(){

    int a = 100;
    int *ptr = &a;

    cout<<a<<endl; // 100
    cout<<&a<<endl; // address of a
    
    cout<<ptr<<endl; // address of a 
    cout<<*ptr<<endl; // value at address stored in ptr - 100
    (*ptr)++;
    cout<<*ptr<<endl; // value at address stores in ptr increments by 1 - 101
    ++(*ptr); //value at address ptr increments by 1 after value assigned already - 102
    cout<<*ptr<<endl;
    *ptr = (*ptr / 2); // value stored at address ptr is divided by 2 - 51
    cout<<*ptr<<endl; // 51
    *ptr = (*ptr-2);// value at address ptr is decreased by 2 - 49
    cout<<*ptr<<endl; // 49
}