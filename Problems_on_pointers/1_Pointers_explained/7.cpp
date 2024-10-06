#include<bits/stdc++.h>
using namespace std;

int main(){

    int a = 5;
    int *p = &a;

    p = p+1;

    cout<<p<<endl;
    cout<<*p<<endl; // This prints the garbage value

    // But in the case of an array

    int arr[] = {10, 20, 30, 40, 50};

    cout<<arr<<endl;
    
    
    // arr = arr+1;
    // Why the above statement gives error when you try to modify the base address of the array as it is also a pointer just as p!
}